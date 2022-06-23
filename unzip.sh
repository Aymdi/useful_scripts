#!/bin/bash

echo ">> unzipping files ..."
for file in $(pwd)/*.zip
do
    zipfile=$(echo "$(basename "$file")")  
    unzipfile=$(echo "$(basename "$file")"|cut -d "." -f 1)
    echo "> unzipping" $zipfile
    unzip $zipfile -d $unzipfile/
    echo "> removing" $zipfile
    rm $zipfile
done
