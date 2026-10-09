# GhostWeb Signal — Liquid Glass Photon Integration

This package contains the files needed to apply the new **Liquid Glass Photon** UI design to GhostWeb Signal.

## Files included

```text
app/src/main/res/values/colors.xml                          # Expanded dark + light tokens
core/ui/src/main/res/values/molly_colors.xml                # Photon cyan primary + navy surfaces
app/src/main/res/drawable/ghostweb_signal_*.xml             # Glass surfaces
docs/design-system/GhostWeb_Liquid_Glass_Design_System.md   # Design system (Markdown)
docs/design-system/GhostWeb_Liquid_Glass_Design_System.pdf  # Design system (PDF)
art/                                                        # Existing GhostWeb icons
```

## How to apply

1. Extract this archive into the root of your GhostWeb Signal repository (or copy the folders).
2. Accept overwrites for the listed files.
3. Rebuild:

```bash
./gradlew :app:assembleProdWebsiteRelease
```

## What changed visually

- Primary color: Molly purple → Photon cyan (`#5B9DFF` / `#2B7BFF`)
- Backgrounds & surfaces: Deep navy Photon palette
- New light-mode tokens ready for day/night switching
- Glass-style headers, chips and status badges

See `docs/design-system/` for the full design system.
