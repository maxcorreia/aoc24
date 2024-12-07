#!/bin/sh
mkdir "day$(date +%d)"
cd "day$(date +%d)"
cp ../template.py "$(date +%-d).py"
touch input.txt
touch test.txt 
