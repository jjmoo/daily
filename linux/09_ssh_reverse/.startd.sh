#!/bin/bash

while true; do
    RET=`ps ax | grep "ssh -f -N -R 8868:localhost:22" | grep -v "grep"`
    if [ "$RET" = "" ]; then
        echo "restart ssh server"
        ssh -f -N -R 8868:localhost:22 ubuntu@tx.jjmoo.com
    fi
    sleep 10
done
