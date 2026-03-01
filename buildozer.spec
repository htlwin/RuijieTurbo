[app]
title = Ruijie Turbo
package.name = ruijieturbo
package.domain = org.htlwin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1

# လိုအပ်သော libraries များ
requirements = python3, kivy, requests, urllib3, certifi

orientation = portrait
fullscreen = 0

# Android configuration
android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

# အရေးကြီးဆုံး - HTTP bypass အတွက်
android.meta_data = android:usesCleartextTraffic="true"

# Poco X7 Pro (Snapdragon 750) အတွက်
android.archs = arm64-v8a
android.wakelock = True

[buildozer]
log_level = 2
warn_on_root = 1
