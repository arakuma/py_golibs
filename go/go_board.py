#-------------------------------------------------------------------------------
# Name:        Go Board
# Purpose:
#
# Author:      Si Wei
#
# Created:     12/04/2013
# Copyright:   (c) Si Wei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from common.utility import BaseObject

class GoBoard(BaseObject):
    def add_stone(self,x,y):
        pass
    def remove_stone(self,x,y):
        pass
    def _draw_board(self):
        pass
    def _draw_h_coords(self):
        pass
    def _draw_lines(self):
        pass

class TextGoBoard(GoBoard):
    pass