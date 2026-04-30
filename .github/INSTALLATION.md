# GitHub Packages Installation Guide

## Overview

The `zqnt-utils` package is automatically published to GitHub Packages on every push to `main` and can be installed in your projects using `pip` or `uv`.

## Prerequisites

You need a GitHub Personal Access Token (PAT) with `read:packages` permission.

1. Go to [GitHub Settings → Personal Access Tokens](https://github.com/settings/tokens)
2. Create a new token with:
   - Scopes: `read:packages`
   - Name: `ZQNT_PACKAGES_TOKEN` (or similar)
3. Copy the token (you won't see it again!)

## Installation with `uv`

This is the recommended method for modern Python projects.

### 1. Configure your `~/.config/uv/uv.toml` (or `~/.uv/uv.toml`):

```toml
[pip]
index-url = "https://pypi.org/simple"
extra-index-urls = [
    "https://ghcr.io/v2/@YOUR_GITHUB_USERNAME/simple"
]

[authentication]
credentials = [
    { url = "https://ghcr.io/v2", credential = "YOUR_GITHUB_TOKEN" }
]
```

### 2. Add to your project:

```bash
uv add zqnt-utils
```

## Installation with `pip`

### 1. Create `~/.pip/pip.conf` or `~/.config/pip/pip.conf`:

```ini
[global]
index-url = https://__token__:YOUR_GITHUB_TOKEN@ghcr.io/v2/@YOUR_GITHUB_USERNAME/simple/

[search]
index = https://__token__:YOUR_GITHUB_TOKEN@ghcr.io/v2/@YOUR_GITHUB_USERNAME/simple/
```

### 2. Install the package:

```bash
pip install zqnt-utils
```

Or with specific version:

```bash
pip install zqnt-utils==0.1.0
```

## Using in `requirements.txt`

Add to your `requirements.txt`:

```
zqnt-utils>=0.1.0
```

Then install:

```bash
pip install -r requirements.txt
```

## Using in `pyproject.toml` (uv)

Add to your `pyproject.toml`:

```toml
[project]
dependencies = [
    "zqnt-utils>=0.1.0",
]
```

Then sync:

```bash
uv sync
```

## Troubleshooting

### "401 Unauthorized"
- Check your token is correct
- Ensure your token has `read:packages` scope
- Verify you've replaced `YOUR_GITHUB_TOKEN` in config files

### "404 Not Found"
- Ensure you've replaced `@YOUR_GITHUB_USERNAME` with your actual GitHub username
- Check the package name is correct: `zqnt-utils` (not `zqnt_utils`)

### "Package not found"
- Wait a few minutes after push to main for the package to be published
- Check GitHub Actions workflow completed successfully

## Version Information

### Main Branch Releases
- **Official Releases**: Published directly with version from `pyproject.toml`
- **Format**: `X.Y.Z` (e.g., `0.1.0`)
- **Type**: Full releases marked as stable
- **GitHub Tags**: Automatic release tags created (e.g., `v0.1.0`)

### Pull Request Pre-releases
- **Pre-release Versions**: Published with PR number and commit SHA
- **Format**: `X.Y.Z.postN.devSHORTSHA` (e.g., `0.1.0.post42.dev3a1b2c`)
- **Type**: Pre-release/development versions
- **Auto-commented**: PR will be auto-commented with exact version to install

### Installing Pre-releases

To test a pre-release version from a PR:

```bash
uv add zqnt-utils==0.1.0.post42.dev3a1b2c --prerelease=allow
```

or with pip:

```bash
pip install --pre zqnt-utils==0.1.0.post42.dev3a1b2c
```

## More Information

- [GitHub Packages Documentation](https://docs.github.com/en/packages/working-with-a-python-registry)
- [uv Documentation](https://docs.astral.sh/uv/)
