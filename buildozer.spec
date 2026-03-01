[app]
title = Ruijie Turbo Pro
package.name = ruijieturbo
package.domain = org.htlwin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.2

# လိုအပ်သော libraries များ
requirements = python3, kivy, requests, urllib3, certifi

orientation = portrait
fullscreen = 0

# Android configuration
android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.ndk = 23b
android.skip_update = False
android.accept_sdk_license = True

# အရေးကြီးဆုံး - Router Bypass အတွက် HTTP ခွင့်ပြုရန်
android.meta_data = android:usesCleartextTraffic="true"

# Poco X7 Pro အတွက် Architecture
android.archs = arm64-v8a
android.wakelock = True

[buildozer]
log_level = 2
warn_on_root = 1
