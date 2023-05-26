#!/bin/bash

bytes_enviados=10000
frequencia=15
tempo=25

# Progreção do número de clietes
for cl in $(seq 200 200 3000); do
    python subscriber.py ./res/recebidos_$cl.txt &

    for c in $(seq 1 1 $cl); do
        python publisher.py $(($bytes_enviados)) $frequencia &
    done

    for t in $(seq $tempo); do
        docker stats --format "|{{.CPUPerc}}|{{.MemUsage}}|{{.NetIO}}" --no-stream >> ./res/log$cl.txt   
    done

    killall python
done

killall python