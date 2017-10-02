#!/bin/sh

find $1 -name "*.smt2" | parallel --plus --jobs 8 ./smtlib.sh $1 $2 {} {#} {##}
