#! /bin/bash
#
# 193_Valid_Phone_Numbers.sh
# Copyright (C) 2016 yangchao <yangchao@Chaos-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.
#

sed -n -e '/^\(\([0-9]\{3\}\)-\|\(([0-9]\{3\})\s\)\)[0-9]\{3\}-[0-9]\{4\}$/p' 193_file.txt
