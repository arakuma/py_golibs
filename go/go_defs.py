#-------------------------------------------------------------------------------
# Name:        sgfparser / Go Game Definitions
# Purpose:
#
# Author:      Si Wei
#
# Created:     09/04/2013
# Copyright:   (c) Si Wei 2013
#-------------------------------------------------------------------------------

# ENUMS
GAME_RESULT_BASE    = 0
GAME_RESULT_DRAW    = GAME_RESULT_BASE + 1
GAME_RESULT_WINS    = GAME_RESULT_BASE + 2
GAME_RESULT_RESIGNS = GAME_RESULT_BASE + 3
GAME_STONE_BASE     = 10
GAME_STONE_EMPTY    = GAME_STONE_BASE  + 1
GAME_STONE_BLACK    = GAME_STONE_BASE  + 2
GAME_STONE_WHITE    = GAME_STONE_BASE  + 3
GAME_MARK_BASE      = 50
GAME_MARK_ARROW     = GAME_MARK_BASE   + 1
GAME_MARK_CIRCLE    = GAME_MARK_BASE   + 2
GAME_MARK_LABEL     = GAME_MARK_BASE   + 3
GAME_MARK_LINE      = GAME_MARK_BASE   + 4
GAME_MARK_X         = GAME_MARK_BASE   + 5
GAME_MARK_SELECTED  = GAME_MARK_BASE   + 6
GAME_MARK_SQUARE    = GAME_MARK_BASE   + 7
GAME_MARK_TRIANGLE  = GAME_MARK_BASE   + 8