import org.jetbrains.kotlin.gradle.dsl.JvmTarget

plugins {
  id("com.android.test")
  id("androidx.baselineprofile") version "1.5.0-rc01"
}

android {
  namespace = "org.ghostweb.baselineprofile"
  compileSdk {
    version = release(36)
  }

  compileOptions {
    sourceCompatibility = JavaVersion.toVersion(libs.versions.javaVersion.get())
    targetCompatibility = JavaVersion.toVersion(libs.versions.javaVersion.get())
  }

  defaultConfig {
    minSdk = 28
    targetSdk = 36

    testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
  }

  buildTypes {
    create("mocked") {
      matchingFallbacks += "debug"
      isDebuggable = true
    }
  }

  targetProjectPath = ":app"

  flavorDimensions += listOf("distribution", "environment")
  productFlavors {
    create("website") { dimension = "distribution" }
    create("prod") { dimension = "environment" }
  }

  testOptions {
    managedDevices {
      localDevices {
        create("api31") {
          device = "Pixel 3"
          apiLevel = 31
          systemImageSource = "aosp"
          require64Bit = false
        }
      }
    }
  }
}

kotlin {
  compilerOptions {
    jvmTarget = JvmTarget.fromTarget(libs.versions.kotlinJvmTarget.get())
  }
}

baselineProfile {
  managedDevices += "api31"
  useConnectedDevices = false
}

dependencies {
  implementation("androidx.test.ext:junit:1.2.1")
  implementation("androidx.test.espresso:espresso-core:3.7.0")
  implementation("androidx.test.uiautomator:uiautomator:2.3.0")
  implementation("androidx.benchmark:benchmark-macro-junit4:1.4.1")
}

androidComponents {
  beforeVariants(selector().all()) {
    if (it.flavorName != "websiteProd" && it.buildType != "mocked") {
      it.enable = false
    }
  }
}
