#!/usr/bin/env bash

./getlist.py $1 >> $1
./v2a.py -p $1
