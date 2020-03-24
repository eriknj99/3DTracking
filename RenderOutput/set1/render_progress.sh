#!/bin/bash

maxFrames=100

while [ true ]; do

numX=$(ls -1 X | wc -l)
numY=$(ls -1 Y | wc -l)
numZ=$(ls -1 Z | wc -l)

echo -e "   \e[31mX : $numX/$maxFrames"
echo -e "   \e[32mY : $numY/$maxFrames"
echo -e "   \e[34mZ : $numZ/$maxFrames"


sleep 2

tput cuu1 # move cursor up by one line
tput el # clear the line
tput cuu1
tput el
tput cuu1
tput el

done
