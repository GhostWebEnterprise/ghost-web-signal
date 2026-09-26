# GhostWeb Signal UI Gate

The GhostWeb Photon migration is **not** considered complete just because the
Gradle build is green. A release may only be published once the APK has passed
the **UI gate** described in this document. The release pipeline enforces this:
`ghostweb-signal-build.yml` refuses to publish unless the UI gate has been
verified on the exact APK bytes being released.

## Gate version

Current gate version: **`photon-1`**

The gate version is registered in the build (`ghostweb_ui_gate_version` res
value in `app/build.gradle.kts`) and is asserted by
`GhostWebPhotonUiRegressionTest#gateVersion_isRegisteredForReleaseVerification`.
Bump both places together whenever the UI gate criteria change.

## UI migration scope (Photon navy/ice)

The following surfaces must stay on the GhostWeb Photon system before any release:

1. **Theme tokens** — one privacy-first Photon surface in both system modes
   (`TextSecure.BaseLightTheme` → `Theme.Molly.Material3.Dark`): surfaces,
   outlines, buttons, and fixed color roles resolve to `ghostweb_signal_*`
   tokens, never Signal ultramarine or Molly light palette leaks.
2. **Startup** — Photon splash (`Theme.Molly.Starting.*`) and the
   `GhostWebStartupAnimation` overlay with brand strings; overlay must clean up
   without touching original content and must respect disabled animations.
3. **Settings, menus and dialogs** — `ThemeOverlay.Signal.MaterialAlertDialog`,
   bottom sheets, context menus and the main conversation-list menu
   (`text_secure_normal.xml`) resolve on dark Photon chrome.
4. **Chats / Calls / navigation / FAB** — unread badges use Photon ice blue
   (`ConversationListTabs__unread`), bottom navigation containers use
   `navbar_container_color`, and the FAB inherits Photon primary colors.
5. **Privacy / Security / Biometrics / PIN** — screen lock and PIN surfaces run
   on the same dark Photon theme (no light fallback windows).
6. **Appearance** — enabling Material You dynamic colors keeps system bars on
   the Photon background (`Theme.Molly.Dynamic.*`).
7. **Conversations / Groups** — conversation surfaces (bubbles, quotes,
   compose, message requests) resolve through theme attributes only.

## Automated regression suite

`app/src/test/java/org/thoughtcrime/securesms/ui/GhostWebPhotonUiRegressionTest.kt`
covers: palette presence, distinct surface layers, ice-blue unread badge,
resolved theme surface/accent, Photon primary and secondary buttons, fixed color
roles, startup overlay lifecycle, startup drawables/layout, menu integrity and
the registered gate version.

The CI build job runs this suite as part of
`:app:testProdWebsiteDebugUnitTest` and fails the run on any regression.

## Release gating

`ghostweb-signal-build.yml` (`Enforce UI gate before publishing`):

- Refuses to publish when the gate summary file (`dist/UI_GATE.md`) is missing.
- Refuses to publish when the gate version in `UI_GATE.md` does not match
  `photon-1` (the expectation is injected as `UI_GATE_EXPECTED_VERSION`).
- Refuses to publish when the gate marker `UI_GATE_STATUS: PASS` is absent.

The publish job downloads the gate summary together with the APK and only then
creates the GitHub Release, so a green build alone can never release a new APK.

## Manual pass still required

A physical-device pass (registration, biometric unlock, calls, group messaging)
remains part of the gate before promoting a release to stable; CI covers the
automated portion only.
