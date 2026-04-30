# ✨ Workflows Updated!

## What Changed

Your workflows have been refactored to match the streamlined pattern from your other Python library. Instead of multiple separate jobs (`lint`, `build`, `test`, `publish`), both workflows now use:

**Single consolidated CI job** that runs all steps sequentially:
- Checkout
- Setup Python + uv
- Install dependencies
- Lint (ruff check)
- Format check (ruff format)
- Run tests
- Create pre-release/release version
- Build package
- Publish to GitHub Packages
- Create GitHub Release (main only) / Comment PR (PR only)

---

## Before vs After

### Main Workflow

**Before:** 4 separate jobs (`lint` → `build` → `test` → `publish-release`)
```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: [lint]
    
  build:
    needs: lint
    runs-on: ubuntu-latest
    steps: [build]
    
  test:
    needs: build
    runs-on: ubuntu-latest
    steps: [test]
    
  publish-release:
    needs: test
    runs-on: ubuntu-latest
    steps: [publish]
```

**After:** 1 consolidated job (`ci`)
```yaml
jobs:
  ci:
    name: Lint · Test · Build · Release
    runs-on: ubuntu-latest
    steps: [lint, format, test, build, publish, release]
```

### PR Workflow

**Before:** 4 separate jobs (`lint` → `build` → `test` → `publish-prerelease`)

**After:** 1 consolidated job (`ci`)
```yaml
jobs:
  ci:
    name: Lint · Test · Build · Publish Preview
    runs-on: ubuntu-latest
    steps: [lint, format, test, build, publish, comment-pr]
```

---

## Benefits of This Approach

✅ **Simpler to understand** - All steps in one sequential flow
✅ **Faster execution** - No job orchestration overhead  
✅ **Easier to debug** - All output in one job log
✅ **Matches your existing patterns** - Consistent with your other libraries
✅ **Less GitHub runner startup overhead**

---

## Files Structure

```
.github/
├── workflows/
│   ├── pr.yml                      # PR pre-release (single CI job)
│   └── main.yml                    # Main release (single CI job)
├── dependabot.yml                  # Automatic dependency updates
├── INSTALLATION.md                 # Developer installation guide
├── WORKFLOWS.md                    # Detailed workflow documentation
├── QUICKREF.md                     # Quick reference guide
└── SETUP_SUMMARY.md                # Setup summary
```

---

## Key Features

✅ **Separate workflows for PRs and main**
✅ **Pre-release versioning**: `X.Y.Z.postN.devSHA` for PRs
✅ **Stable versioning**: `X.Y.Z` for main releases
✅ **Automatic GitHub Releases** with tags
✅ **Auto-commented PR version** for easy testing
✅ **GitHub Packages publishing** included
✅ **Quality gates**: Lint & tests run before publishing
✅ **PEP 440 compliant** versioning

---

## Workflow Triggers

### PR Workflow (`pr.yml`)
- **Trigger**: Pull request to `main` branch
- **Version**: `0.1.0.post42.dev3a1b2c` (PR #42, commit SHA)
- **Publishes**: Pre-release to GitHub Packages
- **GitHub Release**: ❌ No
- **Auto-comment**: ✅ Yes with install command

### Main Workflow (`main.yml`)
- **Trigger**: Push to `main` branch
- **Version**: `0.1.0` (from `pyproject.toml`)
- **Publishes**: Stable release to GitHub Packages
- **GitHub Release**: ✅ Yes with tag `v0.1.0`
- **Auto-comment**: ❌ No

---

## Next Steps

1. **Push these workflows to GitHub**
   ```bash
   git add .github/workflows/
   git commit -m "refactor: streamline workflows with single CI job"
   git push
   ```

2. **Test with a PR**
   - Create a test branch
   - Make a small change
   - Create PR to main
   - Watch workflow run
   - Verify pre-release published and PR commented

3. **Test with a main merge**
   - Merge the test PR
   - Watch main workflow run
   - Verify release published and GitHub Release created

4. **Share with team**
   - Point them to `.github/INSTALLATION.md`
   - Share `.github/QUICKREF.md`

---

## Documentation Files

The setup includes several documentation files for your team:

- **INSTALLATION.md** - How to install from GitHub Packages
- **WORKFLOWS.md** - Detailed workflow explanation
- **QUICKREF.md** - Quick reference and common commands
- **SETUP_SUMMARY.md** - Getting started guide

All are in the `.github/` directory for easy access.

---

## Environment

- **Python**: 3.12
- **Package Manager**: uv
- **Linter/Formatter**: Ruff
- **Test Runner**: pytest
- **Publisher**: twine → GitHub Packages
- **Release Artifacts**: wheel + sdist

---

**You're all set! 🚀**
