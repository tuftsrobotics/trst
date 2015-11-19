#/bin/bash

i=0 #i = run number
while [[ -e log/run/$i.log ]] ; do
    let i++
done
f=log/run/$i.log
touch f
echo "Starting run $i" > $f

