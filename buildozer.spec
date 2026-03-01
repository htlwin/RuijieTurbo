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
# requests, urllib3 နဲ့ certifi တို့ကို မဖြစ်မနေ ထည့်သွင်းပေးထားပါတယ်
requirements = python3, kivy, requests, urllib3, certifi, libffi

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
# Network စစ်ဆေးဖို့နဲ့ Internet သုံးဖို့ လိုအပ်တဲ့ Permissions များ
android.permissions = INTERNET, ACCESS_WIFI_STATE, ACCESS_NETWORK_STATE

# (int) Target Android API (Android 12/13 အတွက် 33 သို့မဟုတ် 31 ထားခြင်းက အဆင်ပြေဆုံးပါ)
android.api = 31

# (int) Minimum API support (Android 5.0 အထက်)
android.minapi = 21
android.ndk_api = 31
# (bool) If True, then automatically accept SDK license
# build လုပ်စဉ် license မေးတာကို အလိုအလျောက် ကျော်သွားစေဖို့ ဖြစ်ပါတယ်
android.accept_sdk_license = True

# (list) The Android archs to build for
# Redmi Note 11 Pro 5G (Snapdragon 750) အတွက် arm64-v8a ကို အဓိကထားပါတယ်
android.archs = arm64-v8a

# (bool) Indicate whether the screen should stay on
# Script run နေစဉ် ဖုန်း screen မပိတ်သွားစေဖို့ True ထားပေးပါ
android.wakelock = True

[buildozer]

# (int) Log level (2 = အမှားရှာရလွယ်အောင် အသေးစိတ်ပြသမည်)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
