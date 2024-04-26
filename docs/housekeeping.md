# Housekeeping

## Releasing

Release is fully automated and you just need to run the [Release workflow](https://github.com/LedgerHQ/test-project/actions/workflows/release.yml).
Versioning is automatic and guessed from [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/) history.

### Stable release

1. Go to the [Release workflow](https://github.com/LedgerHQ/test-project/actions/workflows/release.yml)
2. Properly select the target branch (given our process, the default `main` is correct)
3. **Optional**: manually select a kind of increment (`MAJOR`, `MINOR`, `PATCH`) if you don't want to rely on automatic versioning
4. Run the workflow

### Pre-release

1. Go to the [Release workflow](https://github.com/LedgerHQ/test-project/actions/workflows/release.yml)
2. Properly select the target branch (given our process, the default `main` is correct)
3. Select the pre-release type (`alpha`, `beta` or `rc`)
4. Run the workflow
