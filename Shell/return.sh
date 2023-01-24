#!/bin/bash

# Variables
#ret1=0
#ret2=0

func_return()
{
    ret1=$1
    ret2=$2
}

func_return $1 $2

echo "${ret1}"
echo "${ret2}"