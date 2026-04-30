# GitHub Workflows Summary

## Overview

You now have two streamlined workflows matching your existing Python library setup:

### 1. **Pull Request Workflow** (`.github/workflows/pr.yml`)
Triggered on: **Pull requests to `main`**

**Version Format**: `X.Y.Z.postPR_NUMBER.devCOMMIT_SHA`
- Example: `0.1.0.post42.dev3a1b2c`

**Single CI Job**:
1. ✅ Lint check (Ruff)
2. ✅ Format check (Ruff)
3. ✅ Run tests
4. 📦 Publish pre-release to GitHub Packages
5. 💬 Auto-comment PR with install command

**Purpose**: Let developers test changes before merging

---

### 2. **Main Release Workflow** (`.github/workflows/main.yml`)
Triggered on: **Pushes to `main` branch**

**Version Format**: `X.Y.Z` (from `pyproject.toml`)
- Example: `0.1.0`

**Single CI Job**:
1. ✅ Lint check (Ruff)
2. ✅ Format check (Ruff)
3. ✅ Run tests
4. 📦 Publish official release to GitHub Packages
5. 🏷️ Create GitHub Release with tag `vX.Y.Z`

**Purpose**: Publish official, stable versions for production use

---

## Workflow Diagram

```
Pull Request Created/Updated
          ↓
   pr.yml (single CI job)
          ↓
Lint → Format → Test → Publish Pre-release
                           ↓
                   Auto-comment PR with version
                   (e.g., 0.1.0.post42.dev3a1b2c)

---

Merge to Main / Push to Main
          ↓
  main.yml (single CI job)
          ↓
Lint → Format → Test → Publish Release & Create Tag
                           ↓
                    GitHub Release v0.1.0
                 Available on GitHub Packages
```

---

## How to Use

### For Developers Testing PRs

1. Open a pull request to `main`
2. Wait for the workflow to complete
3. GitHub will comment with the exact pre-release version
4. Install with:
   ```bash
   uv add zqnt-utils==0.1.0.post42.dev3a1b2c --prerelease=allow
   ```

### For Official Releases

1. Update version in `pyproject.toml`:
   ```toml
   version = "0.2.0"  # Change from 0.1.0
   ```
2. Merge to `main` (or push directly)
3. Workflow automatically:
   - Builds and publishes to GitHub Packages
   - Creates GitHub Release with tag `v0.2.0`
   - Developers can now install stable version:
     ```bash
     uv add zqnt-utils==0.2.0
     ```

---

## Key Features

✅ **Separate concerns**: PRs vs releases handled differently
✅ **Pre-release versioning**: PEP 440 compliant
✅ **Automatic tagging**: GitHub releases created automatically
✅ **Developer feedback**: Auto-commented versions on PRs
✅ **Quality gates**: Lint and tests run before publishing
✅ **No manual steps**: Everything automated

---

## Version Scheme

- **Main releases** (stable): `X.Y.Z`
  - Recommended for production
  
- **Pre-releases** (testing): `X.Y.Z.postN.devSHORTSHA`
  - For PR testing
  - `N` = PR number
  - `SHORTSHA` = commit SHA (first 7 chars)
  - Follows PEP 440 versioning standard

---

## Troubleshooting

### PR workflow didn't publish
- Check GitHub Actions logs for errors
- Ensure lint and tests passed
- Verify token has `packages:write` permission

### Release didn't create tag
- Check that version in `pyproject.toml` is valid
- Ensure main branch workflow ran successfully
- Verify you have write permissions to the repo

### Can't install pre-release
- Use `--prerelease=allow` flag with uv
- Use `--pre` flag with pip
- Check pre-release version format in PR comment
