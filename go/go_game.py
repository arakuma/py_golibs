#-------------------------------------------------------------------------------
# Name:        sgfparser / Go Game
# Purpose:
#
# Author:      Si Wei
#
# Created:     09/04/2013
# Copyright:   (c) Si Wei 2013
#-------------------------------------------------------------------------------

from common.utility import BaseObject
from go_defs import *
from go_game_models import *
from sgf.sgf_parser import *

# Models / Game observer
class GameActionObserver:
    '''
    Interface for being notified about all game actions:
        1.stone add/remove
        2.action performed
        3.mark add
    '''
    def move_performed(self, move):
        pass
    def variation_available(self, moves):
        pass
    def stone_added(self, stone, coord):
        pass
    def stone_removed(self, stone, coord):
        pass
    def mark_added(self, mark):
        pass
    def mark_removed(self, mark):
        pass

# constants
PROP_IDENTS_MOVE = [PROP_B, PROP_W]
PROP_IDENTS_SETUP = [PROP_AB, PROP_AW, PROP_AE, PROP_VW, PROP_PL]

# Models / Go game itself
class GoGame(BaseObject):
    '''A game model of Go'''
# constructor
    def __init__(self):
        self.kifu_info  = KifuInfo()
        self.info       = GoGameInfo()
        self.settings   = GoGameSettings()
        self.sgf_parser = SgfParser()
        self._init_default_info()

# public methods
    def from_sgf(self,sgfText):
        '''
        This will be done in three phases:
        1. Get the sgf game trees' root node
        2. Visit all tree nodes and fill up game infomation, basically the
            root node will be read and properties of it are used
        3. Convert sgf models to go game models for upper level uses,
            here we should travel game trees and read out all other nodes,
            fill up go game models with node properties and so on
        '''
        #1
        rootNode = self.sgf_parser.read(sgfText)
        #2
        self._process_game_info(rootNode)
        #3
        self._process_game_actions(rootNode)

    def to_sgf(self):
        '''
        Convert the game back to sgf root node and pass it to sgf parser
        '''
        return self.sgf_parser.write(self._get_sgf_root_node())

    def next(self):
        '''
        Go to the next action, corresponding events will be triggered
        '''
        pass

    def previous(self):
        '''
        Go back to previous action, corresponding events will be triggered
        '''
        pass

# private methods / Game actions
    def _add_action(self, action):
        pass

