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
from go.go_game_models import GameActionObserver
from go.go_board import *

test_sgf_file = "test.sgf"

class GoGameTester(GameActionObserver):
    def __init__(self):
        self._board = TextGoBoard(BOARD_SIZE_19)
        try:
            self._game = GoGame(self)
            self._game.from_sgf(open(test_sgf_file).read())
            print "SGF recorded with %s %s by %s\n"\
                    "Event %s @ %s on %s\n"\
                    "Black: %s (%s), White %s (%s)\n" %\
                    (self._game.kifu_info.app_name,self._game.kifu_info.app_version,self._game.kifu_info.user,\
                    self._game.info.event, self._game.info.place, self._game.info.date,\
                    self._game.info.black_player_name, self._game.info.black_player_rank,self._game.info.white_player_name, self._game.info.white_player_rank)

            for i in range(0,50):
                self._game.next();
            self._board.toggle_number()
            self._board.show_board()
            for i in range(0,50):
                self._game.previous();
            self._board.show_board()
        except (SgfParseException,SgfTranslateException),ex:
            print "Sgf exception: ",ex

    def move_performed(self, move):
        self._board.add_stone(move.stone)
    def variation_available(self, moves):
        print "variation_available"
    def stones_added(self, stones):
        for stone in stones:
            self._board.add_stone(stone)
    def stones_removed(self, stones):
        for stone in stones:
            self._board.remove_stone(stone)
    def marks_added(self, marks):
        print "marks_added"
    def marks_removed(self, marks):
        print "marks_removed"

def main():
    tester = GoGameTester()

if __name__ == '__main__':
    main()
