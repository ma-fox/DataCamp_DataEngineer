cp seasonal/s*.csv .
grep -h -v Tooth s*.csv > temp.csv
history | tail -n 3 > steps.txt
