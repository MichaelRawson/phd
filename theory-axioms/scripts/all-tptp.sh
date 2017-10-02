#!/bin/sh

find $1 -name "*.p" | grep "=" | parallel --plus --jobs 8 ./tptp.sh $1 $2 {} {#} {##}
