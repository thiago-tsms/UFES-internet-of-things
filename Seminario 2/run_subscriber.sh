#!/bin/bash

bytes_enviados=10000
frequencia=10
tempo=20

# Progreção do número de subscriber
for cl in $(seq 100 100 6000); do
    python publisher.py $(($bytes_enviados)) $frequencia &

    # Um cliente monitora
    python subscriber.py ./res/recebidos_$cl.txt 1 &

    for c in $(seq 1 1 $cl); do
        python subscriber.py ./res/recebidos_$cl.txt -1 &
    done

    for t in $(seq $tempo); do
        docker stats --format "|{{.CPUPerc}}|{{.MemUsage}}|{{.NetIO}}" --no-stream >> ./res/log$cl.txt   
    done

    killall python
done

killall python