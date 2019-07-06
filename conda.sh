#!/usr/bin/sh

#####
#
# Must be executed from inside the high-level tictactoe folder
#
# Possible args:
# build: Build from scratch
# update: Update current build
#
#####

if [ "$1" == "build" ]; then
    # Build from scratch
    echo "Building from scratch"
    conda env create --name tictactoe --file conda.yml
elif [ "$1" == "update" ]; then
    # Update
    echo "Updating existing build"
    conda env update --name tictactoe --file conda.yml
else
    # Error
    echo "ERROR: Unrecognized argument '$1', use 'build' or 'update'" 1>&2
    exit 1 # terminate and indicate error
fi

# Install local tictactoe
pip install ./
