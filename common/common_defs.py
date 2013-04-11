# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        sgfparser / Common Definitions
# Purpose:
#
# Author:      Si Wei
#
# Created:     09/04/2013
# Copyright:   (c) Si Wei 2013
#-------------------------------------------------------------------------------

import re

# character constants
CHAR_TREE_BEGIN     = "("
CHAR_TREE_END       = ")"
CHAR_VALUE_BEGIN    = "["
CHAR_VALUE_END      = "]"
CHAR_NODE_PREFIX    = ";"
CHAR_COMPOSE_VALUE  = ":"

# sgf value type patterns
# see http://www.red-bean.com/sgf/sgf4.html
VTP_UCLETTER   = re.compile("^[A-Z]")
VTP_DIGIT      = re.compile("^\d")
VTP_NONE       = re.compile("^")
VTP_NUMBER     = re.compile("^[+-]?\d+")
VTP_REAL       = re.compile("^\d(.\d+)?")
VTP_DOUBLE     = re.compile("^[12]")
VTP_COLOR      = re.compile("^[BW]")
VTP_SIMPLETEXT = re.compile("^([^:\]\\\\]|\.)*")
VTP_TEXT       = re.compile("^([^:\]\\\\]|\.)*")
VTP_POINT      = re.compile("^[a-zA-Z]{2}")
VTP_MOVE       = re.compile("^[a-zA-Z]{2}")
VTP_STONE      = re.compile("^[BW]")
# ValueType  = (None | Number | Real | Double | Color | SimpleText | Text | Point  | Move | Stone)
VT_PATTERNS    = [VTP_NUMBER,VTP_REAL,VTP_DOUBLE,VTP_COLOR,VTP_SIMPLETEXT,VTP_TEXT,VTP_POINT,VTP_TEXT,VTP_STONE]

# sgf properties definition
# see http://www.red-bean.com/sgf/proplist_t.html
## move
PROP_B           = "B"    #Black
PROP_BL          = "BL"   #Black time left
PROP_BM          = "BM"   #Bad move
PROP_DO          = "DO"   #Doubtful
PROP_IT          = "IT"   #Interesting
PROP_KO          = "KO"   #Ko
PROP_MN          = "MN"   #set MoveNumber
PROP_OB          = "OB"   #OtStones Black
PROP_OW          = "OW"   #OtStones White
PROP_TE          = "TE"   #Tesuji
PROP_W           = "W"    #White
## setup
PROP_WL          = "WL"   #White time left
PROP_AB          = "AB"   #Add Black
PROP_AE          = "AE"   #Add Empty
PROP_AW          = "AW"   #Add White
PROP_PL          = "PL"   #Player to play
## -
PROP_AR          = "AR"   #Arrow
PROP_C           = "C"    #Comment
PROP_CR          = "CR"   #Circle
PROP_DD          = "DD"   #Dim points
PROP_DM          = "DM"   #Even position
PROP_FG          = "FG"   #Figure
PROP_GB          = "GB"   #Good for Black
PROP_GW          = "GW"   #Good for White
PROP_HO          = "HO"   #Hotspot
PROP_LB          = "LB"   #Label
PROP_LN          = "LN"   #Line
PROP_MA          = "MA"   #Mark
PROP_N           = "N"    #Nodename
PROP_PM          = "PM"   #Print move mode
PROP_SL          = "SL"   #Selected
PROP_SQ          = "SQ"   #Square
PROP_TR          = "TR"   #Triangle
PROP_UC          = "UC"   #Unclear pos
PROP_V           = "V"    #Value
PROP_VW          = "VW"   #View
## root
PROP_AP          = "AP"   #Application
PROP_CA          = "CA"   #Charset
PROP_FF          = "FF"   #Fileformat
PROP_GM          = "GM"   #Game
PROP_ST          = "ST"   #Style
PROP_SZ          = "SZ"   #Size
## game-info
PROP_AN          = "AN"   #Annotation
PROP_BR          = "BR"   #Black rank
PROP_BT          = "BT"   #Black team
PROP_CP          = "CP"   #Copyright
PROP_DT          = "DT"   #Date
PROP_EV          = "EV"   #Event
PROP_GC          = "GC"   #Game comment
PROP_GN          = "GN"   #Game name
PROP_ON          = "ON"   #Opening
PROP_OT          = "OT"   #Overtime
PROP_PB          = "PB"   #Player Black
PROP_PC          = "PC"   #Place
PROP_PW          = "PW"   #Player White
PROP_RE          = "RE"   #Result
PROP_RO          = "RO"   #Round
PROP_RU          = "RU"   #Rules
PROP_SO          = "SO"   #Source
PROP_TM          = "TM"   #Timelimit
PROP_US          = "US"   #User
PROP_WR          = "WR"   #White rank
PROP_WT          = "WT"   #White team
## Go (GM[1]) specific properties
PROP_TB          = "TB"   #Territory Black
PROP_TW          = "TW"   #Territory White
PROP_HA          = "HA"   #Handicap
PROP_KM          = "KM"   #Komi
## Lines of Action (GM[9]) specific properties
PROP_AS          = "AS"   #Who adds stones
PROP_IP          = "IP"   #Initial pos.
PROP_IY          = "IY"   #Invert Y-axis
PROP_SE          = "SE"   #Markup
PROP_SU          = "SU"   #Setup type

# property values
PROP_VALUE_BLACK          = "B"
PROP_VALUE_WHITE          = "W"
PROP_VALUE_RESULT_DRAW    = "0"
PROP_VALUE_RESULT_RESIGN  = "^([BW])\+R(esign)?$"
PROP_VALUE_RESULT_WIN     = "^([BW])\+(\d+(.\d+)?)$"
PROP_VALUE_GAME_GO        = "1"
PROP_VALUE_BOARD_SIZE_GO  = 19
PROP_VALUE_STYLE_CHILDREN = 0
PROP_VALUE_STYLE_SIBLINGS = 1
PROP_VALUE_STYLE_MARK     = 0
PROP_VALUE_STYLE_NO_MARK  = 2
PROP_VALUE_FILE_FORMAT    = 4
