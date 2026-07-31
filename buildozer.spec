[app]
title = Zahala Factory Control
package.name = zahalafactorycontrol
package.domain = com.zahala

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0
requirements = python3,kivy

orientation = landscape
fullscreen = 1

android.api = 35
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
