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
from common_defs import *
from string import whitespace

class SgfParser(BaseObject):
# constructors
    def __init__(self):
        self._working_game = GoGame()
        self._cur_pos = 0
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
        return self._working_game

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
        # Collection = GameTree { GameTree }
        treeRootNode = None
        # GameTree   = "(" Sequence { GameTree } ")"
        if self._accept_char(CHAR_TREE_BEGIN):
            treeRootNode = self._parse_node()
            # Sequence   = Node { Node }
            currentNode = treeRootNode
            nextNode = self._parse_node()
            while nextNode is not None:
                currentNode.next = nextNode
                currentNode = nextNode
                nextNode = self._parse_node()
            # GameTree   = "(" Sequence { GameTree } ")"
            subTreeRootNode = self._parse_game_tree()
            while subTreeRootNode is not None:
                currentNode.variations.append(subTreeRootNode)
                subTreeRootNode = self._parse_game_tree()
            if len(currentNode.variations) > 0:
                currentNode.next = currentNode.variations[0]
            self._accept_char(CHAR_TREE_END)
        return treeRootNode

    def _parse_node(self):
        treeNode = None
        # Node       = ";" { Property }
        if self._accept_char(CHAR_NODE_PREFIX):
            treeNode = SgfNode()
            prop = self._parse_property()
            while prop is not None:
                treeNode.properties.append(prop)
                prop = self._parse_property()
        return treeNode

    def _parse_property(self):
        # Property   = PropIdent PropValue { PropValue }
        prop = SgfProperty()
        # PropIdent  = UcLetter { UcLetter }
        while self._test_pattern(VTP_UCLETTER):
            prop.ident += self._move_next()
        # PropValues
        value = self._parse_property_value()
        while value is not None:
            prop.values.append(value)
            value = self._parse_property_value()
        # be sure property is filled up properly
        if len(prop.ident) == 0 or len(prop.value) == 0:
            prop = None
        return prop

    def _parse_property_value(self):
        # CValueType = (ValueType | Compose)
        propValue = SgfPropertyValue()
        # PropValue  = "[" CValueType "]"
        if self._accept_char(CHAR_VALUE_BEGIN):
            propValue.valueA = self._parse_property_valuetype_value()
            # Compose    = ValueType ":" ValueType
            if self._accept_char(CHAR_COMPOSE_VALUE):
                propValue.valueB = self._parse_property_valuetype_value()
            self._accept_char(CHAR_VALUE_END)
        if len(propValue.valueA) == 0:
            propValue = None
        return propValue

    def _parse_property_valuetype_value(self):
        simpleValue = ""
        curText = self._working_sgf[self._cur_pos:]
        # use the longest result of all results from ValueType patterns
        longestMatch = None
        for pattern in VT_PATTERNS:
            match = pattern.match(curText)
            if match is not None:
                if longestMatch is not None:
                    if len(match.group(0)) > len(longestMatch.group(0)):
                        longestMatch = match
                else:
                    longestMatch = match
        if longestMatch is not None:
            for i in range(0,len(longestMatch.group(0))):
                simpleValue += self._move_next()
        # FF[4] Section 3.3:
        # Formatting: linebreaks preceded by a "\" are converted to "",
        #   i.e. they are removed (same as Text type). All other linebreaks are
        #   converted to space (no newline on display!!).
        simpleValue = ' '.join(simpleValue.split())
        return simpleValue

# private methods / character processing
    def _move_next(self):
        curChar = self._working_sgf[self._cur_pos]
        self._cur_pos += 1
        return curChar

    def _accept_char(self,char):
        try:
            self._accept_whitespaces()
            if self._working_sgf[self._cur_pos] == char:
                self._move_next()
                return True
            return False
        except:
            print len(self._working_sgf),self._cur_pos

    def _accept_whitespaces(self):
        while self._working_sgf[self._cur_pos].isspace():
            self._move_next()

    def _test_char(self,prefix):
        self._accept_whitespaces()
        return self._working_sgf[self._cur_pos] == prefix

    def _test_pattern(self,pattern):
        self._accept_whitespaces()
        return pattern.match(self._working_sgf[self._cur_pos]) is not None
