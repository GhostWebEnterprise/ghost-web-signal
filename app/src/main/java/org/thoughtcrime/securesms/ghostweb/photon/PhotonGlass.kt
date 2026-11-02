package org.thoughtcrime.securesms.ghostweb.photon

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.luminance
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

/**
 * Reusable Photon visual primitives. Purely presentational: does not change
 * Signal encryption, message transport, account registration, or app locks.
 *
 * Figma: https://www.figma.com/design/dD6E76OfB9jPoGJhTSDRqq
 */
data class PhotonColors(
  val background: Color,
  val glass: Color,
  val raisedGlass: Color,
  val accent: Color,
  val foreground: Color,
  val muted: Color,
)

object PhotonPalette {
  val dark = PhotonColors(
    background = Color(0xFF080E1B),
    glass = Color(0xFF18243B),
    raisedGlass = Color(0xFF202C47),
    accent = Color(0xFF536BFF),
    foreground = Color(0xFFEAF1FF),
    muted = Color(0xFFA5B2D0),
  )

  val light = PhotonColors(
    background = Color(0xFFF0F5FF),
    glass = Color(0xE6FFFFFF),
    raisedGlass = Color(0xF2FFFFFF),
    accent = Color(0xFF2B7BFF),
    foreground = Color(0xFF0A1628),
    muted = Color(0xFF5A6F8C),
  )

  /**
   * Follow the app's resolved Material theme, including an in-app theme choice
   * that may differ from the Android system-wide dark-mode setting.
   */
  @Composable
  fun current(): PhotonColors = if (MaterialTheme.colorScheme.surface.luminance() < 0.5f) dark else light
}

@Composable
fun PhotonGlassSurface(
  modifier: Modifier = Modifier,
  cornerRadius: Dp = 20.dp,
  padding: PaddingValues = PaddingValues(16.dp),
  elevated: Boolean = false,
  content: @Composable () -> Unit,
) {
  val colors = PhotonPalette.current()
  val shape = RoundedCornerShape(cornerRadius)
  Box(
    modifier = modifier
      .shadow(if (elevated) 8.dp else 2.dp, shape)
      .clip(shape)
      .background(
        if (elevated) colors.raisedGlass.copy(alpha = 0.94f)
        else colors.glass.copy(alpha = 0.88f),
      )
      .border(BorderStroke(1.dp, colors.accent.copy(alpha = 0.26f)), shape)
      .padding(padding),
  ) {
    content()
  }
}

@Composable
fun PhotonActionSurface(
  onClick: () -> Unit,
  modifier: Modifier = Modifier,
  enabled: Boolean = true,
  content: @Composable () -> Unit,
) {
  PhotonGlassSurface(
    modifier = modifier
      .heightIn(min = 48.dp)
      .clickable(enabled = enabled, onClick = onClick),
    elevated = enabled,
  ) {
    content()
  }
}
