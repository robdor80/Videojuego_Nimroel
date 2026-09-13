package com.nimroel.assetmanager.domain.processing

import com.nimroel.assetmanager.domain.identity.AssetIdGenerator
import com.nimroel.assetmanager.domain.identity.WorkIdGenerator
import com.nimroel.assetmanager.domain.model.Content
import com.nimroel.assetmanager.domain.storage.IngestWorkItem
import com.nimroel.assetmanager.domain.storage.IngestWorkItemStore
import com.nimroel.assetmanager.domain.storage.IngestWorkState
import com.nimroel.assetmanager.domain.storage.IngestWorkTransition
import java.time.Clock
import java.time.Instant
import kotlinx.coroutines.CancellationException

fun interface StagingFileStore {
    suspend fun stageVerified(
        workId: String,
        sourceRef: ImageSourceRef,
        expectedContent: Content,
    ): StagedImage
}

data class StagedImage(
    val relativePath: String,
    val content: Content,
)

enum class StagingErrorCode(val wireValue: String) {
    SOURCE_UNAVAILABLE("source_unavailable"),
    STAGING_WRITE_FAILED("staging_write_failed"),
    STAGING_VERIFY_FAILED("staging_verify_failed"),
    SOURCE_CHANGED("source_changed"),
    INVALID_IMAGE("invalid_image"),
    UNEXPECTED_IO("unexpected_io"),
}

class StagingException(
    val code: StagingErrorCode,
    detail: String,
    cause: Throwable? = null,
) : Exception(detail, cause)

sealed interface LocalIngestResult {
    data class Ready(
        val workItem: IngestWorkItem,
        val stagedImage: StagedImage,
    ) : LocalIngestResult

    data class Failed(val workItem: IngestWorkItem) : LocalIngestResult
}

class LocalIngestCoordinator(
    private val assetIdGenerator: AssetIdGenerator,
    private val workIdGenerator: WorkIdGenerator,
    private val stagingFileStore: StagingFileStore,
    private val workItemStore: IngestWorkItemStore,
    private val clock: Clock = Clock.systemUTC(),
) {
    suspend fun begin(preparedImage: PreparedImage): LocalIngestResult {
        val createdAt = now()
        val queued = IngestWorkItem(
            workId = workIdGenerator.generate(),
            reservedAssetId = assetIdGenerator.generate(),
            sourceUri = preparedImage.sourceRef.value,
            state = IngestWorkState.QUEUED,
            createdAt = createdAt,
            updatedAt = createdAt,
        )
        workItemStore.createIngestWorkItem(queued)
        val processing = transition(
            IngestWorkTransition(
                workId = queued.workId,
                expectedState = IngestWorkState.QUEUED,
                targetState = IngestWorkState.PROCESSING,
                updatedAt = now(),
            ),
        )
        return try {
            val staged = stagingFileStore.stageVerified(
                workId = processing.workId,
                sourceRef = preparedImage.sourceRef,
                expectedContent = preparedImage.content,
            )
            val ready = transition(
                IngestWorkTransition(
                    workId = processing.workId,
                    expectedState = IngestWorkState.PROCESSING,
                    targetState = IngestWorkState.READY_TO_COMMIT,
                    updatedAt = now(),
                    stagingRelativePath = staged.relativePath,
                ),
            )
            LocalIngestResult.Ready(ready, staged)
        } catch (error: StagingException) {
            val failed = transition(
                IngestWorkTransition(
                    workId = processing.workId,
                    expectedState = IngestWorkState.PROCESSING,
                    targetState = IngestWorkState.FAILED,
                    updatedAt = now(),
                    errorCode = error.code.wireValue,
                    errorDetail = error.message.toBoundedDiagnostic(),
                ),
            )
            LocalIngestResult.Failed(failed)
        } catch (error: CancellationException) {
            throw error
        } catch (error: Exception) {
            transition(
                IngestWorkTransition(
                    workId = processing.workId,
                    expectedState = IngestWorkState.PROCESSING,
                    targetState = IngestWorkState.FAILED,
                    updatedAt = now(),
                    errorCode = StagingErrorCode.UNEXPECTED_IO.wireValue,
                    errorDetail = "Fallo inesperado durante el staging local.",
                ),
            )
            throw error
        }
    }

    private suspend fun transition(value: IngestWorkTransition): IngestWorkItem =
        checkNotNull(workItemStore.transitionIngestWorkItem(value)) {
            "Ingest work item ${value.workId} could not transition from ${value.expectedState.wireValue} to ${value.targetState.wireValue}."
        }

    private fun now(): Instant = Instant.now(clock)
}

private fun String?.toBoundedDiagnostic(): String =
    this.orEmpty()
        .replace(CONTENT_URI, "[fuente externa]")
        .replace('\n', ' ')
        .replace('\r', ' ')
        .take(MAX_DIAGNOSTIC_LENGTH)
        .ifBlank { "El staging local no pudo completarse." }

private const val MAX_DIAGNOSTIC_LENGTH = 240
private val CONTENT_URI = Regex("content://[^\\s]+", RegexOption.IGNORE_CASE)
