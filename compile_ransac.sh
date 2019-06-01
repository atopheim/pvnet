#!/bin/bash

ROOT=$(pwd)  
DIRECTORY=$ROOT/lib/ransac_voting_gpu_layer
$pwd
echo "target directory: $DIRECTORY"
if [ -d "$DIRECTORY" ]; then
	echo Building...
fi
if [ ! -d "$DIRECTORY" ]; then
	echo Folder not found, are you sure you are in root?
	exit
fi

cd $ROOT/lib/ransac_voting_gpu_layer
python3 setup.py build_ext --inplace
echo ls
ls
echo Compiling extention utils...
cd $ROOT/lib/utils/extend_utils

