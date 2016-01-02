#! /bin/bash
#
# 194_Transpose_File.sh
# Copyright (C) 2016 yangchao <yangchao@Chaos-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.
#


awk '
{ 
    for (i=1; i<=NF; i++)  {
        a[NR,i] = $i
    }
}
NF>p { p = NF }
END {    
    for(j=1; j<=p; j++) {
        str=a[1,j]
        for(i=2; i<=NR; i++){
            str=str" "a[i,j];
        }
        print str
    }
}' file.txt
