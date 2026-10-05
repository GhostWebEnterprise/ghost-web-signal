# GhostWeb Signal 🛡️

<div align="center">

<img src="art/file_0000000000348246b3644cb184d2d66e.png" width="220" alt="GhostWeb Signal logo" />

### Privacy-focused secure messaging for Android

**Private by design · Secure by default · Open source**

> **Development status:** GhostWeb Signal is under active development. Features, builds, UI components, and releases may change and may not always work as expected. Review release notes and verify APK signatures before installation.

[![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=plastic&logo=android&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal)
[![Release](https://img.shields.io/github/v/release/GhostWebEnterprise/ghost-web-signal?style=plastic&label=Release)](https://github.com/GhostWebEnterprise/ghost-web-signal/releases)
[![APK](https://img.shields.io/badge/Download-APK-34A853?style=plastic&logo=android&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/releases)
[![Tests](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/test.yml?branch=GWSignal.main&style=plastic&label=Tests&logo=githubactions&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/test.yml)
[![Super-Linter](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/super-linter.yml?branch=GWSignal.main&style=plastic&label=Lint&logo=githubactions&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/super-linter.yml)
[![Reproducible Build](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/reprocheck.yml?branch=GWSignal.main&style=plastic&label=Reproducible%20Build&logo=githubactions&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/reprocheck.yml)
[![AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0--only-blue?style=plastic)](LICENSE)
[![Website](https://img.shields.io/badge/Website-ghostweb.bot.cd-0B57D0?style=plastic&logo=googlechrome&logoColor=white)](https://ghostweb.bot.cd)\n[![Need support?](https://img.shields.io/badge/Need%20support%3F-Contact%3A%20support--ghostweb%40proton.me-6D4AFF?style=plastic&logo=protonmail&logoColor=white)](mailto:support-ghostweb@proton.me)

</div>

---

## About GhostWeb Signal

**GhostWeb Signal** is an independent, open-source, privacy-focused secure messenger for Android developed as part of the **GhostWeb Enterprise** ecosystem.

The project builds on the Signal/Molly Android technology stack while introducing GhostWeb branding, interface work, privacy-focused configuration, release automation, and project-specific enhancements. It is designed to preserve compatibility with the Signal ecosystem while avoiding custom cryptography in favor of established upstream security components.

GhostWeb Signal is an independent project and is **not affiliated with, sponsored by, or endorsed by Signal Messenger LLC or the Signal Foundation**.

## Project status

🚧 **Under active development**

GhostWeb Enterprise is still developing GhostWeb Signal. Development builds and individual features may be incomplete, experimental, unstable, or subject to change. A published build should not automatically be interpreted as production-ready.

Current focus includes:

- GhostWeb-branded Android experience and application identity
- Full GhostWeb UI migration across conversations, calls, groups, settings, privacy, security, and appearance
- Privacy and application-lock experience, including optional biometric protection where supported
- Android build, test, lint, signing, and release automation
- Signed APK verification before GitHub Release publication
- Upstream synchronization and compatibility maintenance

## Core capabilities

The Android codebase builds on established Signal/Molly functionality, including:

- End-to-end encrypted private messaging
- Encrypted group conversations
- Voice and video calling
- Media and file attachments
- Disappearing messages
- Message reactions and replies
- Privacy-oriented notification and application controls
- Secure local application data
- GhostWeb-specific branding and interface customization

Exact functionality can vary by development branch and release.

## Security model

GhostWeb Signal does **not** aim to invent its own cryptography. The project builds on established components from the Signal ecosystem, including **libsignal**, **RingRTC**, and encrypted local-storage technologies used by its upstream codebase.

Release automation is designed to fail closed for signed production APKs: release builds must use the configured Android signing credentials, unsigned release artifacts must not be published, and APK signatures should be verified before a release asset is distributed.

Users should independently review release information and verify artifacts before relying on development builds for sensitive communications.

## Download

Android builds are distributed through [**GitHub Releases**](https://github.com/GhostWebEnterprise/ghost-web-signal/releases).

For release builds:

1. Download the APK from the matching GitHub Release.
2. Review the release notes and development status.
3. Verify the APK signature and any published checksum.
4. Avoid installing APK files redistributed by unknown third parties.

## Build from source

See [BUILDING.md](BUILDING.md) for the repository's complete build requirements.

Typical requirements include **JDK 21** and the Android SDK.

```shell
./gradlew -PCI=true :app:assembleRelease :app:bundleRelease
make test
```

Available build variants can include `prodWebsiteRelease`, `prodStoreRelease`, and `stagingWebsiteRelease`. Check the current Gradle configuration before building because the project is actively evolving.

## Platform roadmap

| Platform | Status |
| --- | --- |
| Android | **Active development / primary platform** |
| iOS | Planned / in development |
| macOS | Planned / in development |
| Windows | Planned / in development |
| Linux | Planned / in development |

Only Android should currently be treated as the primary GhostWeb Signal implementation in this repository.

## GhostWeb ecosystem

| Project | Purpose | Status |
| --- | --- | --- |
| **GhostWeb Signal** | Secure private messaging and calling | **Active development** |
| **GhostWeb VPN** | Network privacy and protection | **Under development · not release-ready** |
| **GhostWeb AI** | AI, agents, and software-building tools | **Under development · not release-ready** |
| **GhostOS** | Privacy-focused Android operating system | **Under development · not release-ready** |

Project hub: **https://ghostweb.bot.cd**

### Related repositories

- [GhostWeb VPN](https://github.com/GhostWebEnterprise/ghost-web-vpn)
- [GhostWeb AI](https://github.com/GhostWebEnterprise/ghost-web-ai)
- [GhostOS](https://github.com/GhostWebEnterprise/GhostOS)

## Upstream & attribution

GhostWeb Signal builds on work from the Signal and Molly open-source ecosystems. The project uses **johanw666/mollyim-android** as an upstream reference while maintaining GhostWeb-specific changes and branding.

Upstream projects retain their respective names, trademarks, copyrights, and licenses.

## License

GhostWeb Signal is distributed under the **GNU Affero General Public License v3.0 only (AGPL-3.0-only)**.

See [LICENSE](LICENSE), [NOTICE](NOTICE), and [LEGAL.md](LEGAL.md) for applicable licensing, attribution, and legal information.

## Support

For GhostWeb project support and development-related contact:

**support-ghostweb@proton.me**

Website: **https://ghostweb.bot.cd**

---

<div align="center">

**GhostWeb Enterprise · Privacy-focused software under active development**

</div>
