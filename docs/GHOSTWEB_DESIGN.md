# GhostWeb: GrapheneOS restraint, Molly familiarity

The existing native Android UI uses neutral graphite surfaces in dark mode,
off-white surfaces in light mode, and a restrained blue accent. This is an
independent visual interpretation, not a copy of GrapheneOS system UI.

## Implemented

- App-level overrides for 60 existing Molly Material color resources. Library
  resource names and upstream dependencies remain unchanged.
- Compose's default light/dark schemes resolve the same color resources as XML,
  so app overrides apply to both UI systems. Extended surface roles follow the
  selected Material scheme. The existing dynamic-color selection remains intact.
- The conversation-list brand header has 16dp outer spacing, 20dp inner spacing,
  a 20sp title and 12sp subtitle. Wrap-content height accommodates larger text.
  The old static ONLINE label is removed: it was not live connection status.
- Header and chip backgrounds use theme attributes, opaque surfaces and restrained
  rounding instead of translucent blue fills and decorative strokes.
- Startup lettering uses normal tracking and a readable 12sp tagline.

Messaging, conversation rows, navigation destinations, chat customization,
registration, servers, calls, contact storage and crypto code are unchanged.
The companion design-reference image illustrates hierarchy and colors; its
sample conversation rows and navigation arrangement are not a runtime screenshot
or a claim that those layouts were reimplemented.

## Verification and limits

Ten calculated text/background pairs meet a 4.5:1 contrast ratio. This is a
limited palette check, not full accessibility certification. Full app review
must cover large fonts, small screens, dynamic colors, RTL, notifications,
wallpapers and all interaction states on an Android device.

Java/JDK and Android SDK downloads were attempted, but network timeouts prevented
toolchain setup. No Android compile, emulator run or physical-device test has
completed. Do not describe the design-reference illustration as a built app.

References: https://grapheneos.org/source#grapheneos and the existing Molly-based
GhostWeb components in this repository. No GrapheneOS OS repositories were
embedded into the app.
