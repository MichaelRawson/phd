#!/bin/sh

name=$(echo $3 | sed -e "s:^$1::; s:.smt2$::; s:.fof$::; s:/:_:g")

if [ -f $2/$name.proof ];
then
        echo "[-] ($4/$5)\t $name"
        exit 0
fi

vampire --mode casc --input_syntax smtlib2 --time_limit 2 --forced_options proof=on $3 > $2/$name.proof
if [ $? = "0" ];
then
	echo "[✔] ($4/$5)\t $name"
else
	rm $2/$name.proof
	echo "[✘] ($4/$5)\t $name"
fi
