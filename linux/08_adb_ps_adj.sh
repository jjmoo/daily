function adbps {
    if [ -z $1 ]; then
        adb shell ps -e -o USER:12=UID,PID,PPID,S,ARGS=CMD
    else
        adb shell ps -e -o USER:12=UID,PID,PPID,S,ARGS=CMD | grep $1 | tee __tmp1.txt | awk '{print $2}' | xargs -i adb shell cat /proc/{}/oom_score_adj > __tmp2.txt && paste __tmp2.txt __tmp1.txt && /bin/rm __tmp1.txt __tmp2.txt
    fi
}
