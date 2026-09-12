$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
Push-Location $projectRoot
try {
    & .\gradlew.bat :android:testDebugUnitTest
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

    npx --yes --package ajv-cli@5.0.0 --package ajv-formats@3.0.1 ajv validate --spec=draft2020 --all-errors -c ajv-formats -s contracts/asset-schema-v1.schema.json -d "android/build/generated/kotlin-asset-schema-v1/*.json"
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
finally {
    Pop-Location
}
