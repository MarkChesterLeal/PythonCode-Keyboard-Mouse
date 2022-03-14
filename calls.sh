#!/bin/bash

export DISPLAY=:10.0

xhost +

PYSCRIPT="/home/ubuntu/.idle/idle.py"

CMD="python3 /home/ubuntu/.idle/idle.py"

processNum=$(ps ax | grep "python3 /home/ubuntu/.idle/idle.py" | wc -l)

if [ $processNum -le 1 ]; then

    echo "$PYSCRIPT is not running will attempt to start now"
    exec python3 "$PYSCRIPT" &

elif
    [ $processNum -ne 2 ]
then

    echo "$CMD still not met"

else
    [ $processNum -eq 2 ]

    echo "already running"

fi

#export DISPLAY=:10.0
#xhost +
#nohup python3 /home/ubuntu/.idle/idle.py &
