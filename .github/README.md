# 🚀 GitHub Workflows - Complete Setup

## Overview

Your `zqnt-utils` Python package now has a professional, streamlined CI/CD pipeline matching your existing library patterns.

---

## 📁 What Was Created

```
.github/
├── workflows/
│   ├── main.yml              # Main branch: lint, test, build, publish & release
│   └── pr.yml                # Pull requests: lint, test, build, publish preview
├── dependabot.yml            # Auto dependency updates (weekly)
│
├── INSTALLATION.md           # For developers: how to install the package
├── QUICKREF.md               # Quick command reference & troubleshooting
├── WORKFLOWS.md              # Detailed workflow documentation
├── SETUP_SUMMARY.md          # Getting started guide
└── UPDATE_SUMMARY.md         # This update's changes
```

---

## 🎯 Workflow Patterns

### **Pull Request Workflow** (`pr.yml`)

```
PR to main
    ↓
Single CI job runs:
├─ Lint (ruff check)
├─ Format check (ruff format)
├─ Tests (pytest)
├─ Build package
├─ Version: 0.1.0.post42.dev3a1b2c
├─ Publish pre-release
└─ Comment PR with version
```

### **Main Release Workflow** (`main.yml`)

```
Push to main
    ↓
Single CI job runs:
├─ Lint (ruff check)
├─ Format check (ruff format)
├─ Tests (pytest)
├─ Build package
├─ Version: 0.1.0 (from pyproject.toml)
├─ Publish release
├─ Create GitHub Release
└─ Create tag v0.1.0
```

---

## 🔄 Workflow Comparison

| Feature | PR Workflow | Main Workflow |
|---------|-----------|--------------|
| **Trigger** | PR to main | Push to main |
| **Job Type** | Single CI job | Single CI job |
| **Version** | `X.Y.Z.postN.devSHA` | `X.Y.Z` |
| **Publish** | Pre-release | Stable release |
| **GitHub Release** | ❌ | ✅ |
| **Tag Created** | ❌ | ✅ (e.g., v0.1.0) |
| **PR Comment** | ✅ | N/A |

---

## 📦 Publishing Flow

```
Pull Request
  ├─ Tests pass
  ├─ Build succeeds
  ├─ Publish to GitHub Packages (pre-release)
  └─ Comment with version for testing

        ↓ (approved and merged)

Main Branch Push
  ├─ Tests pass
  ├─ Build succeeds
  ├─ Publish to GitHub Packages (stable)
  ├─ Create GitHub Release
  └─ Create Git tag
```

---

## 🛠️ Tech Stack

- **Python**: 3.12
- **Package Manager**: `uv`
- **Linting**: Ruff
- **Testing**: pytest
- **Building**: `uv build` (creates wheel + sdist)
- **Publishing**: twine → GitHub Packages
- **Releases**: GitHub Releases API

---

## ⚡ Quick Start for Your Team

### 1. Install Pre-release from PR
```bash
# Copy version from PR comment, e.g., 0.1.0.post42.dev3a1b2c
uv add zqnt-utils==0.1.0.post42.dev3a1b2c --prerelease=allow
```

### 2. Install Stable Release
```bash
uv add zqnt-utils==0.1.0
```

### 3. Create Release
```bash
# Update version in pyproject.toml
version = "0.2.0"

# Commit & push to main
git add pyproject.toml
git commit -m "bump: version 0.1.0 → 0.2.0"
git push origin main

# Workflow automatically publishes and creates release
```

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| **INSTALLATION.md** | Setup guide for developers (GitHub token, config, troubleshooting) |
| **QUICKREF.md** | Commands, processes, and quick fixes |
| **WORKFLOWS.md** | Complete workflow documentation |
| **SETUP_SUMMARY.md** | Getting started guide |
| **UPDATE_SUMMARY.md** | What changed in this update |

---

## ✅ Key Features

✅ **Single consolidated CI jobs** - All steps in one sequential flow  
✅ **Pre-release versioning** - PEP 440 compliant  
✅ **Automatic GitHub Releases** - Tags created automatically  
✅ **Auto-commented PRs** - Shows version for easy testing  
✅ **GitHub Packages** - Publish wheel + sdist automatically  
✅ **Quality gates** - Lint & tests before publishing  
✅ **Dependency management** - Dependabot keeps deps updated  

---

## 🎬 Getting Started

### Step 1: Commit & Push
```bash
git add .github/
git commit -m "feat: add CI/CD workflows with pre-release support"
git push
```

### Step 2: Verify Workflows
Visit: `https://github.com/YOUR_ORG/zqnt-utils-python/actions`

### Step 3: Test with PR
1. Create a test branch
2. Make a change
3. Create PR to `main`
4. Watch `pr.yml` run
5. GitHub comments with pre-release version
6. Test by installing pre-release

### Step 4: Test with Main
1. Merge PR
2. Watch `main.yml` run
3. Check GitHub Releases page
4. Tag `v0.1.0` created automatically

---

## 🔑 Important Notes

### For Workflows (Automatic)
- Uses `${{ secrets.GITHUB_TOKEN }}` automatically
- GitHub creates this token with `packages:write` permission
- No setup needed for workflows!

### For Developers Installing (Manual)
- They need GitHub PAT with `read:packages` scope
- Configure once in `~/.config/uv/uv.toml`
- See `INSTALLATION.md` for full instructions

---

## 🚀 Example Release Process

```
1. Feature branch: git checkout -b feature/new-thing
2. Make changes
3. Create PR
4. pr.yml runs → publishes 0.1.0.post1.dev3a1b2c
5. Team tests pre-release
6. Approve & merge PR
7. main.yml runs → publishes 0.1.0 + creates release
8. Announce version to team
9. Users install with: uv add zqnt-utils==0.1.0
```

---

## 📖 References

- [GitHub Packages Python Registry](https://docs.github.com/en/packages/working-with-a-python-registry)
- [PEP 440 - Version Identification](https://www.python.org/dev/peps/pep-0440/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Ruff Linter & Formatter](https://docs.astral.sh/ruff/)

---

## 💡 Tips

- **Test PRs first** - Pre-releases let your team test changes before merging
- **Update version in pyproject.toml** before pushing to main to trigger a new release
- **Check GitHub Actions logs** if something goes wrong
- **Share documentation** with your team from `.github/` directory

---

**Ready to release! 🎉**

Start with a test PR to verify everything works, then you're all set!
