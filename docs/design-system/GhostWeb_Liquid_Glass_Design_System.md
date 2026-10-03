# GhostWeb Signal — Liquid Glass Design System
**Version 2.0 · Photon Edition**

## 1. Brand Overview
**GhostWeb Signal** is a privacy-first messaging app built on the Signal protocol. The new **Liquid Glass Photon** visual language combines deep navy / ice-blue Photon theming, translucent Liquid Glass surfaces, Signal-inspired information architecture, and high legibility.

**Tagline:** Secure. Private. Untraceable.

## 2. Color System
### Dark Mode
- `bg`: `#050914`
- `surface / panel`: `#0D1A33`
- `surface_high`: `#132445`
- `surface_low`: `#08101F`
- `primary / cyan`: `#5B9DFF`
- `text`: `#E8EEF8`
- `text_muted`: `#8AA0C0`
- `success / online`: `#6EE7B7`
- `on_cyan`: `#041018`

### Light Mode
- `bg_light`: `#F0F5FF`
- `panel_light`: `#FFFFFF`
- `surface_highest_light`: `#E8F0FF` / `#D6E6FF`
- `primary_light`: `#2B7BFF`
- `text_light`: `#0A1628`
- `text_muted_light`: `#5A6F8C`

### Glass Alpha Tokens
`glass_10` 10% cyan; `glass_20` 20% cyan; `glass_30` 30% cyan; `glass_surface` ~80% panel; `glass_surface_elevated` ~90% elevated.

## 3. Typography
System / Inter / SF Pro; Regular 400, Medium 500, Semibold 600. Mobile: Display 28–34sp, Title 20–22sp, Body 15–16sp, Caption 12–13sp, Overline 11sp.

## 4. Spacing & Radius
Small 8–10dp, medium 14–16dp, large 20–24dp, full 999dp. Spacing scale: 4 / 8 / 12 / 16 / 20 / 24 / 32dp.

## 5. Components
Glass cards use `glass_surface`, 1dp subtle outline and 16dp radius. Primary buttons use `#5B9DFF`, 14–16dp radius and 48–52dp height. Message bubbles use cyan-tinted glass for outgoing and dark glass for incoming. Bottom navigation is a floating glass bar. Avatars are circular with cyan ring/green status. Unread badges are cyan pills.

## 6. Elevation & Effects
Prefer glass + borders over heavy shadows. Use soft blur when supported, subtle cyan focus glow, and no harsh drop shadows.

## 7. Iconography
GhostWeb app icon with liquid-glass ring and cyan glow. System icons use outlined 1.5–2px strokes.

## 8. Accessibility
Minimum 4.5:1 body-text contrast, interactive targets ≥48×48dp, system font scaling, and increased border opacity in high-contrast mode.

## 9. Android Implementation
Tokens live in `res/values/colors.xml` and `core/ui/.../molly_colors.xml`. Material 3 consumes the updated Molly tokens. Custom `ghostweb_signal_*_background.xml` drawables use glass alpha. Splash uses `ghostweb_signal_bg`.

**GhostWeb Enterprise · Liquid Glass Photon Design System v2.0**
