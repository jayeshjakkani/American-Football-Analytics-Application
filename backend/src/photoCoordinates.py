#!/usr/bin/env python3
# -*- coding: utf-8 -*-

  class photoCoordinates:
    allCoordinates = {}

#The positions with coordinates (0,0) were not available in experimental data. 
#Therefore, coordinates for those positions are yet not confirmed.
    kickoff_coordinates = {
        "R1": (20, 140),
        "R2": (65, 140),
        "R3": (110, 140),
        "R4": (155, 140),
        "R5" : (200, 140),
        "PK" : (245, 140),
        "L5" : (290, 140),
        "L4" : (335, 140),
        "L3" : (380, 140),
        "L2" : (425, 140),
        "L1" : (470, 140)
        }
    
    kickoff_return_coordinates = {
        "RF1" : (100,175),
        "RF2" : (100,380),
        "MF" : (100,525),
        "LF1" : (100,950),
        "LF2" : (100,875),
        "RM" : (630,400),
        "MM" : (630,650),
        "LM" : (630,900),
        "RB" : (830,400),
        "MB" : (830,650),
        "LB" : (830,900),
        "KR" : (1300,600),
        "KFB" : (1120,700)
        }
    
    punt_coordinates = {
        "GL" : (100,250),
        "P" : (620,525),
        "PPR" : (700,450),
        "PLW" : (450,350),
        "PLT" : (495,150),
        "PLG" : (560,150),
        "PLS" : (620,130),
        "PRG" : (700,150),
        "PRT" : (800,150),
        "PRW" : (800,330),
        "PC" : (570,380),
        "GR" : (1100,250)
        }
        
    punt_return_coordinates = {
        "VRo" : (0, 0),
        "VRi" : (0, 0),
        "PDR1" : (40, 300),
        "PDR2" : (40,375),
        "PLR" : (235,375),
        "PDR3" : (40,425),
        "PLM" : (0,0),
        "PDL3" : (40,500),
        "PDL2" : (40,575),
        "PDL1" : (100,685),
        "PLL" : (235,575),
        "VL" : (100,820),
        "PFB" : (0,0),
        "PR" : (700,540)
        }
    
    fieldgoal_coordinates = {
        "H" : (500, 475),
        "K" : (0,0),
        "FLW" : (210, 325),
        "FLE" : (280, 315),
        "FLT" : (350, 305),
        "FLG" : (400, 295),
        "FLS" : (455, 285),
        "FRG" : (505, 295),
        "FRT" : (555, 305),
        "FRE" : (605, 315),
        "FRW" : (660, 325)
        }
    
    fieldgoal_block_coordinates = {
        "FBR" : (700,150),
        "FBM" : (900,150),
        "FBL" : (1100,150),
        "FR1" : (450,450),
        "FR2" : (575,450),
        "FR3" : (660,450),
        "FR4" : (745,450),
        "FR5" : (830,450),
        "FL6" : (965,450),
        "FL5" : (1050,450),
        "FL4" : (1150, 450),
        "FL3" : (1240,450),
        "FL2" : (1325, 450),
        "FL1" : (1410,450)
        }
    
    def __init__(self):
        self.allCoordinates['KICKOFF'] = self.kickoff_coordinates
        self.allCoordinates['KICKOFF_RETURN'] = self.kickoff_return_coordinates
        self.allCoordinates['PUNT'] = self.punt_coordinates
        self.allCoordinates['PUNT_RETURN'] = self.punt_return_coordinates
        self.allCoordinates['FIELDGOAL'] = self.fieldgoal_coordinates
        self.allCoordinates['FIELDGOAL_BLOCK'] = self.fieldgoal_block_coordinates
