<div align="center">

<img src="art/ghostly-icon-512.png" width="128" alt="Ghostly icon" />

# GhostWeb

**Private by design. Secure by default. Open source.**

[![GitHub](https://img.shields.io/badge/GitHub-GhostWebEnterprise-181717?style=plastic&logo=github&logoColor=white)](https://github.com/GhostWebEnterprise)
[![Android](https://img.shields.io/badge/Platform-Android-3DDC84?style=plastic&logo=android&logoColor=white)](https://github.com/GhostWebEnterprise/ghostweb.signal)
[![Release](https://img.shields.io/github/v/release/GhostWebEnterprise/ghostweb.signal?style=plastic&label=Ghostly%20Release)](https://github.com/GhostWebEnterprise/ghostweb.signal/releases)
[![License](https://img.shields.io/badge/License-AGPL_v3-blue?style=plastic)](https://github.com/GhostWebEnterprise/ghostweb.signal/blob/GWSignal.main/LICENSE)

[![Test](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/test.yml?branch=GWSignal.main&style=plastic&label=Test)](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/test.yml)
[![Lint](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/super-linter.yml?branch=GWSignal.main&style=plastic&label=Super-Linter)](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/super-linter.yml)
[![Reproducible Build](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/reprocheck.yml?style=plastic&label=Reproducible%20Build)](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/reprocheck.yml)
[![Website](https://img.shields.io/github/actions/workflow/status/GhostWebEnterprise/ghostweb.signal/pages.yml?branch=GWSignal.main&style=plastic&label=Website)](https://ghostwebenterprise.github.io/ghostweb.signal/)

</div>

---

## GhostWeb ecosystem

**GhostWeb** is an independent open-source software ecosystem focused on privacy, secure communication, network protection, and AI tooling.

The central project website brings the ecosystem together in one place so users can discover releases, downloads, source code, and documentation.

**Project hub:** https://ghostwebenterprise.github.io/ghostweb.signal/

| Project | Purpose | Status |
|---|---|---|
| **Ghostly / GhostWeb Signal** | Privacy-focused Android messaging and calling | **Available** |
| **GhostWeb VPN** | Privacy-focused browser/network protection | **Available** |
| **GhostWeb AI** | Privacy-focused AI client and tooling | **Available** |

### Downloads

All GhostWeb projects are linked from the central project hub:

- **GhostWeb Signal / Ghostly** — Android messaging client and releases
- **GhostWeb VPN** — browser VPN/proxy protection project and releases
- **GhostWeb AI** — AI client, agents, and releases

---

## Ghostly — Signal client

**Ghostly** is an independent, privacy-focused messaging app for Android, built on the **Signal/Molly** technology stack with its own branding, configuration, and privacy enhancements. It provides end-to-end encrypted messaging and calling while connecting to the standard Signal service network.

### Highlights

- End-to-end encrypted messaging, groups, voice, and video calls
- Encrypted media and file attachments
- Disappearing messages, reactions, and replies
- Multi-device support where supported by the underlying implementation
- Encrypted local storage and secure application access
- Privacy-focused notifications, blocking, and reporting
- Ghostly branding and customization

## Privacy & security

Ghostly uses established cryptographic protocols and libraries from the Signal ecosystem, including libsignal, RingRTC, and SQLCipher, rather than custom cryptography.

The project prioritizes:

- Strong end-to-end encryption by default
- Protection of sensitive local data
- Reduced notification exposure
- Privacy-focused defaults and configuration
- Compatibility with the Signal/Molly architecture

## Download Ghostly

Get signed Android APKs from the [**Releases**](https://github.com/GhostWebEnterprise/ghostweb.signal/releases) page.

Before installing an APK from any source, verify the release signature and published checksums. See [Reproducible Builds](reproducible-builds/README.md) to compile the source yourself and verify the distributed APK.

## Building Ghostly

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

## GhostWeb projects

### GhostWeb VPN

Privacy-focused browser/network protection with proxy and traffic-protection features.

Repository: https://github.com/GhostWebEnterprise/ghost-web-vpn

### GhostWeb AI

Privacy-focused AI client and tooling for working with AI models and agent workflows.

Repository: https://github.com/GhostWebEnterprise/ghost-web-ai

### Central website

Use the GhostWeb website as the main download and project-discovery hub:

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

For the other GhostWeb projects, use their respective repositories linked above.

## License & legal

Ghostly is free software licensed under the **GNU Affero General Public License v3.0 only** (AGPL-3.0-only). See [LICENSE](LICENSE), [NOTICE](NOTICE), and [LEGAL.md](LEGAL.md) for copyright, third-party notices, and export information.

## Disclaimer

GhostWeb projects are independently developed and are not affiliated with, sponsored by, or endorsed by Signal Messenger LLC or the Signal Foundation. They are provided as-is; users should independently evaluate releases, security implications, and compatibility before relying on the software for sensitive communications.
