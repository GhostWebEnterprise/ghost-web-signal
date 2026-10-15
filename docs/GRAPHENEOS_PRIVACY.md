# GrapheneOS-compatible device privacy

Open Settings > Privacy > Device privacy (Enhetsintegritet in Swedish).

This is an app-level compatibility integration, not an embedded GrapheneOS ROM.
It uses public Android APIs and the existing Material 3 settings components;
it adds no OS forks, privileged permissions, hidden APIs or dependencies.
GrapheneOS code is not copied into this app and GrapheneOS affiliation is not implied.

## Implemented

- App protections are available independently of GrapheneOS on supported Android
  devices. An app-lock entry returns to the existing Privacy page for Molly
  passphrase/automatic lockdown/biometric configuration instead of creating a
  second authentication flow.
- Notification content is selectable directly using upstream all/contact/none
  values and SignalStore.settings.messageNotificationsPrivacy. Existing displayed
  notifications are refreshed on the bounded executor after a user selection.
  This uses the same preference as the main Notifications settings page.
- Screenshot/recents protection and incognito keyboard switches use the existing
  Signal/Molly preference keys and implementations. Mandatory screen protection
  remains enforced by ScreenLockController. Keyboard privacy is a request to the IME.
- System app-info entry points explain Contact Scopes, Storage Scopes, Network
  and exploit protection. These controls are set by the user in GrapheneOS.
  Other Android devices retain their normal app-info controls. No OS detection
  or claim that a protection is active is made.
- System notification settings open for the running application's package ID,
  including staging/custom package IDs. Unsupported or blocked settings intents
  fall back to app info, then an error message.
- Android automatic backup is disabled in the manifest. Full-backup and Android
  12+ data-extraction rules exclude every supported app storage domain from both
  cloud backup and automatic device transfer. The existing backup agent is kept
  in source for upstream compatibility but allowBackup=false disables its
  Android Backup Service participation, including SVR authentication tokens.
  Existing cloud backups are not remotely erased by this change.

## Additional GrapheneOS feature entry points

Device-specific guides are collapsed by default behind Show device feature
guides. This is an in-screen display preference, not an OS security toggle.
The device-privacy screen also offers:

| Requested feature | App integration |
| --- | --- |
| Automatic OS updates and first-boot rollback | Opens the official GrapheneOS update guide. The OS owns update installation, restart and rollback; the existing app updater is unchanged. |
| Unlocking for sensitive quick settings | Opens the official feature guide. The OS enforces its system tiles. GhostWeb currently declares no TileService, and no tile or unlock bypass is added. |
| Longer device passwords, fingerprint unlock, auto reboot | Opens Android Security settings with GrapheneOS-specific guidance; device settings remain user-controlled. |
| More profiles, end session, installation restrictions, install available apps | Opens the public system Settings screen and explains System > Multiple users. No hidden profile APIs or cross-profile data sharing. Ending a secondary session stops its message delivery. |
| VPN leak blocking | Opens Android VPN settings with always-on/block-without-VPN guidance and delivery implications. Does not install a VPN or claim a leak test has passed. |
| Location indicator | Opens app info for reviewing location permission; the indicator remains an OS feature. |
| Disable installed apps | Opens app info and explains that disabling GhostWeb stops messaging until re-enabled. |
| GrapheneOS Camera and PDF Viewer | Opens the official feature guide; existing camera/attachment behavior is unchanged. |
| Log viewer and crash reports | Opens the official feature guide and points to existing Help/debug logs. Does not collect or upload logs. |

These entry points are instructions and navigation, not reimplementations of OS
security. On stock Android, only that device's available settings apply. Public
system actions used are ACTION_SECURITY_SETTINGS, ACTION_SETTINGS and
ACTION_VPN_SETTINGS; all share the existing guarded fallback to app info.

Molly's PassphraseValidator truncates only the input to its strength estimator;
this is not a device-password limit. Its passphrase encryption and biometric
authentication implementations are preserved. GrapheneOS lock-screen fingerprint
attempt limits and device password length are enforced by the OS, not this app.

## Preserved upstream behavior

Production Signal servers, staging Signal servers, libsignal, RingRTC,
registration, contact discovery/sync, messaging, database encryption, Molly
passphrase/biometric locks, dependency versions, package IDs, signing and build
flavors are unchanged. Do not replace upstream encrypted storage with
EncryptedSharedPreferences: it would not preserve the upstream database design.
App-initiated backup, export and transfer flows are unchanged; the automatic
Android backup restrictions do not disable those separate user actions.

Contact Scopes intentionally restrict which device contacts are visible and
block device contact writes. The integration does not enable scopes or revoke
permissions automatically. Network permission must remain enabled for messaging.
Do not disable GrapheneOS exploit protections globally as a compatibility workaround.

## Verification

Run `python tools/check_graphene_privacy.py` for source-level backup and navigation
contracts. These checks do not compile an APK or prove runtime behavior.

With JDK 21 and the repository's Android SDK installed, run the existing Gradle
checks and builds for the selected prod/staging and website/store variants. Before
release, inspect merged manifests and test on GrapheneOS and stock Android:

1. Navigate to Device privacy; toggle both switches and verify the main Privacy
   page agrees. Reopen the app to confirm persistence. Confirm mandatory screen
   protection cannot be disabled; check screenshots and recents behavior.
   Choose all/contact/none notification content and check both current and new
   notifications and agreement with the main Notifications settings page. Open
   App lock and confirm it returns to the existing Privacy settings without
   bypassing authentication. Test optional guides collapsed and expanded.
2. Open every system settings entry and return; test navigation failure handling.
3. Enable Contact Scopes manually and verify only chosen device contacts are
   visible, existing conversations still work, and no contacts are deleted.
4. Exercise photo/file attachments with restricted storage access.
5. Send/receive messages and make calls with production Signal registration,
   including background delivery on a GrapheneOS device without Play services.
6. Verify Android backup/restore and setup device transfer cannot extract app data;
   test the existing explicit Signal/Molly backup/restore separately.

## Sources

- https://github.com/GrapheneOS
- https://grapheneos.org/usage#contact-scopes
- https://grapheneos.org/usage#storage-scopes
- https://grapheneos.org/usage#bugs-uncovered-by-security-features
- https://developer.android.com/identity/data/autobackup
