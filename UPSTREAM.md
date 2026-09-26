# GhostWeb upstream

GhostWeb Android is built from the Molly Android concept and uses `johanw666/mollyim-android` as the upstream reference source.

Upstream: https://github.com/johanw666/mollyim-android
Upstream branch: `main`

## Migration policy

- Preserve upstream copyright, license, attribution, and third-party notices.
- GhostWeb branding and original changes remain separate from upstream attribution.
- Do not imply affiliation with Signal, Molly, or their maintainers.
- Security-sensitive changes must be verified against upstream before release.

## Build gate

Migration is not considered complete until the repository builds successfully, tests pass, and the resulting APK is verified.

## UI gate

The Photon/GhostWeb UI migration additionally requires the UI gate described in
[docs/ui-gate.md](docs/ui-gate.md). A green build alone does not authorize a new
release: the release pipeline blocks publishing until the UI gate for the
current gate version (`photon-1`) has passed on the exact APK being released.
