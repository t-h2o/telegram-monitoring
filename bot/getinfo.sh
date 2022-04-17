#!/bin/bash

getinfo () {

#	stats	
	if [ $1 == "stats" ]; then
		fram=$(free -m | awk '$1 == "Mem:" {print $2}')
		uram=$(free -m | awk '$1 == "Mem:" {print $3}')
		echo "$(uptime -p)"
		echo "$uram MB on $fram MB of RAM"
	fi
	
#	who	
	if [ $1 == "who" ]; then
		echo "there is $(users | wc -w) connected :"
		echo "$(who)"
	fi

#	Disks	
	if [ $1 == "disk" ]; then
		fdisk=$(df -Bg | grep '^/dev/' | grep -v '/boot$' | awk '{ft += $2} END {print ft}')
		udisk=$(df -Bg | grep '^/dev/' | grep -v '/boot$' | awk '{ut += $3} END {print ut}')
		echo $udisk Gb used on $fdisk Gb
	fi

#	CPU	
	if [ $1 == "cpu" ]; then
		cpul=$(top -bn1	| \
		grep '^%Cpu'	| \
		cut -c 9-		| \
		xargs			| \
		awk '{printf("%.1f%%"), $1 + $3}')
		echo $cpul  CPU load
	fi
}

#	test if arguments
if [ -z $1 ]; then
	exit; fi
getinfo $1
