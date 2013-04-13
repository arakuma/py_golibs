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
from go_game_models import *

class GoBoard(BaseObject):
    def __init__(self,size):
        self._size        = size
        self._show_number = False
        self._show_coord  = True
        self._stones      = []
        self._marks       = []
        self._hoshi_list  = []
        self._cur_index   = 0
        for y in range(0,size):
            self._stones.append([])
            self._marks.append([])
            for x in range(0,size):
                self._stones[y].append(None)
                self._marks[y].append(None)
        if self._size == BOARD_SIZE_9:
            self._hoshi_list = BOARD_HOSHI_9
        elif self._size == BOARD_SIZE_13:
            self._hoshi_list = BOARD_HOSHI_13
        elif self._size == BOARD_SIZE_19:
            self._hoshi_list = BOARD_HOSHI_19
        self._init_board()
# public methods
    def add_stone(self,stone):
        if stone.index == 0:
            self._cur_index += 1
            stone.index = self._cur_index
        self._stones[stone.coord.x][stone.coord.y] = stone
    def remove_stone(self,stone):
        self._cur_index -= 1
        self._stones[stone.coord.x][stone.coord.y] = None
    def add_mark(self,mark):
        self._marks[mark.from_pos.x][mark.from_pos.y] = mark
    def remove_mark(self,mark):
        self._marks[mark.from_pos.x][mark.from_pos.y] = None
    def toggle_number(self):
        self._show_number = not self._show_number
    def toggle_coord(self):
        self._show_coord = not self._show_coord
# private methods
    def _redraw_board(self):
        self._draw_coords()
        self._draw_lines()
        #self._draw_stones()
