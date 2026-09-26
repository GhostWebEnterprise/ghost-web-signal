package org.thoughtcrime.securesms.ui

import android.content.Context
import android.graphics.drawable.Drawable
import android.view.LayoutInflater
import android.view.View
import android.widget.FrameLayout
import android.widget.PopupMenu
import android.widget.TextView
import androidx.test.core.app.ApplicationProvider
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.RuntimeEnvironment
import org.robolectric.annotation.Config
import org.thoughtcrime.securesms.R
import org.thoughtcrime.securesms.main.GhostWebStartupAnimation

/**
 * GhostWeb Signal Photon migration UI gate.
 *
 * Regression coverage for the Photon navy/ice re-theme: the resolved theme must
 * stay on the GhostWeb surface palette, primary buttons must use the Photon
 * accent instead of Signal's ultramarine, and the main conversation-list menu
 * must stay intact. Referenced by the release gate in docs/ui-gate.md.
 */
@RunWith(RobolectricTestRunner::class)
@Config(application = android.app.Application::class, sdk = [28])
class GhostWebPhotonUiRegressionTest {

  private val context: Context = ApplicationProvider.getApplicationContext()

  private fun themedContext(): Context {
    val themed = RuntimeEnvironment.getApplication()
    themed.setTheme(R.style.TextSecure_BaseDarkTheme)
    return themed
  }

  private fun android.content.res.Resources.Theme.resolveColor(attr: Int): Int {
    val typedValue = android.util.TypedValue()
    resolveAttribute(attr, typedValue, true)
    return typedValue.data
  }

  private fun Context.getDrawableSafe(id: Int): Drawable = getDrawable(id)

  @Test
  fun photonPalette_isPresent() {
    val resolved = context.getColor(R.color.ghostweb_signal_bg)
    assertEquals(0xFF050914.toInt(), resolved)
  }

  @Test
  fun photonSurfaces_areDistinctLayers() {
    val bg = context.getColor(R.color.ghostweb_signal_bg)
    val panel = context.getColor(R.color.ghostweb_signal_panel)
    val high = context.getColor(R.color.ghostweb_signal_surface_high)
    val highest = context.getColor(R.color.ghostweb_signal_surface_highest)

    assertEquals(4, setOf(bg, panel, high, highest).size)
  }

  @Test
  fun unreadBadge_isPhotonIceBlue_notUpstreamRed() {
    // Photon ice blue #5B9DFF, deliberately not upstream's red #CE4A40.
    assertEquals(0xFF5B9DFF.toInt(), context.getColor(R.color.ConversationListTabs__unread))
  }

  @Test
  fun darkTheme_resolvesGhostWebSurfaceAndAccent() {
    val themed = themedContext()
    val surface = themed.theme.resolveColor(android.R.attr.colorSurface)
    val accent = themed.theme.resolveColor(R.attr.signal_accent_primary)

    assertEquals(context.getColor(R.color.ghostweb_signal_bg), surface)
    assertEquals(context.getColor(R.color.ghostweb_signal_cyan), accent)
  }

  @Test
  fun darkTheme_primaryButtonIsPhotonCyan_notSignalUltramarine() {
    val themed = themedContext()
    val button = themed.theme.resolveColor(R.attr.signal_button_primary)
    val buttonText = themed.theme.resolveColor(R.attr.signal_button_primary_text)

    assertEquals(context.getColor(R.color.ghostweb_signal_cyan), button)
    assertEquals(context.getColor(R.color.ghostweb_signal_on_cyan), buttonText)
  }

  @Test
  fun darkTheme_secondaryButtonStaysOnPhotonSurface() {
    val themed = themedContext()
    val secondary = themed.theme.resolveColor(R.attr.signal_button_secondary)
    assertEquals(context.getColor(R.color.ghostweb_signal_surface_high), secondary)
  }

  @Test
  fun darkTheme_primaryFixedColorsArePhotonTokens() {
    val themed = themedContext()
    val primaryFixed = themed.theme.resolveColor(android.R.attr.colorPrimaryFixed)
    val onPrimaryFixed = themed.theme.resolveColor(android.R.attr.colorOnPrimaryFixed)

    assertEquals(context.getColor(R.color.ghostweb_signal_cyan), primaryFixed)
    assertEquals(context.getColor(R.color.ghostweb_signal_on_cyan), onPrimaryFixed)
  }

  @Test
  fun startupOverlay_laysOutAndCleansUp() {
    val themed = themedContext()
    val container = FrameLayout(themed)
    val content = View(themed)
    container.addView(content)

    val animation = GhostWebStartupAnimation(container)
    assertEquals(2, container.childCount)
    animation.dismiss()
    assertEquals(1, container.childCount)
    assertTrue(container.getChildAt(0) === content)
  }

  @Test
  fun startupOverlay_drawablesInflate() {
    val themed = themedContext()
    assertNotNull(themed.getDrawableSafe(R.drawable.ghostweb_startup_halo))
    assertNotNull(themed.getDrawableSafe(R.drawable.ghostweb_signal_header_background))
    assertNotNull(themed.getDrawableSafe(R.drawable.ghostweb_signal_chip_background))
    assertNotNull(themed.getDrawableSafe(R.drawable.ghostweb_signal_status_background))
  }

  @Test
  fun startupLayout_inflatesWithBrandedStrings() {
    val themed = themedContext()
    val view = LayoutInflater.from(themed).inflate(R.layout.ghostweb_startup, null)

    val title = view.findViewById<TextView>(R.id.ghostweb_startup_title)
    val tagline = view.findViewById<TextView>(R.id.ghostweb_startup_tagline)
    assertEquals(themed.getString(R.string.ghostweb_signal_title), title.text.toString())
    assertEquals(themed.getString(R.string.ghostweb_signal_tagline), tagline.text.toString())
  }

  @Test
  fun conversationListMenu_isIntactForUiGate() {
    val themed = themedContext()
    val menu = PopupMenu(themed, View(themed)).menu
    android.view.MenuInflater(themed).inflate(R.menu.text_secure_normal, menu)

    assertNotNull(menu.findItem(R.id.menu_new_group))
    assertNotNull(menu.findItem(R.id.menu_settings))
    assertNotNull(menu.findItem(R.id.menu_clear_passphrase))
    assertNotNull(menu.findItem(R.id.menu_mark_all_read))
    assertNotNull(menu.findItem(R.id.menu_filter_unread_chats))
    assertNotNull(menu.findItem(R.id.menu_notification_profile))
  }

  @Test
  fun gateVersion_isRegisteredForReleaseVerification() {
    val version = context.getString(R.string.ghostweb_ui_gate_version)
    assertEquals("photon-1", version)
  }
}
