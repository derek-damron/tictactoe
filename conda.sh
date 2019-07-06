#!/usr/bin/sh

#####
#
# Must be executed from inside the high-level tictactoe folder
#
#####

conda env create --name tictactoe --file conda.yml
pip install ./