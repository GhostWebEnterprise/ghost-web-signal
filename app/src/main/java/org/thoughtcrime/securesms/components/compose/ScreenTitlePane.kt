/*
 * Copyright 2025 Signal Messenger, LLC
 * SPDX-License-Identifier: AGPL-3.0-only
 */

package org.thoughtcrime.securesms.components.compose

import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.adaptive.currentWindowAdaptiveInfo
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.window.core.layout.WindowSizeClass
import org.thoughtcrime.securesms.ghostweb.photon.PhotonGlassSurface

/**
 * Displays the screen title for split-pane UIs on tablets and foldable devices.
 */
@Composable
fun ScreenTitlePane(
  title: String,
  modifier: Modifier = Modifier,
) {
  val windowSizeClass = currentWindowAdaptiveInfo().windowSizeClass
  val startPadding = if (
    windowSizeClass.isWidthAtLeastBreakpoint(WindowSizeClass.WIDTH_DP_EXPANDED_LOWER_BOUND)
  ) 80.dp else 20.dp

  PhotonGlassSurface(
    modifier = modifier.padding(
      start = startPadding,
      end = 20.dp,
      bottom = 12.dp,
    ),
    cornerRadius = 16.dp,
    padding = PaddingValues(horizontal = 16.dp, vertical = 8.dp),
  ) {
    Text(
      text = title,
      style = MaterialTheme.typography.headlineLarge,
      color = MaterialTheme.colorScheme.onSurface,
    )
  }
}
