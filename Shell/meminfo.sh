#!/bin/bash

A=$(cat /proc/meminfo | grep "MemFree" | awk '{ print $2 }')
B=$(cat /proc/meminfo | grep "MemTotal" | awk '{ print $2 }')

A_new=$(echo "scale=5; ${A} / 1000000" | bc | awk '{ printf "%.5f\n", $0}')
B_new=$(echo "scale=5; ${B} / 1000000" | bc | awk '{ printf "%.5f\n", $0}')

echo "MemFree: ${A_new} GB"
echo "MemTotal: ${B_new} GB"

RATIO=$(echo "scale=10; ${A} / ${B}" | bc | awk '{ printf "%.10f\n", $0}')

echo "scale=5; (1 - ${RATIO}) * 100" | bc | awk '{ printf "%-20s %.5f %s\n", "Memory usage rate", $0, "%"}'
