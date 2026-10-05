# GhostWeb Signal Security Policy

<div align="center">

[![Security Policy](https://img.shields.io/badge/Security-Policy-2ea44f?style=plastic&logo=github&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/security/policy)
[![Security Advisories](https://img.shields.io/badge/Security-Advisories-red?style=plastic&logo=github&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/security/advisories)
[![CodeQL](https://img.shields.io/badge/Security-CodeQL-blue?style=plastic&logo=githubactions&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/security/code-scanning)
[![Dependencies](https://img.shields.io/badge/Security-Dependencies-blue?style=plastic&logo=dependabot&logoColor=white)](https://github.com/GhostWebEnterprise/ghost-web-signal/security/dependabot)
[![Need support?](https://img.shields.io/badge/Need%20support%3F-Contact%3A%20support--ghostweb%40proton.me-6D4AFF?style=plastic&logo=protonmail&logoColor=white)](mailto:support-ghostweb@proton.me)

**Private by design · Secure by default · Responsible disclosure**

</div>

> **Development notice:** GhostWeb Signal is under active development. Development builds, UI components, integrations and release infrastructure may change. A successful build or published development release must not be interpreted as a guarantee that the software is free from security vulnerabilities.

## Scope

This policy covers security issues in **GhostWeb-specific code, configuration, build/release infrastructure and distributed GhostWeb Signal artifacts** maintained in this repository.

Examples include:

- vulnerabilities that could expose message content, attachments, keys, tokens or other sensitive data;
- authentication, authorization, account or session bypasses;
- weaknesses in application lock, biometric/PIN handling or privacy controls;
- insecure local storage or unintended data leakage;
- notification, clipboard, logging or backup behavior that exposes sensitive information;
- vulnerabilities introduced by GhostWeb-specific UI or application changes;
- network-security or certificate-validation weaknesses introduced by this project;
- malicious or unsafe deep-link, intent, URI or attachment handling;
- build, signing, update or release-pipeline weaknesses that could permit unauthorized artifacts;
- exposed credentials, signing material or other secrets belonging to GhostWeb;
- dependency or supply-chain vulnerabilities that materially affect GhostWeb Signal.

Issues that exist exclusively in an upstream project should normally also be reported to the relevant upstream maintainer. If you are unsure whether a vulnerability is GhostWeb-specific or upstream, report it privately to GhostWeb first and we will triage it.

## Supported versions

GhostWeb Signal is currently an actively developed project rather than a project with multiple long-term supported release trains.

| Version / channel | Security support |
| --- | --- |
| Latest GhostWeb Signal release | ✅ Security reports accepted |
| Current `GWSignal.main` development branch | ⚠️ Best-effort during active development |
| Older releases superseded by a newer release | ❌ Not guaranteed |
| Unofficial, modified or third-party builds | ❌ Not supported by GhostWeb Enterprise |

Users should update to the latest verified GhostWeb Signal release when security fixes are published.

## Reporting a vulnerability

**Do not disclose suspected vulnerabilities in a public GitHub issue, discussion, pull request, social-media post or other public channel before coordinated disclosure.**

Preferred reporting path:

1. Use the repository's **GitHub Security Advisories / private vulnerability reporting** interface when the **Report a vulnerability** option is available:
   https://github.com/GhostWebEnterprise/ghost-web-signal/security/advisories
2. If private vulnerability reporting is unavailable, contact **support-ghostweb@proton.me** and clearly mark the message as a **security vulnerability report**.
3. Do not send private keys, passwords, authentication tokens, personal message content or other unnecessary sensitive user data.

A useful report should contain, where possible:

- a concise vulnerability summary;
- affected GhostWeb Signal version, tag or commit;
- affected Android/device version where relevant;
- technical impact and realistic attack scenario;
- clear reproduction steps or a minimal proof of concept;
- logs or screenshots with secrets and personal information removed;
- whether user interaction or special privileges are required;
- suggested remediation, if known;
- your preferred name/handle for acknowledgement, if desired.

## Coordinated disclosure

GhostWeb Enterprise follows a coordinated-disclosure approach. Please allow maintainers a reasonable opportunity to reproduce, assess and remediate a valid vulnerability before publishing technical details.

After receiving a report, maintainers may:

1. acknowledge and triage the report;
2. request additional information;
3. determine affected versions and severity;
4. develop and privately validate a remediation;
5. prepare a security release and/or GitHub Security Advisory where appropriate;
6. coordinate public disclosure with the reporter after a fix is available.

Response and remediation time depend on severity, reproducibility, upstream dependencies and the complexity of the required fix. This policy does **not** promise a fixed response or patch deadline.

## Security architecture

GhostWeb Signal builds on established Signal/Molly Android components and does not intend to introduce custom cryptographic primitives as a substitute for reviewed upstream cryptography.

Security-sensitive areas include:

- Signal protocol / `libsignal` integration inherited from upstream;
- calling infrastructure such as RingRTC where applicable;
- encrypted local application storage;
- Android platform security and application sandboxing;
- optional application-lock and biometric controls where supported;
- dependency integrity;
- release signing and artifact verification;
- upstream synchronization and security patches.

GhostWeb-specific changes should preserve upstream security properties wherever possible.

## Build and release security

Production release artifacts should follow a fail-closed release process.

GhostWeb release automation is intended to require configured Android signing credentials, reject unsigned production release artifacts and verify APK signatures before publication. Signing credentials, keystores, passwords, tokens and other release secrets must never be committed to this repository.

A GitHub Actions success indicator alone is not proof that an application is vulnerability-free. Users should obtain builds from the official GhostWeb Signal release channel and verify published signatures/checksums where provided.

## Dependency and supply-chain security

Security-relevant dependency updates should be reviewed promptly. Automated dependency, static-analysis or code-scanning results are useful detection mechanisms but do not replace human review.

Contributors should:

- avoid adding unnecessary dependencies;
- use trusted upstream sources;
- never commit credentials or secret material;
- preserve lockfiles/version controls where the build system uses them;
- review security-sensitive dependency changes carefully;
- keep GhostWeb changes reasonably synchronized with relevant upstream security fixes.

## Security testing rules

Good-faith security research is welcome when performed safely and lawfully.

Do not:

- access, modify, delete or retain another person's data without authorization;
- attempt social engineering, phishing or credential theft;
- perform denial-of-service or intentionally degrade services;
- deploy malware or destructive payloads;
- test against accounts, devices or infrastructure you do not own or have explicit permission to test;
- publicly disclose an unpatched vulnerability before reasonable coordinated disclosure.

Use your own test accounts, devices and data wherever possible.

## Out of scope

The following are generally not treated as GhostWeb Signal vulnerabilities unless they demonstrate a concrete security impact caused by this project:

- generic feature requests or UI bugs without a security consequence;
- vulnerabilities requiring an already fully compromised/rooted device with no additional security boundary bypass;
- unsupported or modified third-party APKs;
- reports based solely on automated scanner output without a reproducible impact;
- social-engineering attacks that do not exploit GhostWeb Signal;
- upstream vulnerabilities with no affected GhostWeb code or distributed version.

## No bug bounty promise

GhostWeb Enterprise does not currently promise monetary compensation or operate a guaranteed bug-bounty program. Security researchers may be credited for responsibly disclosed vulnerabilities when appropriate and when they wish to be identified.

## Security vs. general support

For suspected vulnerabilities, use the private security-reporting process above.

For ordinary support, build problems, feature requests or non-sensitive questions:

**support-ghostweb@proton.me**

Project: https://github.com/GhostWebEnterprise/ghost-web-signal

---

**Never include vulnerability details, credentials, private keys, signing material or sensitive user information in a public GitHub issue.**
