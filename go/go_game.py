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

# ENUMS
GAME_RESULT_BASE    = 0
GAME_RESULT_DRAW    = GAME_RESULT_BASE + 1
GAME_RESULT_WINS    = GAME_RESULT_BASE + 2
GAME_RESULT_RESIGNS = GAME_RESULT_BASE + 3
GAME_STONE_BASE     = 10
GAME_STONE_BLACK    = GAME_STONE_BASE  + 1
GAME_STONE_WHITE    = GAME_STONE_BASE  + 2

# MODELS
class GoGame(BaseObject):
    '''A game model of Go'''
    def __init__(self):
        self.kifuInfo  = KifuInfo()
        self.info      = GoGameInfo()
        self.settings  = GoGameSettings()

class GoGameSettings(BaseObject):
    def __init__(self):
        self.figure_options = 0
        self.print_mode     = 0

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