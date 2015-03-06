#!/usr/bin/env sh
python setup.py develop
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo
if [ "$1" == "remote" ] ; then
    REMOTE=true python -m unittest discover tests -v
else 
    python -m unittest discover tests -v
fi
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo
yes | pip uninstall yaaHN
