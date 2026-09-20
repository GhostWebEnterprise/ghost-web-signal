package org.thoughtcrime.securesms.main

import android.app.Application
import android.provider.Settings
import android.view.View
import android.widget.FrameLayout
import org.junit.Assert.assertEquals
import org.junit.Assert.assertSame
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.RuntimeEnvironment
import org.robolectric.annotation.Config

@RunWith(RobolectricTestRunner::class)
@Config(application = Application::class, sdk = [28])
class GhostWebStartupAnimationTest {
  private lateinit var container: FrameLayout
  private lateinit var content: View

  @Before
  fun setUp() {
    val context = RuntimeEnvironment.getApplication()
    container = FrameLayout(context)
    content = View(context)
    container.addView(content)
    Settings.Global.putFloat(context.contentResolver, Settings.Global.ANIMATOR_DURATION_SCALE, 1f)
  }

  @Test
  fun dismissBeforeAuthenticationLeavesOriginalContentUntouched() {
    val animation = GhostWebStartupAnimation(container)
    assertEquals(2, container.childCount)
    animation.dismiss()
    animation.start()
    assertEquals(1, container.childCount)
    assertSame(content, container.getChildAt(0))
    assertEquals(View.VISIBLE, content.visibility)
  }

  @Test
  fun disabledSystemAnimationsRemoveOverlayImmediately() {
    Settings.Global.putFloat(container.context.contentResolver, Settings.Global.ANIMATOR_DURATION_SCALE, 0f)
    GhostWebStartupAnimation(container).start()
    assertEquals(1, container.childCount)
    assertSame(content, container.getChildAt(0))
  }

  @Test
  fun stoppingBeforeFirstFrameCancelsPendingAnimation() {
    val animation = GhostWebStartupAnimation(container)
    animation.start()
    animation.start()
    animation.dismiss()
    animation.dismiss()
    container.viewTreeObserver.dispatchOnPreDraw()
    assertEquals(1, container.childCount)
    assertSame(content, container.getChildAt(0))
  }
}
