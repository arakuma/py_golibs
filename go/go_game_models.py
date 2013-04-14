#-------------------------------------------------------------------------------
# Name:        sgfparser / Go Game Models
# Purpose:
#
# Author:      Si Wei
#
# Created:     12/04/2013
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
        3.mark add/remove
        4.view zone change
    '''
    def move_performed(self, move):
        pass
    def variation_available(self, moves):
        pass
    def stones_added(self, stone):
        pass
    def stones_removed(self, stone):
        pass
    def marks_added(self, mark):
        pass
    def marks_removed(self, mark):
        pass
    def view_changed(self, points):
        pass
    def view_restored(self):
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
    def __init__(self, markType, coordFrom, coordTo = None, text = ""):
        self.type     = markType
        self.from_pos = coordFrom
        self.to_pos   = coordTo
        self.text     = text

class Stone(BaseObject):
    def __init__(self, color, coord):
        self.color = color # GAME_STONE_BASE
        self.coord = coord
        self.index = 0

class Move(BaseObject):
    def __init__(self, stone = None):
        self.number               = 0
        self.stone                = stone
        self.is_bad               = False
        self.is_doubtful          = False
        self.is_interesting       = False
        self.is_ko                = False
        self.is_tejitsu           = False
        self.time_left_black      = 0.0
        self.time_left_white      = 0.0
        self.moves_left_black     = 0
        self.moves_left_white     = 0
    def set_number(self,number):
        self.number = number
        self.stone.index = number

# Models / Go game actions
class Action(BaseObject):
    '''
    This is actually an internal class used by GoGame and SgfParser,
        all actions will be processed to events for upper level use.
    Basically an Action is converted from and only from one SgfNode
        and all properties in SgfNode will be translated to attributes of Action
    '''
    def __init__(self, observer, name = ""):
        self._observer      = observer
        self.name           = name
        self.marks          = []
        # Action should be a double-linked node because it should be possible to
        #     go forward/wind back during review
        self.previous       = None
        self.next           = None
        self.variations     = []    # list of Actions
        self.comment        = ""
        self.is_hotspot     = False
        self.is_black_good  = False
        self.is_white_good  = False
        self.even_position  = 0.0
        self.is_unclear     = False
        self.value          = 0
        self.figure         = None
        self.view_points    = []
    def do(self):
        if len(self.view_points) == 0:
            self._observer.view_restored()
        else:
            self._observer.view_changed(self.view_points)
        if len(self.marks) > 0:
            self._observer.marks_added(self.marks)
        if len(self.variations) > 0:
            self._observer.variation_available(self.variations)
    def undo(self):
        if len(self.marks) > 0:
            self._observer.marks_removed(self.marks)

class MoveAction(Action):
    '''
    For prop B, W
    '''
    def __init__(self, observer, name = "", move = None):
        Action.__init__(self,observer,name)
        self.move = Move()
        if self.move is None: move = Move()
    def do(self):
        Action.do(self)
        self._observer.move_performed(self.move)
    def undo(self):
        Action.undo(self)
        self._observer.stones_removed([self.move.stone])

class SetupAction(Action):
    '''
    For prop AB, AW, AE, PL
    '''
    def __init__(self, observer, name = "", stones = None):
        Action.__init__(self,observer,name)
        self.stones         = stones
        self.player_to_move = GAME_STONE_BASE
        if self.stones is None: self.stones = []
    def do(self):
        Action.do(self)
        _observer.stone_added(self.stones)
    def undo(self):
        Action.undo(self)
        _observer.stones_removed(self.stones)

# Models / Go Game attributes
class GoGameSettings(BaseObject):
    def __init__(self):
        self.print_mode   = 0
        self.figure       = 0

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
