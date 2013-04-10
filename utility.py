# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Utilities
# Purpose:
#
# Author:      Si Wei
#
# Created:     17/01/2013
# Copyright:   (c) Si Wei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Class definitions
class BaseObject(object):
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            return name + ' not found!'

#Enumeration simulation
def Enum( *sequential, **named ):
    enums = dict( zip( sequential, range( len( sequential ) ) ), **named )
    return type( "Enum", (), enums )