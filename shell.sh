#!/bin/bash
cp deneme /home/dyilmaz/Desktop/book/all
cd /home/dyilmaz/Desktop/book/all
split -l 9 deneme
cd /home/dyilmaz/Desktop/book/all
rm deneme
ls | while read filename
do
  tr '\n' '*'< $(echo $filename) > 1$(echo $filename)
done
rm x*
paste -s * > last.csv
