#! /usr/bin/env bash
d="$(pwd)"
cmd="0 1 * * * cd $d && python2 sumpocket.py"
user="$(whoami)"
(crontab -l -u "$user"; echo "$cmd") | crontab -u "$user" -
