#!/bin/bash

CURRENT_USER=$(whoami)
sudo mkdir -p $LOG_FOLDER
sudo chown $CURRENT_USER $LOG_FOLDER
sudo chmod 774 mkdir $LOG_FOLDER
