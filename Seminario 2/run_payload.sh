#!/bin/bash

n_clientes=1
bytes_enviados=1000
frequencia=10
tempo=10 # Cada coleta ocerre entre (1 e 2 segundos)

for be in $(seq 1 1 $bytes_enviados); do
    python subscriber.py >> ./res/recebidos.txt &
    python publisher.py $(($be*10000000)) $frequencia &

    for t in $(seq $tempo); do
        docker stats --format "|{{.CPUPerc}}|{{.MemUsage}}|{{.NetIO}}" --no-stream >> ./res/log$be.txt   
    done

    killall python
done

killall python
