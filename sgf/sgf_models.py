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

from common.utility import BaseObject

class SgfNode(BaseObject):
    '''Basic node of sgf format'''
    def __init__(self):
        self.index      = 0     # pre-order recursion node index
        self.next       = None  # linked next SgfNode
        self.variations = []    # if variations are available,
                                #    self.next will be variations[0]
        self.properties = []    # list of SgfProperty
        self.is_root    = False

class SgfProperty(BaseObject):
    '''Property of sgf format'''
    def __init__(self):
        self.ident = ""
        self.values = []     # list of SgfPropertyValue

class SgfPropertyValue(BaseObject):
    '''Value of property'''
    def __init__(self):
        self.valueA = ""
        self.valueB = ""