# private methods / Game info and actions from/to sgf
    def _get_sgf_root_node(self):
        return None

    def _init_default_info(self):
        self.kifu_info.format = PROP_VALUE_FILE_FORMAT
        self.kifu_info.app_name = ""
        self.kifu_info.app_version = 0
        self.kifu_info.charset = ""
        self.kifu_info.style = PROP_VALUE_STYLE_CHILDREN + PROP_VALUE_STYLE_MARK
        boardSize = BoardSize()
        boardSize.col = PROP_VALUE_BOARD_SIZE_GO
        boardSize.row = PROP_VALUE_BOARD_SIZE_GO
        self.kifu_info.size = boardSize
        self.kifu_info.game = PROP_VALUE_GAME_GO
        self.settings.print_mode = PROP_VALUE_PRINT_MODE_AS_IS

    def _process_game_info(self,rootNode):
        # I was thinking of building a dict for propIdent-game.attribute
        #     to make it look nicer than the if-else statements
        #     unluckily seems it's not easy to get attribute name as string
        kifuInfo = self.kifu_info
        gameInfo = self.info
        settings = self.settings
        for prop in rootNode.properties:
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
            elif ident == PROP_FG:
                settings.figure_options = int(simpleValue)
            elif ident == PROP_PM:
                settings.print_mode = int(simpleValue)
            else:
                # unrecognized property ident
                raise SgfTranslateException("unrecognized root prop ident " + ident)

    def _process_game_actions(self,node):
        # basicly travel all nodes of all game trees
        #     and extract properties from nodes to fill up game models
        walkingNode = node
        # sgf.node <-> gogame.action
        while walkingNode is not None:
            print walkingNode.properties[0].ident + "[" + walkingNode.properties[0].values[0].valueA + "],",
            # node properties
            if not node.isRoot:
                action = self._get_action_from_node(walkingNode)
            if len(walkingNode.variations) > 0:
                # variations here is treated with recursion
                for variationRootNode in walkingNode.variations:
                    self._process_game_actions(variationRootNode)
                # and in this case walking node will no necessary to be here
                #     any longer
                walkingNode = None
            else:
                walkingNode = walkingNode.next

    def _get_action_from_node(self,node):
        '''
        Convert one sgf node to a single action of go game
        '''
        action = MoveAction()
        # Will B/W/VW props always be the first one of the node?
        # Actually no...but we must be sure action is constructed in time before
        #     any other props are translated to attribute of it.
        # So the first time of ieteration is for identifying the action type
        for prop in node.properties:
            if prop.ident in PROP_IDENTS_MOVE:
                action = MoveAction()
            elif prop.ident in PROP_IDENTS_SETUP:
                action = SetupAction()
        # OK, take the second time of properties iteration for translating
        for prop in node.properties:
            ident = prop.ident
            values = prop.values
            simpleValue = values[0].valueA
            # move
            if ident == PROP_B or ident == PROP_W:
                if ident == PROP_B:
                    action.move.stone = GAME_STONE_BLACK
                elif ident == PROP_W:
                    action.move.stone = GAME_STONE_WHITE
                action.move.position = self._coord_from_lc_letters(simpleValue)
            elif ident == PROP_BL:
                action.move.time_left_black = float(simpleValue)
            elif ident == PROP_WL:
                action.move.time_left_white = float(simpleValue)
            elif ident == PROP_BM:
                action.move.is_bad = bool(simpleValue)
            elif ident == PROP_DO:
                action.move.is_doubtful = bool(simpleValue)
            elif ident == PROP_IT:
                action.move.is_interesting = bool(simpleValue)
            elif ident == PROP_KO:
                action.move.is_ko = bool(simpleValue)
            elif ident == PROP_MN:
                action.move.number = int(simpleValue)
            elif ident == PROP_OB:
                action.move.moves_left_black = int(simpleValue)
            elif ident == PROP_OW:
                action.move.moves_left_white = int(simpleValue)
            elif ident == PROP_TE:
                action.move.is_tejitsu = bool(simpleValue)
            # mutual
            elif ident == PROP_C:
                pass
            elif ident == PROP_GB:
                pass
            elif ident == PROP_GW:
                pass
            elif ident == PROP_V:
                pass
            elif ident == PROP_HO:
                pass
            elif ident == PROP_FG:
                pass
            elif ident == PROP_DM:
                pass
            # marks
            elif ident == PROP_AR:
                for value in values:
                    arrowMark = Mark(GAME_MARK_ARROW,\
                        self._coord_from_lc_letters(value.valueA),\
                        self._coord_from_lc_letters(value.valueB))
                    action.marks.append(arrowMark)
            elif ident == PROP_DD:
                if len(simpleValue) == 0:
                    action.marks.append(Mark(GAME_MARK_UNDIM, None))
                else:
                    expanedValues = self._expand_composed_value(prop)
                    for value in values:
                        dimMark = Mark(GAME_MARK_DIM,\
                            self._coord_from_lc_letters(value.valueA))
                        action.marks.append(dimMark)
            elif ident == PROP_CR:
                for value in values:
                    circleMark = Mark(GAME_MARK_CIRCLE,\
                        self._coord_from_lc_letters(value.valueA))
                    action.marks.append(circleMark)
            elif ident == PROP_LB:
                for value in values:
                    labelMark = Mark(GAME_MARK_LABEL,\
                        self._coord_from_lc_letters(value.valueA),\
                        value.valueB)
                    action.marks.append(labelMark)
            elif ident == PROP_LN:
                for value in values:
                    lineMark = Mark(GAME_MARK_LINE,\
                        self._coord_from_lc_letters(value.valueA),\
                        self._coord_from_lc_letters(value.valueB))
                    action.marks.append(lineMark)
            elif ident == PROP_MA:
                for value in values:
                    xMark = Mark(GAME_MARK_X,\
                        self._coord_from_lc_letters(value.valueA))
                    action.marks.append(xMark)
            elif ident == PROP_SL:
                for value in values:
                    selectedMark = Mark(GAME_MARK_SELECTED,\
                        self._coord_from_lc_letters(value.valueA))
                    action.marks.append(selectedMark)
            elif ident == PROP_SQ:
                for value in values:
                    squareMark = Mark(GAME_MARK_SQUARE,\
                        self._coord_from_lc_letters(value.valueA))
                    action.marks.append(squareMark)
            elif ident == PROP_TR:
                for value in values:
                    triangleMark = Mark(GAME_MARK_SQUARE,\
                        self._coord_from_lc_letters(value.valueA))
                    action.marks.append(triangleMark)
            # stones setup
            elif ident == PROP_AB or ident == PROP_AW or ident == PROP_AE:
                pass
            elif ident == PROP_PL:
                pass
            elif ident == PROP_UC:
                pass
            elif ident == PROP_PM:
                pass
            elif ident == PROP_N:
                pass
            elif ident == PROP_VW:
                pass
            else:
                raise SgfTranslateException("unrecognized action prop ident " + ident)
        return action

#private methods / helpers
    def _coord_from_lc_letters(self,value):
        '''
        Convert coord value to Coordinate
        See http://www.red-bean.com/sgf/go.html
        Now only lower case letters are supported
            which lead to max board size to 26*26
        '''
        if len(value) == 0 or value == PROP_VALUE_MOVE_PASS_COORD:
            return None

        baseCoordValue = ord('a')
        charX, charY = value[0],value[1]
        if charX.isupper() or charY.isupper():
            raise SgfPropValueException("not supported upper case letters for coord")
        coord = Coordinate()
        coord.x = ord(charX) - baseCoordValue
        coord.y = ord(charY) - baseCoordValue
        return coord

    def _lc_letters_from_coord(self,coord):
        '''
        Convert Coordinate back to lower case letters
        '''
        baseCoordValue = ord('a')
        return chr(coord.x + baseCoordValue) + chr(coord.y + baseCoordValue)

    def _expand_composed_value(self,prop):
        expandedValues = []
        '''
        Expand any composed value likes [ca:ce] to [ca][cb][cc][cd][ce]
        for DD and VW
        '''
        for value in prop.values:
            if len(value.valueB) == 0:
                expandedValues.append(value)
            else:
                vs,ve = value.valueA, value.valueB
                for i in range(ord(vs[0]),ord(ve[0]) + 1):
                    for j in range(ord(vs[1]),ord(ve[1]) + 1):
                        newValue = SgfPropertyValue()
                        newValue.valueA = chr(i)+chr(j)
                        expandedValues.append(newValue)
        return expandedValues

