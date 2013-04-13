#-------------------------------------------------------------------------------
# Name:        sgfparser / Go Game Definitions
# Purpose:
#
# Author:      Si Wei
#
# Created:     09/04/2013
# Copyright:   (c) Si Wei 2013
#-------------------------------------------------------------------------------

# enumerations
GAME_RESULT_BASE    = 0
GAME_RESULT_DRAW    = GAME_RESULT_BASE + 1
GAME_RESULT_WINS    = GAME_RESULT_BASE + 2
GAME_RESULT_RESIGNS = GAME_RESULT_BASE + 3

GAME_STONE_BASE     = 10
GAME_STONE_EMPTY    = GAME_STONE_BASE  + 1
GAME_STONE_BLACK    = GAME_STONE_BASE  + 2
GAME_STONE_WHITE    = GAME_STONE_BASE  + 3
GAME_STONE_INVALID  = GAME_STONE_BASE  + 4 # for captured point

GAME_MARK_BASE      = 50
GAME_MARK_ARROW     = GAME_MARK_BASE   + 1
GAME_MARK_CIRCLE    = GAME_MARK_BASE   + 2
GAME_MARK_LABEL     = GAME_MARK_BASE   + 3
GAME_MARK_LINE      = GAME_MARK_BASE   + 4
GAME_MARK_X         = GAME_MARK_BASE   + 5
GAME_MARK_SELECTED  = GAME_MARK_BASE   + 6
GAME_MARK_SQUARE    = GAME_MARK_BASE   + 7
GAME_MARK_TRIANGLE  = GAME_MARK_BASE   + 8
GAME_MARK_DIM       = GAME_MARK_BASE   + 9
GAME_MARK_UNDIM     = GAME_MARK_BASE   + 10

# constants
BOARD_SIZE_9        = 9
BOARD_SIZE_13       = 13
BOARD_SIZE_19       = 19
BOARD_HOSHI_9       = [(2,2),(6,2),(2,6),(6,6)]
BOARD_HOSHI_13      = [(3,3),(9,3),(6,6),(3,9),(9,9)]
BOARD_HOSHI_19      = [(3,3),(9,3),(15,3),(3,9),(9,9),(15,9),(3,15),(9,15),(15,15)]