# methods need to be overrided
    def show_board(self):
        pass
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
    Currently this board class is only for demostration
    marks are not supported yet (^ ^;)
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
    CHR_INTERSECTION       = '┼'
    CHR_HOSHI              = '•'
    '''
    CHR_STONE_BLACK        = 'B'
    CHR_STONE_WHITE        = 'W'
    CHR_BORDER_LEFT        = '+'
    CHR_BORDER_TOP         = '+'
    CHR_BORDER_RIGHT       = '+'
    CHR_BORDER_BOTTOM      = '+'
    CHR_LINE_H             = '-'
    CHR_LINE_V             = '|'
    CHR_CORNER_TL          = '+'
    CHR_CORNER_TR          = '+'
    CHR_CORNER_BR          = '+'
    CHR_CORNER_BL          = '+'
    CHR_INTERSECTION       = '+'
    CHR_HOSHI              = '*'
    CHR_COORD_BASE         = 'a'
    CHR_EMPTY              = ' '
    CHR_LF                 = '\n'

    PADDING                = 1
    MARGIN                 = 0
    COORD_WIDTH            = 1
    GRID_ORIGIN_X          = PADDING * 2 + MARGIN * 2 + COORD_WIDTH
    GRID_ORIGIN_Y          = PADDING + MARGIN + COORD_WIDTH
    ZOOM_FACTOR            = 1 # (ZOOM_FACTOR-1) CHR_LINEs should be added between two y-axis points
                               # CHR_LINE count of x-axis's should be doubled for a nicer look
                                                   #               /│\
    def __init__(self,size):                       #                │
        self._extra_line_times_y = self.ZOOM_FACTOR - 1 #           │
        self._extra_line_times_x = self._extra_line_times_y * 2  #──┘
        if self._extra_line_times_x == 0:
            self._extra_line_times_x = 1
        GoBoard.__init__(self,size)

    def add_stone(self,stone):
        GoBoard.add_stone(self,stone)
        self._draw_stone(stone)
    def remove_stone(self,stone):
        GoBoard.remove_stone(self,stone)
        self._draw_grid_symbol(stone.coord.x,stone.coord.y,self.CHR_INTERSECTION)
    def add_mark(self,mark):
        GoBoard.add_mark(self,mark)
    def remove_mark(self,mark):
        GoBoard.remove_mark(self,mark)
    def toggle_number(self):
        GoBoard.toggle_number(self,stone)
    def toggle_coord(self):
        GoBoard.toggle_coord(self,stone)
    def show_board(self):
        for i in range(0,len(self._board[0])):
            line = ""
            for j in range(0,len(self._board)):
                line += self._board[j][i]
            print line

    def _init_board(self):
        self._board = []
        boardWidth  = self.GRID_ORIGIN_X+self._size+self._extra_line_times_x*(self._size-1)+self.COORD_WIDTH+self.MARGIN*2+self.PADDING*2
        boardHeight = self.GRID_ORIGIN_Y+self._size+self._extra_line_times_y*(self._size-1)+self.COORD_WIDTH+self.MARGIN+self.PADDING
        for x in range(0,boardWidth):
            self._board.append([])
            for y in range(0,boardHeight):
                self._board[x].append(self.CHR_EMPTY)
        self._redraw_board()

    def _draw_coords(self):
        hBottomY = self.GRID_ORIGIN_Y + self._extra_line_times_y * (self._size - 1) + self._size + self.PADDING
        vRightX  = self.GRID_ORIGIN_X + self._extra_line_times_x * (self._size - 1) + self._size + self.PADDING * 2
        for i in range(0,self._size):
            # h-coords
            coord_text = self.CHR_EMPTY
            if self._show_coord:
                coord_text = chr(ord(self.CHR_COORD_BASE)+i)
            hX = self.GRID_ORIGIN_X + self._extra_line_times_x * i + i
            self._board[hX][self.MARGIN] = coord_text
            self._board[hX][hBottomY] = coord_text
            # v-coords
            vY = self.GRID_ORIGIN_Y + self._extra_line_times_y * i + i
            self._board[self.MARGIN * 2][vY] = coord_text
            self._board[vRightX][vY] = coord_text

    def _draw_lines(self):
        # corners
        self._draw_grid_symbol(0,0,self.CHR_CORNER_TL)
        self._draw_grid_symbol(self._size-1,0,self.CHR_CORNER_TR)
        self._draw_grid_symbol(0,self._size-1,self.CHR_CORNER_BL)
        self._draw_grid_symbol(self._size-1,self._size-1,self.CHR_CORNER_BR)
        # borders & lines
        for i in range(1,self._size-1):   # two corners should be excluded
            # h-borders
            self._draw_grid_symbol(i,0,self.CHR_BORDER_TOP)
            self._draw_grid_symbol(i,self._size-1,self.CHR_BORDER_TOP)
            # v-borders
            self._draw_grid_symbol(0,i,self.CHR_BORDER_LEFT)
            self._draw_grid_symbol(self._size-1,i,self.CHR_BORDER_RIGHT)
            for j in range(1,self._size-1):
                # intersections
                intersectionSymbol = self.CHR_INTERSECTION
                if (i,j) in self._hoshi_list:
                    # hoshi point
                    intersectionSymbol = self.CHR_HOSHI
                self._draw_grid_symbol(i,j,intersectionSymbol)
        # extra padding between lines
        for i in range(0,self._size-1):
            for j in range(0,self._size):
                x = self.GRID_ORIGIN_X + self._extra_line_times_x * i + i + 1
                y = self.GRID_ORIGIN_Y + self._extra_line_times_y * j + j
                # h-extra-lines
                for k in range(0,self._extra_line_times_x):
                    self._board[x+k][y] = self.CHR_LINE_H
                # v-extra-lines
                for k in range(j+1,j+1+self._extra_line_times_y):
                    self._board[i][k] = self.CHR_LINE_V

    def _draw_stones(self):
        for x in range(0,len(self._stones)):
            stoneSeq = self._stones[x]
            for y in range(0,len(stoneSeq)):
                if not self._stones[x][y] is None:
                    self._draw_stone(self._stones[x][y])

    def _draw_stone(self,stone):
        stoneSymbol = self.CHR_INTERSECTION
        if self._show_number:
            stoneSymbol = str(stone.index)
        else:
            if stone.color == GAME_STONE_BLACK:
                stoneSymbol = self.CHR_STONE_BLACK
            elif stone.color == GAME_STONE_WHITE:
                stoneSymbol = self.CHR_STONE_WHITE
        self._draw_grid_symbol(stone.coord.x,stone.coord.y,stoneSymbol)

    def _draw_grid_symbol(self,x,y,symbol):
        '''
        This method is for grid origin translation because:
            1.margin/padding and the coord itself will affect on the start point of grid in board matrix
            2.zoom factor and extra line padding for x-axis
        '''
        x = self.GRID_ORIGIN_X + self._extra_line_times_x * x + x
        y = self.GRID_ORIGIN_Y + self._extra_line_times_y * y + y
        try:
            self._board[x][y] = symbol
        except:
            print x,",",y,",",symbol
