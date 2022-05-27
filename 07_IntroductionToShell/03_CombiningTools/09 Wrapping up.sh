wc -l seasonal/*
wc -l seasonal/* | grep -v total
wc -l seasonal/* | grep -v total | sort -n | head -n 1
