plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.ajiganteng.app"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.ajiganteng.app"
        minSdk = 23
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }
}
