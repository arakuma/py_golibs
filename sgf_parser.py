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
    nodeIndex = 0
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
        SgfParser.nodeIndex = 0
        self._working_sgf = sgf_text
        #1
        rootNode = self._parse_game_tree()
        #2 and #3
        self._working_game = GoGame()
        self._fill_up_game(rootNode)
        return self._working_game

    def write(self,game):
        '''
        Parse the GoGame model reversely to sgf_text
        '''
        return ""

# private methods / Go Game related
    def _fill_up_game(self,rootNode):
        # basicly travel all nodes of all game trees
        #     and extract property values from nodes to fill up game info
        self._extract_game_info(rootNode)
        walkingNode = rootNode
        #while walkingNode.next is not None:
        #    walkingNode = rootNode.next

    def _extract_game_info(self,gameInfoNode):
        # I was thinking of building a dict for propIdent-game.attribute
        #     to make it look nicer than the if-else statements
        #     unluckily seems it's not easy to get attribute name as string
        kifuInfo = self._working_game.kifuInfo
        gameInfo = self._working_game.info
        for prop in gameInfoNode.properties:
            ident = prop.ident
            values = prop.values
            valuePair = values[0]
            simpleValue = valuePair.valueA
            if ident == PROP_PB:
                gameInfo.black_player_name = simpleValue
            elif ident == PROP_BR:
                gameInfo.black_player_rank = simpleValue
            elif ident == PROP_BT:
                gameInfo.black_team = simpleValue
            elif ident == PROP_PW:
                gameInfo.white_player_name = simpleValue
            elif ident == PROP_WR:
                gameInfo.white_player_rank = simpleValue
            elif ident == PROP_WT:
                gameInfo.white_team = simpleValue
            elif ident == PROP_RE:
                if simpleValue == PROP_VALUE_RESULT_DRAW:
                    gameInfo.result.type = GAME_RESULT_DRAW
                else:
                    m = re.match(PROP_VALUE_RESULT_RESIGN,simpleValue)
                    if m is not None:
                        gameInfo.result.type = GAME_RESULT_RESIGNS
                        if m.group(1) == PROP_VALUE_BLACK:
                            gameInfo.result.winning_party = GAME_STONE_WHITE
                        else:
                            gameInfo.result.winning_party = GAME_STONE_BLACK
                    else:
                        m = re.match(PROP_VALUE_RESULT_WIN)
                        if m is not None:
                            gameInfo.result.type = GAME_RESULT_WINS
                            gameInfo.result.winning_party = m.group(1)
                            gameInfo.result.score = float(group(2))
            elif ident == PROP_KM:
                gameInfo.komi = float(simpleValue)
            elif ident == PROP_HA:
                gameInfo.handicap = int(simpleValue)
            elif ident == PROP_TM:
                gameInfo.time = simpleValue
            elif ident == PROP_DT:
                gameInfo.date = simpleValue
            elif ident == PROP_EV:
                gameInfo.event = simpleValue
            elif ident == PROP_RO:
                gameInfo.round = simpleValue
            elif ident == PROP_PL:
                gameInfo.place = simpleValue
            elif ident == PROP_RU:
                gameInfo.rules = simpleValue
            elif ident == PROP_GN:
                gameInfo.game_name = simpleValuem
            elif ident == PROP_ON:
                gameInfo.opening = simpleValue
            elif ident == PROP_GC:
                gameInfo.game_comment = simpleValue
            elif ident == PROP_SO:
                gameInfo.source = simpleValue
            elif ident == PROP_US:
                gameInfo.user = simpleValue
            elif ident == PROP_AN:
                gameInfo.annotation = simpleValue
            elif ident == PROP_CP:
                gameInfo.copyright = simpleValue
            elif ident == PROP_AP:
                kifuInfo.app_name = valuePair.valueA
                kifuInfo.app_version = float(valuePair.valueB)
            elif ident == PROP_CA:
                kifuInfo.charset = simpleValue
            elif ident == PROP_FF:
                kifuInfo.format = int(simpleValue)
            elif ident == PROP_GM:
                kifuInfo.game = int(simpleValue)
            elif ident == PROP_ST:
                kifuInfo.game = int(simpleValue)
            elif ident == PROP_SZ:
                boardSize = BoardSize()
                if len(valuePair.valueB) > 0:
                    boardSize.col = int(valuePair.valueA)
                    boardSize.row = int(valuePair.valueB)
                else:
                    boardSize.col = int(simpleValue)
                    boardSize.row = int(simpleValue)
                kifuInfo.size = boardSize
            else:
                # unrecognized property ident
                Exception("game info fail: unrecognized prop ident ", ident)

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
            treeNode.index = SgfParser.nodeIndex
            SgfParser.nodeIndex += 1
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
            if self._test_char(CHAR_VALUE_END):
                # None
                self._move_next()
            else:
                propValue.valueA = self._parse_property_valuetype_value()
                # Compose    = ValueType ":" ValueType
                if self._accept_char(CHAR_COMPOSE_VALUE):
                    propValue.valueB = self._parse_property_valuetype_value()
                self._accept_char(CHAR_VALUE_END)
                if len(propValue.valueA) == 0 and len(propValue.valueB == 0):
                    propValue = None
        else:
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
        self._accept_whitespaces()
        if self._working_sgf[self._cur_pos] == char:
            self._move_next()
            return True
        return False

    def _accept_whitespaces(self):
        while self._working_sgf[self._cur_pos].isspace():
            self._move_next()

    def _test_char(self,prefix):
        self._accept_whitespaces()
        return self._working_sgf[self._cur_pos] == prefix

    def _test_pattern(self,pattern):
        self._accept_whitespaces()
        return pattern.match(self._working_sgf[self._cur_pos]) is not None
