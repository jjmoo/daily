function lspkg {
    adb shell pm list package -3 | cut -d : -f 2
}

function stpkg {
    adb shell dumpsys package $1 | grep -B 2 "android.intent.category.LAUNCHER" | head -1 | awk '{print $2}' | xargs adb shell am start -n
}

function lppkg {
    for pkg in `lspkg`; do
        echo "start pkg: $pkg"
        stpkg $pkg 2>/dev/null
        sleep 3
    done
}
