file=seasonal/*.csv
for f in $file; do grep 2017-07 $f | tail -1; done
