#! /bin/bash

for i in `seq -w 01 30`
do
  subdirectory="day$i"
  mkdir "$subdirectory"
  cd $subdirectory
  echo "# Overview for Day $i" > README.md
  cd ..
done
