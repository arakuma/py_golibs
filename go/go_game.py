#-------------------------------------------------------------------------------
# Name:        sgfparser / Go Game Models
# Purpose:
#
# Author:      Si Wei
#
# Created:     09/04/2013
# Copyright:   (c) Si Wei 2013
#-------------------------------------------------------------------------------

from common.utility import BaseObject
from go_defs import *

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

# Models / Basic structures
class Coordinate(BaseObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class FigureInfo(BaseObject):
    def __init__(self, options, name):
        self.options = options
        self.name = name

class Mark(BaseObject):
    def __init__(self, markType, fromX, fromY, toX = 0, toY = 0, text = ""):
        self.type     = markType
        self.from_pos = Coordinate(fromX,fromY)
        self.to_pos   = Coordinate(toX,toY)
        self.text     = text

class Stone(BaseObject):
    def __init__(self, color):
        self.color = color # GAME_STONE_BASE

class Move(BaseObject):
    def __init__(self, stone, x, y, comment = "", figure = None):
        self.stone         = stone
        self.position      = Coordinate(x,y)
        self.comment       = ""
        self.figure        = figure
        self.value         = 0
        self.is_black_good = False
        self.is_white_good = False
        self.is_hotspot    = False

# Models / Go game actions
class Action(BaseObject):
    '''
    This is actually an internal class used by GoGame and SgfParser,
        all actions will be processed to events for upper level use.
    Basically an Action is converted from and only from one SgfNode
        and all properties in SgfNode will be parsed to attributes in Action.
    '''
    def __init__(self, name, marks = None):
        self.name     = name
        self.marks    = marks
        # Action should be a double-linked node because it should be possible to
        #     go forward/wind back during review
        self.previous = None
        self.next     = None

class MoveAction(Action):
    def __init__(self, name, move, marks = None):
        super.__init__(name,marks)
        self.move = move

class StoneAction(Action):
    def __init__(self, name, stones, marks = None):
        super.__init__(name,marks)
        self.stones = stones

# Models / Go game itself
class GoGame(BaseObject):
    '''A game model of Go'''
    def __init__(self):
        self.kifuInfo  = KifuInfo()
        self.info      = GoGameInfo()
        self.settings  = GoGameSettings()

class GoGameSettings(BaseObject):
    def __init__(self):
        self.print_mode   = 0

class KifuInfo(BaseObject):
    def __init__(self):
        self.format       = 0
        self.app_name     = ""
        self.app_version  = 0
        self.charset      = ""
        self.style        = 0
        self.size         = None
        self.game         = 0

class BoardSize(BaseObject):
    def __init__(self):
        self.row = 0
        self.col = 0

class GoGameResult(BaseObject):
    '''Result of a Go game, including winning party and score'''
    def __init__(self):
        self.type          = GAME_RESULT_BASE
        self.winning_party = GAME_STONE_BASE
        self.score         = 0.0

class GoGameInfo(BaseObject):
    '''
    Information about a Go game
    See http://www.red-bean.com/sgf/user_guide/index.html
    '''
    def __init__(self):
        self.black_player_name = ""
        self.black_player_rank = ""
        self.black_team        = ""
        self.white_player_name = ""
        self.white_player_rank = ""
        self.white_team        = ""
        self.result            = GoGameResult()
        self.komi              = 0.0
        self.handicap          = 0
        self.time              = ""
        self.date              = ""
        self.event             = ""
        self.round             = ""
        self.place             = ""
        self.rules             = ""
        self.game_name         = ""
        self.opening           = ""
        self.game_comment      = ""
        self.source            = ""
        self.user              = ""
        self.annotation        = ""
        self.copyright         = ""
