#!/bin/bash

WHEN_START="$1"
WHEN_END="$2"

## start time
START_MANTH=$(echo ${WHEN_START} | awk '{ print $1 }')
START_DAY=$(echo ${WHEN_START} | awk '{ print $2 }')
START_TIME=$(echo ${WHEN_START} | awk '{ print $3 }')

START_H=$(echo ${START_TIME} | awk -F ":" '{ print $1 }')
START_M=$(echo ${START_TIME} | awk -F ":" '{ print $2 }')
START_S=$(echo ${START_TIME} | awk -F ":" '{ print $3 }')

## end time
END_MANTH=$(echo ${WHEN_END} | awk '{ print $1 }')
END_DAY=$(echo ${WHEN_END} | awk '{ print $2 }')
END_TIME=$(echo ${WHEN_END} | awk '{ print $3 }')

END_H=$(echo ${END_TIME} | awk -F ":" '{ print $1 }')
END_M=$(echo ${END_TIME} | awk -F ":" '{ print $2 }')
END_S=$(echo ${END_TIME} | awk -F ":" '{ print $3 }')

## Function
grep_syslog ()
{
	grep -w "${START_MANTH} ${START_DAY} ${START_H}:${START_M}" /var/log/messages
}

grep_syslog

