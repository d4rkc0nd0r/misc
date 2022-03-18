#!/bin/bash

# reverse dump
# this script converts the hex dump to raw bytes

filename="$1"

if [$filename == ""] ; then
	echo "No file supplied."
	echo "Usage: ./reverse_dump [filename]"

else
	xxd -r -p $filename >> firmware.bin
	exit 1
fi

exit 0
