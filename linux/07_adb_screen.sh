function adbshot {
    adb shell /system/bin/screencap -p /sdcard/screenshot.png
    adb pull /sdcard/screenshot.png "Screenshot_`date +%s`.png"
    adb shell rm /sdcard/screenshot.png
}