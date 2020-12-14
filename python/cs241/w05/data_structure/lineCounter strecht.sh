#!/bin/bash

#echo "Runing on file: $1"
#wc -l $1

echo "Runing on directory $1"
echo "Files in the directory:"

for i in $1/*.py ; do
	wc -l $i
done
