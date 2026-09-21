# GhostWeb

<div align="center">

<img src="art/ghostweb-icon-512.png" width="128" alt="GhostWeb icon" />

## GhostWeb **(S)** ### ©

**Private by design. Secure by default. Open source.**

[![GitHub](https://img.shields.io/badge/GitHub-GhostWebEnterprise-181717?style=plastic&logo=github&logoColor=white)](https://github.com/GhostWebEnterprise)
[![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=plastic&logo=android&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal)
[![Release](https://img.shields.io/github/v/release/GhostWebEnterprise/ghost-web-signal?style=plastic&label=GhostWeb)](https://github.com/GhostWebEnterprise/ghost-web-signal/releases)
[![License](https://img.shields.io/badge/License-AGPL_v3-blue?style=plastic)](https://github.com/GhostWebEnterprise/ghost-web-signal/blob/GWSignal.main/LICENSE)
[![Test](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/test.yml?branch=GWSignal.main&style=plastic&label=Test)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/test.yml)
[![Website](https://img.shields.io/badge/Website-ghostweb.bot.cd-0b57d0?style=plastic&logo=googlechrome&logoColor=white)](https://ghostweb.bot.cd)
[![Release](https://img.shields.io/github/v/release/GhostWebEnterprise/ghost-web-signal?style=plastic&label=Release)](https://github.com/GhostWebEnterprise/ghost-web-signal/releases)
[![Dependabot](https://img.shields.io/github/issues/GhostWebEnterprise/ghost-web-signal/dependabot?style=plastic&label=Dependabot)](https://github.com/GhostWebEnterprise/ghost-web-signal/network/updates)
[![Lint](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/super-linter.yml?branch=GWSignal.main&style=plastic&label=Super-Linter)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/super-linter.yml)
[![Reproducible Build](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghost-web-signal/reprocheck.yml?style=plastic&label=Reproducible%20Build)](https://github.com/GhostWebEnterprise/ghost-web-signal/actions/workflows/reprocheck.yml)

</div>

---

## **GhostWeb Eco System**

**GhostWeb** is an independent open-source software ecosystem focused on privacy, secure communication, network protection, AI tooling, and privacy-focused Android development.

**Official project hub:** [ghostweb.bot.cd](https://ghostweb.bot.cd)

| Project | Purpose | Status |
| --- | --- | --- |
| **GhostWeb Signal** | Privacy-focused Android messaging and calling | **Available** |
| **GhostWeb VPN** | Privacy-focused browser and network protection | **Available** |
| **GhostWeb AI** | Privacy-focused AI client and tooling | **Available** |
| **GhostOS** | Privacy-focused custom Android ROM | **In development** |

## **GhostWeb Signal**

**GhostWeb: Ⓢignl** is an independent, privacy-focused messaging app for Android, built on the **Signal/Molly** technology stack with its own branding, configuration, and privacy enhancements. It provides end-to-end encrypted messaging and calling while connecting to the standard Signal service network.

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
