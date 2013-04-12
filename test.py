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

class GoGameEventTester(GameActionObserver):
    def __init__(self):
        pass
    def move_performed(self, move):
        print "move_performed"
    def variation_available(self, moves):
        print "variation_available"
    def stone_added(self, stone, coord):
        print "stone_added"
    def stone_removed(self, stone, coord):
        print "stone_removed"
    def mark_added(self, mark):
        print "mark_added"
    def mark_removed(self, mark):
        print "mark_removed"

def main():
    try:
        game = GoGame(GoGameEventTester())
        game.from_sgf(open(test_sgf_file).read())
        print game.info.event,game.info.black_player_name,game.info.white_player_name,\
            game.kifu_info.app_name,game.kifu_info.app_version
    except (SgfParseException,SgfTranslateException),ex:
        print "Sgf exception: ",ex

if __name__ == '__main__':
    main()
