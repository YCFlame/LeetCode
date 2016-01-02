#! /bin/bash
#
# 192_Word_Frequency.sh
# Copyright (C) 2016 yangchao <yangchao@Chaos-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.
#


awk '
{
    for(i=1;i<=NF;i++) {
        a[$i]++
    } 
}
END {
    for(k in a) {
        print k,a[k]
    }
}' words.txt | sort -k 2 -n -r
