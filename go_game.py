#-------------------------------------------------------------------------------
# Name:        sgfparser / Go Game Models
# Purpose:
#
# Author:      Si Wei
#
# Created:     09/04/2013
# Copyright:   (c) Si Wei 2013
#-------------------------------------------------------------------------------

import utility

# ENUMS
GAME_RESULT_BASE       = 0
GAME_RESULT_DRAW          = GAME_RESULT_BASE + 1
GAME_RESULT_BLACK_WINS    = GAME_RESULT_BASE + 2
GAME_RESULT_WHITE_WINS    = GAME_RESULT_BASE + 3
GAME_RESULT_BLACK_RESIGNS = GAME_RESULT_BASE + 4
GAME_RESULT_WHITE_RESIGNS = GAME_RESULT_BASE + 5

# MODELS
class GoGame(BaseObject):
    '''A game model of Go'''
    def __init__(self):
        self.format = ""
        self.app_name = ""
        self.app_version = 0
        self.info = GoGameInfo()

class GoGameInfo(BaseObject):
    '''
    Information about a Go game
    See http://www.red-bean.com/sgf/user_guide/index.html
    '''
    def __init__(self):
        self.black_player_name = ""
        self.black_player_rank = ""
        self.black_team = ""
        self.white_player_name = ""
        self.white_player_rank = ""
        self.white_team = ""
        self.result = GoGameResult()
        self.komi = 0.0
        self.handicap = 0
        self.time = ""
        self.date = ""
        self.event = ""
        self.round = ""
        self.place = ""
        self.rules = ""
        self.game_name = ""
        self.opening = ""
        self.game_comment = ""
        self.source = ""
        self.user = ""
        self.annotation = ""
        self.copyright = ""

class GoGameResult(BaseObject):
    '''Result of a Go game, including winning party and score'''
    def __init__(self):
        self.fact = GAME_RESULT_BASE
        self.score = 0.0