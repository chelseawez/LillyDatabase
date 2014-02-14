#!/bin/bash
dir=`dirname $0`
cd $dir
psql -f drop.sql
