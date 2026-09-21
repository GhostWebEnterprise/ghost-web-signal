# GhostWeb

<div align="center">

<img src="art/ghostweb-icon-512.png" width="128" alt="GhostWeb icon" />

## GhostWeb Signal 🛡️

**Private by design. Secure by default. Open source.**

[![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=plastic&logo=android&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal)
[![Signal compatible](https://img.shields.io/badge/Network-Signal-3A76F0?style=plastic&logo=signal&logoColor=white)](https://signal.org/)
[![Release](https://img.shields.io/github/v/release/GhostWebEnterprise/ghost-web-signal?style=plastic&label=Release)](https://github.com/GhostWebEnterprise/ghost-web-signal/releases)
[![APK](https://img.shields.io/badge/Download-APK-34A853?style=plastic&logo=android&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/releases)
[![Test](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/test.yml?branch=GWSignal.main&style=plastic&label=Tests&logo=githubactions&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/test.yml)
[![Super-Linter](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/super-linter.yml?branch=GWSignal.main&style=plastic&label=Lint&logo=githubactions&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/super-linter.yml)
[![Reproducible Build](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/reprocheck.yml?branch=GWSignal.main&style=plastic&label=Reproducible%20Build&logo=githubactions&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/reprocheck.yml)
[![AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0--only-blue?style=plastic)](https://github.com/GhostWebEnterprise/ghost-web-signal/blob/GWSignal.main/LICENSE)
[![Signal Protocol](https://img.shields.io/badge/E2EE-Signal%20Protocol-3A76F0?style=plastic&logo=signal&logoColor=white)](https://signal.org/docs/)
[![Website](https://img.shields.io/badge/GhostWeb-ghostweb.bot.cd-111827?style=plastic&logo=googlechrome&logoColor=white)](https://ghostweb.bot.cd)

</div>

---

## **GhostWeb Ecosystem**

GhostWeb Signal is part of the **GhostWeb Enterprise** privacy ecosystem.

| Project | Purpose | Current status |
| --- | --- | --- |
| **GhostWeb Signal** | Private Android messaging and calling | **Available / active development** |
| **GhostWeb VPN** | Browser, Android and desktop network protection | **Under active development** |
| **GhostWeb AI** | Multi-model AI, agents and software delivery | **Under active development** |
| **GhostOS** | Privacy-focused custom Android ROM | **Under development · not release-ready** |

**Project hub:** [ghostweb.bot.cd](https://ghostweb.bot.cd)

## **GhostWeb Signal**

**GhostWeb Signal** is an independent, privacy-focused messaging app for Android, built on the **Signal/Molly** technology stack with its own branding, configuration, and privacy enhancements. It provides end-to-end encrypted messaging and calling while connecting to the standard Signal service network.

### Highlights

- End-to-end encrypted messaging, groups, voice, and video calls
- Encrypted media and file attachments
- Disappearing messages, reactions, and replies
- Encrypted local storage and secure application access
- Privacy-focused notifications, blocking, and reporting
- GhostWeb branding and customization

## Privacy & security

GhostWeb Signal uses established cryptographic protocols and libraries from the Signal ecosystem, including libsignal, RingRTC, and SQLCipher, rather than custom cryptography.

## Download GhostWeb Signal

Get signed Android APKs from the [**Releases**](https://github.com/GhostWebEnterprise/ghost-web-signal/releases) page. Before installing an APK, verify the release signature and published checksums.

## Building GhostWeb Signal

Requirements: JDK 21 and the Android SDK (see [BUILDING.md](BUILDING.md)).

```shell
./gradlew -PCI=true :app:assembleRelease :app:bundleRelease
make test
```

Build flavors include `prodWebsiteRelease`, `prodStoreRelease`, and `stagingWebsiteRelease`.

## Platform status

| Platform | Status |
| --- | --- |
| Android | **Available** |
| iOS | In development |
| macOS | In development |
| Windows | In development |
| Linux | In development |

## Related GhostWeb projects

- [GhostWeb VPN](https://github.com/GhostWebEnterprise/ghost-web-vpn)
- [GhostWeb AI](https://github.com/GhostWebEnterprise/ghost-web-ai)
- [GhostOS](https://github.com/GhostWebEnterprise/GhostOS)
- [GhostWeb project hub](https://ghostweb.bot.cd)

## Upstream & attribution

GhostWeb is built from the Molly Android concept and uses [johanw666/mollyim-android](https://github.com/johanw666/mollyim-android) as its upstream reference. Molly and Signal remain upstream projects.

## License & legal

GhostWeb is free software licensed under the **GNU Affero General Public License v3.0 only** (AGPL-3.0-only). See [LICENSE](LICENSE), [NOTICE](NOTICE), and [LEGAL.md](LEGAL.md).

## Disclaimer

GhostWeb projects are independently developed and are not affiliated with, sponsored by, or endorsed by Signal Messenger LLC or the Signal Foundation.
