[app]

# (str) Title of your application
title = Ruijie Turbo

# (str) Package name
package.name = ruijieturbo

# (str) Package domain (needed for android/ios packaging)
package.domain = org.htlwin

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# requests, urllib3 နဲ့ certifi တို့က bypass logic အတွက် အဓိက လိုအပ်ပါတယ်
requirements = python3, kivy, requests, urllib3, certifi

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
# WiFi အခြေအနေ စစ်ဆေးရန်နှင့် Internet သုံးရန် လိုအပ်သော permissions များ
android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE

# (int) Target Android API (Android 12 အတွက် 31 က အကောင်းဆုံးပါ)
android.api = 31

# (int) Minimum API support (Android 5.0 အထက်)
android.minapi = 21

# (int) Android NDK API (Stability အတွက် 21 ထားပါသည်)
android.ndk_api = 21

# (bool) If True, then automatically accept SDK license
# GitHub Actions မှာ license မေးတာကို အလိုအလျောက် ကျော်ရန် ဖြစ်သည်
android.accept_sdk_license = True

# (str) Android manifest meta-data 
# အရေးကြီးဆုံးအချက် - Router IP (192.168.110.1) ဆီသို့ HTTP traffic ပေးပို့ခွင့်ပြုရန် ဖြစ်သည်
android.meta_data = android:usesCleartextTraffic="true"

# (list) The Android archs to build for
# Poco X7 Pro (64-bit) အတွက် arm64-v8a ကို အဓိကထားသည်
android.archs = arm64-v8a

# (bool) Indicate whether the screen should stay on
# Bypass လုပ်နေစဉ် ဖုန်း screen မပိတ်သွားစေရန်
android.wakelock = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

[buildozer]

# (int) Log level (2 = အမှားရှာရလွယ်အောင် အသေးစိတ်ပြသမည်)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
