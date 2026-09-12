package com.nimroel.assetmanager.domain.model

/** Rules beyond decoding. Schema tooling remains the complete structural authority. */
object AssetValidator {
    private val referenceId = Regex("^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
    private val contractVersion = Regex("^[0-9]+\\.[0-9]+(?:\\.[0-9]+)?(?:[-+][0-9A-Za-z.-]+)?$")
    private val mimeType = Regex("^image/[a-z0-9.+-]+$")
    private val sha256 = Regex("^[0-9a-f]{64}$")
    private val namespace = Regex("^[a-z0-9]+(?:[.-][a-z0-9]+)+$")

    fun validate(asset: Asset): List<String> = buildList {
        if (asset.schemaVersion != 1) add("schemaVersion must be 1")
        validateLifecycle(asset, this)
        asset.classification?.let { validateClassification(it, this) }
        asset.subject?.let { validateSubject(it, this) }
        asset.visual?.let { validateVisual(it, this) }
        validateDetails(asset.details, asset.type, this)
        validateContent(asset.content, this)
        validateProvenance(asset, this)
        asset.storage?.let { validateStorage(it, this) }
        asset.extensions?.let { validateExtensions(it, this) }
    }

    private fun validateLifecycle(asset: Asset, errors: MutableList<String>) {
        val value = asset.lifecycle
        if (value.supersededByAssetId == asset.assetId) errors += "supersededByAssetId cannot equal assetId"
        if (value.supersededByAssetId == null && value.note == null) return
        value.note?.takeIf { it.isBlank() || it.length > 1000 }?.let { errors += "lifecycle.note must contain 1..1000 characters" }
    }
    private fun validateClassification(value: Classification, errors: MutableList<String>) {
        if (value == Classification()) errors += "classification cannot be empty"
        pair(value.vocabularyId, value.vocabularyVersion, "classification vocabulary", errors)
        refs(listOf(value.vocabularyId, value.realmId, value.cultureId, value.regionId, value.settlementId), errors)
        ids(value.tags, "classification.tags", errors)
    }
    private fun validateSubject(value: Subject, errors: MutableList<String>) {
        if (value == Subject()) errors += "subject cannot be empty"
        refs(listOf(value.entityId, value.speciesId, value.genderId, value.ageBandId), errors)
    }
    private fun validateVisual(value: Visual, errors: MutableList<String>) {
        if (value == Visual()) errors += "visual cannot be empty"
        pair(value.visualProfileId, value.visualProfileVersion, "visual profile", errors)
        refs(listOf(value.visualProfileId, value.compositionId, value.timeOfDayId, value.weatherId, value.lightingId, value.expressionId), errors)
    }
    private fun validateDetails(details: AssetDetails?, type: AssetType, errors: MutableList<String>) {
        if (details != null && details.assetType != type) errors += "details must match type"
        when (details) {
            is NpcPortraitDetails -> { if (details.professionId == null && details.socialClassId == null) errors += "npc_portrait details cannot be empty"; refs(listOf(details.professionId, details.socialClassId), errors) }
            is LandscapeDetails -> { ref(details.environmentId, errors); ids(details.landformIds, "landformIds", errors); ids(details.waterFeatureIds, "waterFeatureIds", errors); ref(details.seasonId, errors) }
            is SettlementDetails -> { ref(details.settlementScaleId, errors); ref(details.environmentId, errors) }
            is BuildingDetails -> { ref(details.buildingFunctionId, errors); ids(details.materialIds, "materialIds", errors) }
            is InteriorDetails -> { ref(details.interiorFunctionId, errors); ref(details.containingBuildingEntityId, errors) }
            is ObjectDetails -> { ref(details.objectKindId, errors); ids(details.materialIds, "materialIds", errors) }
            is EnvironmentSceneDetails -> { ref(details.sceneFunctionId, errors); ref(details.environmentId, errors); ids(details.featuredEntityIds, "featuredEntityIds", errors) }
            null -> Unit
        }
    }
    private fun validateContent(value: Content, errors: MutableList<String>) {
        if (!mimeType.matches(value.mimeType) || value.mimeType.length > 128) errors += "content.mimeType is invalid"
        if (value.widthPx < 1 || value.heightPx < 1 || value.byteSize?.let { it < 1 } == true) errors += "content dimensions and byteSize must be positive"
        if (!sha256.matches(value.sha256)) errors += "content.sha256 must be 64 lowercase hexadecimal characters"
        if (value.colorSpace?.let { it.isBlank() || it.length > 64 } == true) errors += "content.colorSpace is invalid"
    }
    private fun validateProvenance(asset: Asset, errors: MutableList<String>) {
        val value = asset.provenance
        if (value.originKind == OriginKind.GENERATED && value.generator == null) errors += "generated provenance requires generator"
        if (value.originKind in setOf(OriginKind.EDITED, OriginKind.DERIVED) && value.sourceAssetIds.isNullOrEmpty()) errors += "edited/derived provenance requires sourceAssetIds"
        value.generator?.let { if (!referenceId.matches(it.provider) || it.model?.let(String::isBlank) == true || it.generatedAt.isBlank()) errors += "generator is invalid" }
        value.sourceAssetIds?.let { ids -> if (ids.distinct().size != ids.size) errors += "sourceAssetIds must be unique"; if (asset.assetId in ids) errors += "sourceAssetIds cannot contain assetId" }
        pair(value.promptTemplateId, value.promptTemplateVersion, "prompt template", errors)
        refs(listOf(value.promptTemplateId, value.promptRecordId), errors)
    }
    private fun validateStorage(value: Storage, errors: MutableList<String>) {
        if (value.replicas.isEmpty()) errors += "storage.replicas cannot be empty"
        value.replicas.forEach { replica ->
            ref(replica.replicaId, errors); ref(replica.provider, errors)
            if (listOf(replica.objectId, replica.logicalPath, replica.deliveryUrl).all { it.isNullOrBlank() }) errors += "replica requires objectId, logicalPath, or deliveryUrl"
        }
    }
    private fun validateExtensions(value: Extensions, errors: MutableList<String>) {
        if (value.namespaces.isEmpty()) errors += "extensions cannot be empty"
        value.namespaces.forEach { (key, _) -> if (!namespace.matches(key)) errors += "extension namespace is invalid" }
    }
    private fun pair(id: String?, version: String?, label: String, errors: MutableList<String>) { if ((id == null) != (version == null)) errors += "$label ID and version must be supplied together"; version?.let { if (!contractVersion.matches(it) || it.length > 64) errors += "$label version is invalid" } }
    private fun refs(values: List<String?>, errors: MutableList<String>) = values.forEach { ref(it, errors) }
    private fun ref(value: String?, errors: MutableList<String>) { if (value != null && (!referenceId.matches(value) || value.length > 128)) errors += "reference ID is invalid" }
    private fun ids(values: List<String>?, label: String, errors: MutableList<String>) { if (values != null && (values.isEmpty() || values.distinct().size != values.size)) errors += "$label must be non-empty and unique"; values?.forEach { ref(it, errors) } }
}
