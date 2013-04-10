# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Sgf parser
# Purpose:
#
# Author:      Si Wei
#
# Created:     10/04/2013
# Copyright:   (c) Si Wei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from utility import BaseObject
from go_game import *

class SgfParser(BaseObject):
    def __init__(self):
        self._working_game = GoGame()
        self._curPos = 0
        self._working_sgf = ""

    def read(self,sgf_text):
        self._working_sgf = sgf_text
        self._working_game = GoGame()

    def write(self,game):
        pass

    def _accept_current(self):
        _curPos += 1

    def _accept_char(self,char):
        if _working_sgf[_curPos] == char:
            self._accept_current()

    def _accept_whitespaces(self):
        while(_working_sgf[_curPos] in string.whitespace):
            self._accept_current()

    def _test_char(self,prefix):
        self._accept_whitespaces()
        return _working_sgf[_curPos] == prefix

    def _test_pattern(self,pattern):
        self._accept_whitespaces()
        return pattern.match(_working_sgf[_curPos]
