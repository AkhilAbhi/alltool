#!/bin/bash

cd /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
echo -e "PS1='\$' " > bash.bashrc
