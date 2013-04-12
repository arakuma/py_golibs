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

test_sgf_file = "test.sgf"

def main():
    try:
        game = GoGame()
        game.from_sgf(open(test_sgf_file).read())
        print game.info.event,game.info.black_player_name,game.info.white_player_name,\
            game.kifu_info.app_name,game.kifu_info.app_version
    except (SgfParseException,SgfTranslateException),ex:
        print "Sgf exception: ",ex

if __name__ == '__main__':
    main()
