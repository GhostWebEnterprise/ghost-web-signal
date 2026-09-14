<div align="center">

<img src="art/ghostly-icon-512.png" width="128" alt="Ghostly icon" />

# Ghostly

**Private by design. Secure by default. Open source.**

[![GitHub](https://img.shields.io/badge/GitHub-TempleEU%2Fghostweb.signal-181717?style=plastic&logo=github&logoColor=white)](https://github.com/TempleEU/ghostweb.signal)
[![Platform](https://img.shields.io/badge/Platform-Android-3DDC84?style=plastic&logo=android&logoColor=white)](https://github.com/TempleEU/ghostweb.signal)
[![Release](https://img.shields.io/github/v/release/TempleEU/ghostweb.signal?style=plastic&label=Release)](https://github.com/TempleEU/ghostweb.signal/releases)
[![License](https://img.shields.io/badge/License-AGPL_v3-blue?style=plastic)](https://github.com/TempleEU/ghostweb.signal/blob/GWSignal.main/LICENSE)

[![Test](https://img.shields.io/github/actions/workflow/status/TempleEU/ghostweb.signal/test.yml?branch=GWSignal.main&style=plastic&label=Test)](https://github.com/TempleEU/ghostweb.signal/actions/workflows/test.yml)
[![Lint](https://img.shields.io/github/actions/workflow/status/TempleEU/ghostweb.signal/super-linter.yml?branch=GWSignal.main&style=plastic&label=Super-Linter)](https://github.com/TempleEU/ghostweb.signal/actions/workflows/super-linter.yml)
[![Reproducible Build](https://img.shields.io/github/actions/workflow/status/TempleEU/ghostweb.signal/reprocheck.yml?style=plastic&label=Reproducible%20Build)](https://github.com/TempleEU/ghostweb.signal/actions/workflows/reprocheck.yml)
[![Website](https://img.shields.io/github/actions/workflow/status/TempleEU/ghostweb.signal/pages.yml?branch=GWSignal.main&style=plastic&label=Website)](https://templeeu.github.io/ghostweb.signal/)

</div>

---

**Ghostly** is an independent, privacy-focused messaging app for Android, built on the
**Signal/Molly** technology stack with its own branding, configuration, and privacy
enhancements. It provides end-to-end encrypted messaging and calling while connecting to
the standard Signal service network.

Website: **https://templeeu.github.io/ghostweb.signal/**

## Highlights

- End-to-end encrypted messaging, groups, voice, and video calls
- Encrypted media and file attachments, disappearing messages, reactions and replies
- Multi-device support (where supported by the underlying implementation)
- Encrypted local storage and secure application access
- Privacy-focused notifications, blocking, and reporting
- Ghostly branding and customization

## Privacy & security

Ghostly uses established, reviewed cryptographic protocols and libraries from the Signal
ecosystem (libsignal, RingRTC, SQLCipher) rather than custom cryptography. The project
prioritizes:

- Strong end-to-end encryption by default
- Protection of sensitive local data
- Reduced notification exposure
- Privacy-focused defaults and configuration
- Compatibility with the Signal/Molly architecture

## Download

Get signed APKs from the
[**Releases**](https://github.com/TempleEU/ghostweb.signal/releases) page.

Before installing an APK from any source, verify the release signature and published
checksums. See [Reproducible Builds](reproducible-builds/README.md) to compile the exact
source yourself and confirm the distributed APK matches byte-for-byte.

## Building

Requirements: JDK 21 and the Android SDK (see [BUILDING.md](BUILDING.md)).

```shell
# Assemble release APK + AAB
./gradlew -PCI=true :app:assembleRelease :app:bundleRelease

# Run unit tests
make test
```

Alternatively, use the Make targets (the same entrypoint the Docker builder uses):

```shell
make assemble   # release APK + AAB
```

Build flavors: `prodWebsiteRelease` (in-app updater), `prodStoreRelease` (no updater),
and `stagingWebsiteRelease` (Signal staging network).

## Platform status

| Platform | Status |
|----------|--------------------|
| Android  | **Available**      |
| iOS      | In development     |
| macOS    | In development     |
| Windows  | In development     |
| Linux    | In development     |

## Upstream & attribution

Ghostly is built from the Molly Android concept and uses
[johanw666/mollyim-android](https://github.com/johanw666/mollyim-android) as its upstream
reference (branch `main`). Molly and Signal remain the upstream projects:

- Signal Android — https://github.com/signalapp/Signal-Android
- Molly — https://github.com/mollyim/mollyim-android

Migration policy and the build gate are documented in [UPSTREAM.md](UPSTREAM.md).

## Contributing

Security-focused improvements, bug reports, and thoughtful contributions are welcome.

- [Issues](https://github.com/TempleEU/ghostweb.signal/issues)
- [Pull requests](https://github.com/TempleEU/ghostweb.signal/pulls)
- [Releases](https://github.com/TempleEU/ghostweb.signal/releases)

## License & legal

Ghostly is free software licensed under the **GNU Affero General Public License v3.0
only** (AGPL-3.0-only). See [LICENSE](LICENSE), [NOTICE](NOTICE), and
[LEGAL.md](LEGAL.md) for copyright, third-party notices, and export information.

## Disclaimer

Ghostly is an independently developed project and is not affiliated with, sponsored by,
or endorsed by Signal Messenger LLC or the Signal Foundation. It is provided as-is;
users should independently evaluate releases and security implications before relying on
the software for sensitive communications.
