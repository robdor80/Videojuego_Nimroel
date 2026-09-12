$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
Push-Location $projectRoot
try {
    npx --yes --package ajv-cli@5.0.0 ajv validate --spec=draft2020 --all-errors -s contracts/vocabularies/vocabulary-v1.schema.json -d "contracts/vocabularies/data/*.json"
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    npx --yes --package ajv-cli@5.0.0 ajv test --spec=draft2020 -s contracts/vocabularies/vocabulary-v1.schema.json -d "contracts/vocabularies/test-fixtures/invalid/missing-label.json" --invalid
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    npx --yes --package ajv-cli@5.0.0 ajv validate --spec=draft2020 --all-errors -s contracts/vocabulary-sets/vocabulary-set-v1.schema.json -d "contracts/vocabulary-sets/data/*.json"
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    npx --yes --package ajv-cli@5.0.0 ajv test --spec=draft2020 -s contracts/vocabulary-sets/vocabulary-set-v1.schema.json -d "contracts/vocabulary-sets/test-fixtures/invalid/*.json" --invalid
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    npx --yes --package ajv-cli@5.0.0 ajv validate --spec=draft2020 --all-errors -s contracts/presets/preset-v1.schema.json -d "contracts/presets/examples/*.json"
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    npx --yes --package ajv-cli@5.0.0 ajv test --spec=draft2020 -s contracts/presets/preset-v1.schema.json -d "contracts/presets/test-fixtures/invalid/*.json" --invalid
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
finally { Pop-Location }
