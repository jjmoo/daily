#!/bin/bash

count=0
while true; do
    PID=`ps ax | grep "8868:localhost:22" | grep -v "grep" | cut -d " " -f 1`
    if [ "$PID" = "" ]; then
        count=0
        echo "`date` --> restart 8868"
        ssh -f -N -R 8868:localhost:22 ubuntu@tx.jjmoo.com
    else
        let count++
        if [ $count -ge 30 ]; then
            count=0
            RET=`who -a | grep "127.0.0.1"`
            if [ "$RET" = "" ]; then
                echo "`date` --> kill 8868"
                kill $PID
            fi
        fi
    fi
    sleep 10
done
