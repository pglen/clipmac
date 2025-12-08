#!/bin/bash

# Pack current project. Will back out from dir and create archive

CURR=$(grep VERSION clipmac.py | awk -F '=' {'print $2'} | \
                    awk -F '"' {'print $2'})
#echo $CURR ; exit
FNAME=clipmac-$CURR.tgz
#echo $FNAME ; exit
if [ -f ../$FNAME ] ; then
    echo File ../$FNAME exists. Please delete first.
    exit
fi
pushd `pwd` >/dev/null
cd ..
echo "Packing / Archiving project '$FNAME'"
tar cfz $FNAME clipmac
popd >/dev/null

# EOF
