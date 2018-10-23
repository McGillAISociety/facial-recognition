#!/bin/bash

wget --content-disposition https://www.dropbox.com/s/sackvibhwzhn7jw/20180402-114759%20%282%29.zip?dl=1 -O temp.zip
mkdir models
unzip temp.zip -d models
rm temp.zip
