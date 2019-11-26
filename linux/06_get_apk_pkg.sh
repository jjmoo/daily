# 获取指定目录及子目录下所有APK文件对应的包名
find . -name "*.apk" | xargs -i bash -c "aapt d badging {} 2>/dev/null | head -1 | cut -d \' -f 2" | sort
