#!/bin/sh

docker run -it -p 8888:8888 -v $(pwd):/notebooks/host tensorflow/tensorflow
