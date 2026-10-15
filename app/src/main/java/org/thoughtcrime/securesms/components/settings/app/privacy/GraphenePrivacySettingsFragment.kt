package org.thoughtcrime.securesms.components.settings.app.privacy

import android.content.ActivityNotFoundException
import android.content.Intent
import android.net.Uri
import android.provider.Settings
import android.widget.Toast
import androidx.navigation.fragment.findNavController
import org.signal.core.util.concurrent.SignalExecutors
import org.thoughtcrime.securesms.R
import org.thoughtcrime.securesms.ScreenLockController
import org.thoughtcrime.securesms.components.settings.DSLSettingsFragment
import org.thoughtcrime.securesms.components.settings.DSLSettingsText
import org.thoughtcrime.securesms.components.settings.configure
import org.thoughtcrime.securesms.dependencies.AppDependencies
import org.thoughtcrime.securesms.keyvalue.SignalStore
import org.thoughtcrime.securesms.preferences.widgets.NotificationPrivacyPreference
import org.thoughtcrime.securesms.util.CommunicationActions
import org.thoughtcrime.securesms.util.SecurePreferenceManager
import org.thoughtcrime.securesms.util.TextSecurePreferences
import org.thoughtcrime.securesms.util.WindowUtil
import org.thoughtcrime.securesms.util.adapter.mapping.MappingAdapter

/** Uses upstream app protections and public Android settings intents on every build variant. */
class GraphenePrivacySettingsFragment : DSLSettingsFragment(R.string.GraphenePrivacy__title) {

  private var settingsAdapter: MappingAdapter? = null
  private var showSystemGuides = false

  override fun bindAdapter(adapter: MappingAdapter) {
    settingsAdapter = adapter
    refresh()
  }

  override fun onResume() {
    super.onResume()
    refresh()
  }

  override fun onDestroyView() {
    settingsAdapter = null
    super.onDestroyView()
  }

  private fun refresh() {
    val context = requireContext()
    val screenSecurity = TextSecurePreferences.isScreenSecurityEnabled(context)
    val incognitoKeyboard = TextSecurePreferences.isIncognitoKeyboardEnabled(context)
    val notificationPrivacyValues = resources.getStringArray(R.array.pref_notification_privacy_values)
    val notificationPrivacy = SignalStore.settings.messageNotificationsPrivacy.toString()

    settingsAdapter?.submitList(configure {
      textPref(summary = DSLSettingsText.from(R.string.GraphenePrivacy__intro))
      sectionHeaderPref(R.string.GraphenePrivacy__app_protection)

      clickPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__app_lock),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__app_lock_summary),
        onClick = { findNavController().popBackStack(R.id.privacySettingsFragment, false) }
      )

      radioListPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__message_preview),
        listItems = resources.getStringArray(R.array.pref_notification_privacy_entries),
        selected = notificationPrivacyValues.indexOf(notificationPrivacy).let { if (it >= 0) it else notificationPrivacyValues.indexOf("none") },
        onSelected = { index ->
          SignalStore.settings.messageNotificationsPrivacy = NotificationPrivacyPreference(notificationPrivacyValues[index])
          SignalExecutors.BOUNDED.execute {
            AppDependencies.messageNotifier.updateNotification(context.applicationContext)
          }
          refresh()
        }
      )

      switchPref(
        title = DSLSettingsText.from(R.string.preferences__screen_security),
        summary = DSLSettingsText.from(R.string.PrivacySettingsFragment__block_screenshots_in_the_recents_list_and_inside_the_app),
        isChecked = screenSecurity || ScreenLockController.alwaysSetSecureFlagOnResume,
        isEnabled = !ScreenLockController.alwaysSetSecureFlagOnResume,
        onClick = {
          TextSecurePreferences.setScreenSecurityEnabled(context, !screenSecurity)
          WindowUtil.initializeScreenshotSecurity(context, requireActivity().window)
          refresh()
        }
      )

      switchPref(
        title = DSLSettingsText.from(R.string.preferences__incognito_keyboard),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__keyboard_summary),
        isChecked = incognitoKeyboard,
        onClick = {
          SecurePreferenceManager.getSecurePreferences(context).edit()
            .putBoolean(TextSecurePreferences.INCOGNITO_KEYBOARD_PREF, !incognitoKeyboard).apply()
          refresh()
        }
      )

      dividerPref()
      sectionHeaderPref(R.string.GraphenePrivacy__permissions)
      clickPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__contacts),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__contacts_summary),
        onClick = { openAppSettings() }
      )
      clickPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__storage),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__storage_summary),
        onClick = { openAppSettings() }
      )
      clickPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__network),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__network_summary),
        onClick = { openAppSettings() }
      )
      clickPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__notifications),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__notifications_summary),
        onClick = {
          openSystemSettings(Intent(Settings.ACTION_APP_NOTIFICATION_SETTINGS).putExtra(Settings.EXTRA_APP_PACKAGE, context.packageName))
        }
      )

      dividerPref()
      switchPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__show_system_guides),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__show_system_guides_summary),
        isChecked = showSystemGuides,
        onClick = {
          showSystemGuides = !showSystemGuides
          refresh()
        }
      )
      if (showSystemGuides) {
        sectionHeaderPref(R.string.GraphenePrivacy__device_controls)
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__os_updates),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__os_updates_summary),
          onClick = { CommunicationActions.openBrowserLink(context, "https://grapheneos.org/usage#updates") }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__quick_settings),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__quick_settings_summary),
          onClick = { CommunicationActions.openBrowserLink(context, "https://grapheneos.org/features#other-features") }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__device_lock),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__device_lock_summary),
          onClick = { openSystemSettings(Intent(Settings.ACTION_SECURITY_SETTINGS)) }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__profiles),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__profiles_summary),
          onClick = { openSystemSettings(Intent(Settings.ACTION_SETTINGS)) }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__vpn),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__vpn_summary),
          onClick = { openSystemSettings(Intent(Settings.ACTION_VPN_SETTINGS)) }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__location),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__location_summary),
          onClick = { openAppSettings() }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__disable_app),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__disable_app_summary),
          onClick = { openAppSettings() }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__companion_apps),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__companion_apps_summary),
          onClick = { CommunicationActions.openBrowserLink(context, "https://grapheneos.org/features#grapheneos-camera") }
        )
        clickPref(
          title = DSLSettingsText.from(R.string.GraphenePrivacy__diagnostics),
          summary = DSLSettingsText.from(R.string.GraphenePrivacy__diagnostics_summary),
          onClick = { CommunicationActions.openBrowserLink(context, "https://grapheneos.org/features#log-viewer-and-crash-reporting") }
        )
      }

      dividerPref()
      sectionHeaderPref(R.string.GraphenePrivacy__backup)
      textPref(summary = DSLSettingsText.from(R.string.GraphenePrivacy__backup_summary))
      clickPref(
        title = DSLSettingsText.from(R.string.GraphenePrivacy__learn_more),
        summary = DSLSettingsText.from(R.string.GraphenePrivacy__learn_more_summary),
        onClick = { CommunicationActions.openBrowserLink(context, "https://grapheneos.org/usage") }
      )
    }.toMappingModelList())
  }

  private fun openAppSettings() {
    openSystemSettings(appSettingsIntent())
  }

  private fun appSettingsIntent() = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.fromParts("package", requireContext().packageName, null))

  private fun openSystemSettings(intent: Intent) {
    try {
      startActivity(intent)
    } catch (_: ActivityNotFoundException) {
      openFallbackSettings()
    } catch (_: SecurityException) {
      openFallbackSettings()
    }
  }

  private fun openFallbackSettings() {
    try {
      startActivity(appSettingsIntent())
    } catch (_: ActivityNotFoundException) {
      showSettingsError()
    } catch (_: SecurityException) {
      showSettingsError()
    }
  }

  private fun showSettingsError() {
    Toast.makeText(requireContext(), R.string.PrivacySettingsFragment__failed_to_navigate_to_system_settings, Toast.LENGTH_SHORT).show()
  }
}
