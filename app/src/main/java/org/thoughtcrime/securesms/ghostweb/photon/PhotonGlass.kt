package org.thoughtcrime.securesms.ghostweb.photon

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.defaultMinSize
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

/**
 * Reusable Photon visual primitives. Purely presentational: does not change
 * Signal encryption, message transport, account registration, or app locks.
 *
 * Figma: https://www.figma.com/design/dD6E76OfB9jPoGJhTSDRqq
 */
object PhotonPalette {
  val Background = Color(0xFF080E1B)
  val Glass = Color(0xFF18243B)
  val RaisedGlass = Color(0xFF202C47)
  val Accent = Color(0xFF536BFF)
  val Foreground = Color(0xFFEAF1FF)
  val Muted = Color(0xFFA5B2D0)
}

@Composable
fun PhotonGlassSurface(
  modifier: Modifier = Modifier,
  cornerRadius: Dp = 20.dp,
  padding: PaddingValues = PaddingValues(16.dp),
  elevated: Boolean = false,
  content: @Composable () -> Unit
) {
  val shape = RoundedCornerShape(cornerRadius)
  Box(
    modifier = modifier
      .shadow(if (elevated) 8.dp else 2.dp, shape)
      .clip(shape)
      .background(
        if (elevated) PhotonPalette.RaisedGlass.copy(alpha = 0.94f)
        else PhotonPalette.Glass.copy(alpha = 0.88f)
      )
      .border(BorderStroke(1.dp, PhotonPalette.Accent.copy(alpha = 0.26f)), shape)
      .padding(padding)
  ) {
    content()
  }
}

@Composable
fun PhotonActionSurface(
  onClick: () -> Unit,
  modifier: Modifier = Modifier,
  enabled: Boolean = true,
  content: @Composable () -> Unit
) {
  val interactionSource = remember { MutableInteractionSource() }
  PhotonGlassSurface(
    modifier = modifier
      .defaultMinSize(minHeight = 48.dp)
      .clickable(
        enabled = enabled,
        interactionSource = interactionSource,
        indication = null,
        onClick = onClick
      ),
    elevated = enabled
  ) {
    content()
  }
}
