<div align="center">

<img src="art/ghostly-icon-512.png" width="128" alt="GhostWeb icon" />

# GhostWeb

**Private by design. Secure by default. Open source.**

[![GitHub](https://img.shields.io/badge/GitHub-GhostWebEnterprise-181717?style=plastic&logo=github&logoColor=white)](https://github.com/GhostWebEnterprise)
[![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=plastic&logo=android&logoColor=white)](https://github.com/GhostWebEnterprise/ghostweb.signal)
[![Release](https://img.shields.io/github/v/release/GhostWebEnterprise/ghostweb.signal?style=plastic&label=GhostWeb)](https://github.com/GhostWebEnterprise/ghostweb.signal/releases)
[![License](https://img.shields.io/badge/License-AGPL_v3-blue?style=plastic)](https://github.com/GhostWebEnterprise/ghostweb.signal/blob/GWSignal.main/LICENSE)

[![Test](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/test.yml?branch=GWSignal.main&style=plastic&label=Test)](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/test.yml)
[![Lint](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/super-linter.yml?branch=GWSignal.main&style=plastic&label=Super-Linter)](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/super-linter.yml)
[![Reproducible Build](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/reprocheck.yml?style=plastic&label=Reproducible%20Build)](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/reprocheck.yml)
[![Website](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/pages.yml?branch=GWSignal.main&style=plastic&label=Website)](https://ghostwebenterprise.github.io/ghostweb.signal/)

</div>

---

## GhostWeb ecosystem

**GhostWeb** is an independent open-source software ecosystem focused on privacy, secure communication, network protection, and AI tooling.

The central website is the project hub for discovering the GhostWeb applications, source code, releases, downloads, and documentation.

**Project hub:** https://ghostwebenterprise.github.io/ghostweb.signal/

| Project | Purpose | Status |
|---|---|---|
| **GhostWeb Signal** | Privacy-focused Android messaging and calling | **Available** |
| **GhostWeb VPN** | Privacy-focused browser and network protection | **Available** |
| **GhostWeb AI** | Privacy-focused AI client and tooling | **Available** |

### Downloads

All GhostWeb projects are available through the central website:

- **GhostWeb Signal / Ghostly** — Android messaging client and releases
- **GhostWeb VPN** — browser VPN/proxy protection project and releases
- **GhostWeb AI** — AI client, agents, and releases

---

## GhostWeb: Signal 

**GhostWeb: Signal** is an independent, privacy-focused messaging app for Android, built on the **Signal/Molly** technology stack with its own branding, configuration, and privacy enhancements. It provides end-to-end encrypted messaging and calling while connecting to the standard Signal service network.

### Highlights

- End-to-end encrypted messaging, groups, voice, and video calls
- Encrypted media and file attachments
- Disappearing messages, reactions, and replies
- Multi-device support where supported by the underlying implementation
- Encrypted local storage and secure application access
- Privacy-focused notifications, blocking, and reporting
- Ghostly branding and customization

## Privacy & security

GhostWeb: Signal uses established cryptographic protocols and libraries from the Signal ecosystem, including libsignal, RingRTC, and SQLCipher, rather than custom cryptography.

The project prioritizes:

- Strong end-to-end encryption by default
- Protection of sensitive local data
- Reduced notification exposure
- Privacy-focused defaults and configuration
- Compatibility with the Signal/Molly architecture

## Download GhostWeb: Signal 

Get signed Android APKs from the [**Releases**](https://github.com/GhostWebEnterprise/ghostweb.signal/releases) page.

Before installing an APK from any source, verify the release signature and published checksums. See [Reproducible Builds](reproducible-builds/README.md) to compile the source yourself and verify the distributed APK.

## Building GhostWeb: Signal

Requirements: JDK 21 and the Android SDK (see [BUILDING.md](BUILDING.md)).

```shell
# Assemble release APK + AAB
./gradlew -PCI=true :app:assembleRelease :app:bundleRelease

# Run unit tests
make test
```

Alternatively:

```shell
make assemble   # release APK + AAB
```

Build flavors include `prodWebsiteRelease` (in-app updater), `prodStoreRelease` (no updater), and `stagingWebsiteRelease` (Signal staging network).

## Platform status

| Platform | Status |
|---|---|
| Android | **Available** |
| iOS | In development |
| macOS | In development |
| Windows | In development |
| Linux | In development |

---

## GhostWeb VPN (still in testing phase)

**GhostWeb VPN** is the GhostWeb privacy/network-protection project, providing browser-based proxy and traffic-protection functionality.

**Repository:** https://github.com/GhostWebEnterprise/ghost-web-vpn

**Releases:** https://github.com/GhostWebEnterprise/ghost-web-vpn/releases

## GhostWeb AI (still in testing phase)

**GhostWeb AI** is the GhostWeb AI client and tooling project for AI models, agents, and related workflows.

**Repository:** https://github.com/GhostWebEnterprise/ghost-web-ai

**Releases:** https://github.com/GhostWebEnterprise/ghost-web-ai/releases

## Central GhostWeb website

The GhostWeb website brings the projects together in one place for downloads and project discovery:

**https://ghostwebenterprise.github.io/ghostweb.signal/**

---

## Upstream & attribution

Ghostly is built from the Molly Android concept and uses [johanw666/mollyim-android](https://github.com/johanw666/mollyim-android) as its upstream reference (branch `main`). Molly and Signal remain the upstream projects.

- Signal Android — https://github.com/signalapp/Signal-Android
- Molly — https://github.com/mollyim/mollyim-android

Migration policy and the build gate are documented in [UPSTREAM.md](UPSTREAM.md).

## Contributing

Security-focused improvements, bug reports, documentation improvements, and thoughtful contributions are welcome.

- [Issues](https://github.com/GhostWebEnterprise/ghostweb.signal/issues)
- [Pull requests](https://github.com/GhostWebEnterprise/ghostweb.signal/pulls)
- [Releases](https://github.com/GhostWebEnterprise/ghostweb.signal/releases)

For GhostWeb VPN and GhostWeb AI, use the respective repositories linked above.

## License & legal

Ghostly is free software licensed under the **GNU Affero General Public License v3.0 only** (AGPL-3.0-only). See [LICENSE](LICENSE), [NOTICE](NOTICE), and [LEGAL.md](LEGAL.md) for copyright, third-party notices, and export information.

## Disclaimer

GhostWeb projects are independently developed and are not affiliated with, sponsored by, or endorsed by Signal Messenger LLC or the Signal Foundation. They are provided as-is; users should independently evaluate releases, security implications, and compatibility before relying on the software for sensitive communications.
