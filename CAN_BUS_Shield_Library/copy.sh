#!/bin/bash

#copy.sh
#this script copies necessary files from this folder to the arduino library on
#   located in the applications folder, has absolute path hard coded in
#   from path is relative to this file's running

export arduino_lib_path="/Applications/Arduino.app/Contents/Resources/Java/libraries/CAN_BUS_Shield_Library"

echo $arduino_lib_path
cp mcp_can.h mcp_can.cpp mcp_can_dfs.h $arduino_lib_path

################################################################################
# END OF FILE
################################################################################
