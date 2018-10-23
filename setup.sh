#!/bin/bash

if [[ ! -e models ]]
then
	echo "Downloading facenet model..."
	mkdir models
	wget --content-disposition https://www.dropbox.com/s/sackvibhwzhn7jw/20180402-114759%20%282%29.zip?dl=1 -O temp.zip
	unzip temp.zip -d models
	rm temp.zip
else
	echo "Model directory already present. Skipping download."
fi

wget --content-disposition https://github.com/davidsandberg/facenet/archive/master.zip -O facenet.zip
unzip facenet.zip
rm facenet.zip
