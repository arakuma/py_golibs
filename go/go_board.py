# -*- coding: utf-8 -*-
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
from go_defs import *

class GoBoard(BaseObject):
    def __init__(self,size):
        self._size        = size
        self._show_number = False
        self._show_coord  = False
        self._stones      = []
        self._marks       = []
        for y in range(0,size):
            self._stones.append([])
            self._marks.append([])
            for x in range(0,size):
                self._stones[y].append(None)
                self._marks[y].append(None)
        self._init_board()
# public methods
    def add_stone(self,stone):
        self._stones[stone.coord.x][stone.coord.y] = stone
        self._draw_board()
    def remove_stone(self,stone):
        self._stones[stone.coord.x][stone.coord.y] = None
        self._draw_board()
    def add_mark(self,mark):
        self._marks[mark.from_pos.x][mark.from_pos.y] = mark
        self._draw_board()
    def remove_mark(self,mark):
        self._marks[mark.from_pos.x][mark.from_pos.y] = None
        self._draw_board()
    def toggle_number(self):
        self._show_number = not self._show_number
        self._draw_board()
    def toggle_coord(self):
        self._show_coord = not self._show_coord
        self._draw_board()
# private methods
    def _draw_board(self):
        self._draw_coords()
        self._draw_lines()
        self._draw_stones()
# methods need to be overrided
    def _init_board(self):
        pass
    def _draw_coords(self):
        pass
    def _draw_lines(self):
        pass
    def _draw_stones(self):
        pass
    def _draw_marks(self):
        pass

class TextGoBoard(GoBoard):
    '''
    Currently this board class is only for demostration,
        that's why padding/margin value are not configurable,
        so is the zoom factor (for board size).
        They are hardcoded: padding=0, margin=0, zoom_factor=1
    And marks are not supported (^ ^;)
    Example:
                 a b c d e f g h i--\
          a      ┌─┬─┬─┬─┬─┬─┬─┬─┐a  \
          b      ├─┼─┼─┼─┼─┼─┼─┼─┤b   \
          c      ├─┼─•─┼─┼─┼─☻─┼─┤c\   \
          d      ├─┼─☺─┼─┼─☻─☺─☻─┤d \   \
          e      ├─┼─┼─┼─☻─┼─☺─☺─┤e  \---\--> h/v coords
          f      ├─┼─☻─┼─┼─┼─┼─┼─┤f
          g      ├─┼─•─┼─┼─☺─•─┼─┤g
          h      ├─┼─┼─┼─┼─┼─┼─┼─┤h
          i      └─┴─┴─┴─┴─┴─┴─┴─┘i
                 a b c d e f g h i
    \_  _/ \_  _/\______  _______/
      \/     \/         \/
    margin padding     grid
    \_____________  ______________/
                  \/
                 board = grid + coord + padding + margin
    '''
    CHR_STONE_BLACK        = '☻'
    CHR_STONE_WHITE        = '☺'
    CHR_BORDER_LEFT        = '├'
    CHR_BORDER_TOP         = '┬'
    CHR_BORDER_RIGHT       = '┤'
    CHR_BORDER_BOTTOM      = '┴'
    CHR_LINE_H             = '─'
    CHR_LINE_V             = '│'
    CHR_CORNER_TL          = '┌'
    CHR_CORNER_TR          = '┐'
    CHR_CORNER_BR          = '┘'
    CHR_CORNER_BL          = '└'
    CHR_POINT              = '┼'
    CHR_COORD_BASE         = 'a'
    CHR_HOSHI              = '•'
    CHR_EMPTY              = ' '
    CHR_LF                 = '\n'

    PADDING                = 0
    MARGIN                 = 0
    COORD_WIDTH            = 1
    GRID_ORIGIN            = PADDING + MARGIN + COORD_WIDTH
    ZOOM_FACTOR            = 1 # (ZOOM_FACTOR-1) CHR_LINEs should be added between two y-axis points
                               # CHR_LINE count of x-axis's should be doubled for a nicer look

    def __init__(self,size):
        GoBoard.__init__(self,size)
        self._grid_offset_x = GRID_ORIGIN + (ZOOM_FACTOR*2-1)*(self._size-2)
        self._grid_offset_y = GRID_ORIGIN + (ZOOM_FACTOR-1)*(self._size-2)

    def _init_board(self):
        self._board = []
        for y in range(0,self.GRID_ORIGIN+self._size+2):
            self._board.append([])
            for x in range(0,self.GRID_ORIGIN+self._size*2+1):
                self._board[y].append(self.CHR_EMPTY)
            self._board[y].append(self.CHR_LF) # an extra space for new line

    def _draw_board(self):
        GoBoard._draw_board(self)
        print self._board

    def _draw_coords(self):
        for i in range(0,self._size):
            # h-coords
            coord_text = self.CHR_EMPTY
            if self._show_coord:
                coord_text = chr(ord(self.CHR_COORD_BASE)+i)
            self._board[i*2+1][0] = coord_text
            self._board[i*2+1][self._size+2] = coord_text
            # v-coords
            self._board[0][i+1] = coord_text
            self._board[self._size*2][i+1] = coord_text

    def _draw_lines(self):
        # corners
        self._draw_grid_symbol(0,0,self.CHR_CORNER_TL)
        self._draw_grid_symbol(0,0,self.CHR_CORNER_TL)
        self._draw_grid_symbol(0,0,self.CHR_CORNER_TL)
        self._draw_grid_symbol(0,0,self.CHR_CORNER_TL)
        self._board[1][1]                     = self.CHR_CORNER_TL
        self._board[self._size*2][1]          = self.CHR_CORNER_TR
        self._board[1][self._size]            = self.CHR_CORNER_BL
        self._board[self._size*2][self._size] = self.CHR_CORNER_BR
        # borders
        for i in range(1,self._size-1):   # two corners should be excluded
            # h-borders
            self._board[i*2+1][1] = self.CHR_BORDER_TOP
            self._board[i*2+1][self._size] = self.CHR_BORDER_BOTTOM
            self._board[i*2][1] = self.CHR_LINE_H
            self._board[i*2][1] = self.CHR_LINE_V
            if i == self._size - 2:
                # last pos of h-border
                self._board[i*2+2][1] = self.CHR_LINE_H
                self._board[i*2+2][self._size] = self.CHR_LINE_V
            # v-borders
        # lines
        for i in range(0,self._size):
            # h-lines

            # v-lines
            pass

    def _draw_stones(self):
        pass

    def _draw_grid_symbol(self,x,y,symbol):
        '''
        This method is for grid origin translation because:
            1.margin/padding and the coord itself will affect on the start point of grid in board matrix
            2.x-axis needs extra padding for a nicer look
        '''
        x += self.GRID_ORIGIN8
        y += self.GRID_ORIGIN + (ZOOM_FACTOR-1)
        self._board[x][y] = symbol
