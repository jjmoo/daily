#!/bin/bash

# append "~/.start.sh" to "~/.profile" for ubuntu 18.04

RET=`ps ax | grep ".startd.sh" | grep -v "grep"`
if [ "$RET" = "" ]; then
    echo "run ~/.startd.sh"
    ~/.startd.sh &
fi
