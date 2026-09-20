package org.thoughtcrime.securesms.main

import android.animation.Animator
import android.animation.AnimatorListenerAdapter
import android.animation.ValueAnimator
import android.graphics.RenderEffect
import android.graphics.Shader
import android.os.Build
import android.provider.Settings
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.accessibility.AccessibilityManager
import android.view.animation.LinearInterpolator
import androidx.core.view.OneShotPreDrawListener
import androidx.core.view.doOnPreDraw
import org.thoughtcrime.securesms.R

/** Branding only. MainActivity starts this after its existing authentication gate succeeds. */
class GhostWebStartupAnimation(private val container: ViewGroup) {
  private val overlay = LayoutInflater.from(container.context).inflate(R.layout.ghostweb_startup, container, false)
  private val logo: View = overlay.findViewById(R.id.ghostweb_startup_logo)
  private val halo: View = overlay.findViewById(R.id.ghostweb_startup_halo)
  private val title: View = overlay.findViewById(R.id.ghostweb_startup_title)
  private val tagline: View = overlay.findViewById(R.id.ghostweb_startup_tagline)
  private var animator: ValueAnimator? = null
  private var preDraw: OneShotPreDrawListener? = null
  private var started = false
  private var dismissed = false

  init {
    container.addView(overlay)
    render(0f)
  }

  fun start() {
    if (started || dismissed) return
    started = true

    val accessibility = container.context.getSystemService(AccessibilityManager::class.java)
    val durationScale = Settings.Global.getFloat(container.context.contentResolver, Settings.Global.ANIMATOR_DURATION_SCALE, 1f)
    if (durationScale == 0f || !ValueAnimator.areAnimatorsEnabled() || accessibility?.isTouchExplorationEnabled == true) {
      dismiss()
      return
    }

    // MainActivity holds its first frame until the conversation list is ready.
    preDraw = overlay.doOnPreDraw {
      preDraw = null
      if (!dismissed) {
        animator = ValueAnimator.ofFloat(0f, DURATION_MS.toFloat()).apply {
          duration = DURATION_MS
          interpolator = LinearInterpolator()
          addUpdateListener { render(it.animatedValue as Float) }
          addListener(object : AnimatorListenerAdapter() {
            override fun onAnimationEnd(animation: Animator) = dismiss()
          })
          start()
        }
      }
    }
  }

  fun dismiss() {
    if (dismissed) return
    dismissed = true
    preDraw?.removeListener()
    preDraw = null
    animator?.removeAllListeners()
    animator?.removeAllUpdateListeners()
    animator?.cancel()
    animator = null
    if (Build.VERSION.SDK_INT >= 31) logo.setRenderEffect(null)
    container.removeView(overlay)
  }

  private fun render(elapsedMs: Float) {
    val focus = 1f - (1f - progress(elapsedMs, 0f, 1050f)).let { it * it * it }
    logo.alpha = 0.2f + 0.8f * focus
    logo.scaleX = 1.09f - 0.09f * focus
    logo.scaleY = logo.scaleX
    // Older Android versions use the same scale/fade without a GPU blur API.
    if (Build.VERSION.SDK_INT >= 31) {
      val radius = 22f * container.resources.displayMetrics.density * (1f - focus)
      logo.setRenderEffect(if (radius > 0.1f) RenderEffect.createBlurEffect(radius, radius, Shader.TileMode.DECAL) else null)
    }
    halo.alpha = 0.55f * progress(elapsedMs, 0f, 800f)
    title.alpha = progress(elapsedMs, 430f, 550f)
    tagline.alpha = progress(elapsedMs, 650f, 500f)
    overlay.alpha = 1f - progress(elapsedMs, 1370f, 430f)
  }

  private fun progress(time: Float, start: Float, duration: Float): Float = ((time - start) / duration).coerceIn(0f, 1f)

  private companion object {
    const val DURATION_MS = 1800L
  }
}
