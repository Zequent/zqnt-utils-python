# Quick Reference

## File Structure

```
.github/
├── workflows/
│   ├── pr.yml              # Pull request workflow
│   └── main.yml            # Main branch release workflow
├── dependabot.yml          # Auto dependency updates
├── WORKFLOWS.md            # Detailed workflow documentation
└── INSTALLATION.md         # Installation guide for developers
```

## Workflow Comparison

| Feature | PR Workflow | Main Workflow |
|---------|-----------|--------------|
| **Trigger** | PR to main | Push to main |
| **Version** | `X.Y.Z.postN.devSHA` | `X.Y.Z` |
| **Publish** | Pre-release | Stable release |
| **GitHub Release** | ❌ No | ✅ Yes |
| **Auto-comment** | ✅ Yes | ❌ No |
| **Tag** | ❌ No | ✅ Yes `vX.Y.Z` |

## Checklist for First Setup

- [ ] Push workflows to GitHub
- [ ] Create GitHub Personal Access Token with `read:packages` scope
- [ ] Developers configure `~/.config/uv/uv.toml` or `~/.pip/pip.conf`
- [ ] Test with a PR to verify pre-release publishing works
- [ ] Update `pyproject.toml` version for first official release
- [ ] Verify GitHub Release is created after merge to main

## Common Commands

### Test Pre-release from PR
```bash
uv add zqnt-utils==0.1.0.post1.devABC123 --prerelease=allow
```

### Install Latest Stable
```bash
uv add zqnt-utils
```

### Install Specific Version
```bash
uv add zqnt-utils==0.1.0
```

### Check Available Versions
```bash
uv pip index versions zqnt-utils
```

## Release Process

1. **Update version** in `pyproject.toml`
2. **Commit & push** to main (or merge PR)
3. **Wait** for main workflow to complete (~2 min)
4. **Check** GitHub Releases page for new release
5. **Share** version with team
6. **Developers install** with `uv add zqnt-utils==X.Y.Z`

## Pre-release Testing Process

1. **Create PR** with changes
2. **Wait** for pr.yml workflow (~2 min)
3. **GitHub comments** with pre-release version
4. **Copy version** from comment
5. **Install** with `uv add zqnt-utils==VERSION --prerelease=allow`
6. **Test** the changes
7. **Provide feedback** or approve PR

## Troubleshooting Quick Links

| Issue | Solution |
|-------|----------|
| 401 Unauthorized | Check GitHub token scopes and config |
| 404 Not Found | Check username and package name in config |
| Package not in index | Wait 2-3 min after workflow completes |
| Pre-release install fails | Add `--prerelease=allow` flag to uv |
| No GitHub Release created | Ensure version format is valid in `pyproject.toml` |
