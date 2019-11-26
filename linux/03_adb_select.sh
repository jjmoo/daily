function fdadb {
    if [ -z $1 ]; then
        unset ANDROID_SERIAL
        adb devices -l
    else
        export ANDROID_SERIAL=$1
    fi
}
