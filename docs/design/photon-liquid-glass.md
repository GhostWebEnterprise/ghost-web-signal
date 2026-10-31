# GhostWeb Signal — Photon Liquid Glass UI specification

Figma source: [Photon Liquid Glass design](https://www.figma.com/design/dD6E76OfB9jPoGJhTSDRqq)

## Scope
22 Android screen concepts covering onboarding, registration, chats, conversation, calls, groups, contacts, stories, profile, settings, privacy, security, appearance, media, search, new message, group detail, active call, app lock, linked devices, notifications and about.

24 editable base components/variants in the Figma Components • Photon page.

## Design foundations
- Background #080E1B, glass surface #18243B, raised glass #202C47, accent #536BFF, foreground #EAF1FF.
- Rounded cards 16–25dp, 1dp translucent borders, layered low-opacity shadows.
- Android touch targets >=48dp; scalable typography, screen-reader labels, contrast checks.
- Prefer material transparency only when readable; respect reduced motion and battery saver.
- 120–180ms interactions; preserve gesture navigation and Android back behavior.

## Android implementation plan
1. Audit existing Compose/XML screens and GhostWeb branding assets before modifying UI.
2. Add centralized theme tokens, glass surface and reusable components without replacing messaging infrastructure.
3. Migrate screens in small testable batches; preserve encryption, account registration, calls, notification channels and security settings.
4. Wire actual state, error, loading and permission flows; add screenshot and accessibility regression tests.
5. Verify on-device behavior, CI, signing and release independently before declaring APK ready.

This document describes design intent, not an assertion that Figma screens are implemented in the Android APK. Do not merge UI changes into release branches without regression tests.
