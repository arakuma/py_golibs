# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Test Module
# Purpose:
#
# Author:      Si Wei
#
# Created:     10/04/2013
# Copyright:   (c) Si Wei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from go.go_game import *
from sgf.sgf_parser import *

test_sgf_file = "test.sgf"

def main():
    sgfParser = SgfParser()
    try:
        game = sgfParser.read(open(test_sgf_file).read())
        print game.info.event,game.info.black_player_name,game.info.white_player_name,\
            game.kifuInfo.app_name,game.kifuInfo.app_version
    except (SgfParseException,SgfTranslateException),ex:
        print "Sgf exception: ",ex

if __name__ == '__main__':
    main()
