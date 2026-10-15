package org.thoughtcrime.securesms.ui

import android.app.Application
import android.content.Context
import androidx.core.graphics.ColorUtils
import androidx.test.core.app.ApplicationProvider
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
import org.thoughtcrime.securesms.R

@RunWith(RobolectricTestRunner::class)
@Config(application = Application::class, sdk = [28])
class GhostWebNeutralPaletteTest {
  private val context: Context = ApplicationProvider.getApplicationContext()

  @Test
  fun lightTextPairsMeetMinimumContrast() {
    assertContrast(R.color.molly_on_surface_light, R.color.molly_surface_light)
    assertContrast(R.color.molly_on_surface_variant_light, R.color.molly_surface_container_low_light)
    assertContrast(R.color.molly_on_primary_light, R.color.molly_primary_light)
    assertContrast(R.color.molly_on_primary_container_light, R.color.molly_primary_container_light)
  }

  @Test
  fun darkTextPairsMeetMinimumContrast() {
    assertContrast(R.color.molly_on_surface_dark, R.color.molly_surface_dark)
    assertContrast(R.color.molly_on_surface_variant_dark, R.color.molly_surface_container_low_dark)
    assertContrast(R.color.molly_on_primary_dark, R.color.molly_primary_dark)
    assertContrast(R.color.molly_on_primary_container_dark, R.color.molly_primary_container_dark)
  }

  private fun assertContrast(foreground: Int, background: Int) {
    val ratio = ColorUtils.calculateContrast(context.getColor(foreground), context.getColor(background))
    assertTrue("Text contrast must be at least 4.5:1, was $ratio", ratio >= 4.5)
  }
}
