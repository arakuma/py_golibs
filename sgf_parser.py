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
from sgf_models import *

class SgfParser(BaseObject):
# constructors
    def __init__(self):
        self._working_game = GoGame()
        self._curPos = 0
        self._working_sgf = ""

# public methods
    def read(self,sgf_text):
        '''
        Read in sgf format text and parse it to a GoGame model
        This will be done in three phases:
            1. Parse the sgf text to the game tree collection
            2. Visit all tree nodes and fill up game infomation
            3. Assign root node to GoGame's game start node then later it could
                be used for reviewing the game or directly go through the tree
        '''
        self._working_sgf = sgf_text
        self._working_game = GoGame()
        #1
        rootNode = self._parse_game_tree()
        #2 and #3
        self._fill_up_game(rootNode)
        return _working_game

    def write(self,game):
        '''
        Parse the GoGame model reversely to sgf_text
        '''
        return ""

# private methods / Go Game related
    def _fill_up_game(self,rootNode):
        pass

    def _extract_property(self,propertyNode):
        pass

# private methods / Sgf models parsing
    def _parse_game_tree(self):
        rootNode = SgfNode()
        return rootNode

    def _parse_node(self):
        pass

    def _parse_property(self):
        pass

# private methods / character processing
    def _accept_current(self):
        _curPos += 1

    def _accept_char(self,char):
        if _working_sgf[_curPos] == char:
            self._accept_current()
            return True
        return False

    def _accept_whitespaces(self):
        while(_working_sgf[_curPos] in string.whitespace):
            self._accept_current()

    def _test_char(self,prefix):
        self._accept_whitespaces()
        return _working_sgf[_curPos] == prefix

    def _test_pattern(self,pattern):
        self._accept_whitespaces()
        return pattern.match(_working_sgf[_curPos]
