# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        sgfparser / SGF Models
# Purpose:
#
# Author:      Si Wei
#
# Created:     09/04/2013
# Copyright:   (c) Si Wei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from utility import BaseObject

class SgfNode(BaseObject):
    '''Basic node of sgf format'''
    def __init__(self):
        self.index = 0       # pre-order recursion node index
        self.next = None     # another SgfNode
        self.variations = [] # if variations are available,
                             #    self.next will be variations[0][0]