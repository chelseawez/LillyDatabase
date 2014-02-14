#!/bin/bash
dir=`dirname $0`
cd $dir
psql -af drop.sql mysite
psql -af create.sql mysite
psql -af load.sql mysite
