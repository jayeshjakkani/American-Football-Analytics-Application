#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class playsSeperator:
    def getDataframesByPlays(self, team, data, filtertype, filtervalue):
        if(filtertype == "Month"):
            extract = data["pff_GAMEDATE"].iloc[0]
            extract_month = extract.split("-")
            if(int(extract_month[1]) == filtervalue):
                data = data[(data["pff_GAMEDATE"] == extract)]
        elif(filtertype == "Season"):
        	data = data[(data["pff_GAMESEASON"] == filtervalue)]
        elif(filtertype == "Week"):
            data = data[(data["pff_WEEK"] == filtervalue)]
        elif(filtertype == "Match"):
            data = data[(data["pff_GAMEID"] == filtervalue)]
        elif(filtertype == "Opponent"):
            data1 = data[(data["pff_DEFTEAM"] == filtervalue)]
            data2 = data[(data["pff_OFFTEAM"] == filtervalue)]
            data = pd.concat([data1, data2])
        p = data[(data["pff_SPECIALTEAMSTYPE"] == "PUNT") & (data["pff_OFFTEAM"] == team)]
        kor = data[(data["pff_SPECIALTEAMSTYPE"] == "KICKOFF") & (data["pff_OFFTEAM"] == team)]
        pr = data[(data["pff_SPECIALTEAMSTYPE"] == "PUNT") & (data["pff_DEFTEAM"] == team)]
        ko = data[(data["pff_SPECIALTEAMSTYPE"] == "KICKOFF") & (data["pff_DEFTEAM"] == team)]
        epfg = data[(data["pff_SPECIALTEAMSTYPE"] == "EXTRA POINT") | (data["pff_SPECIALTEAMSTYPE"] == "FIELD GOAL")]
        fg = epfg[epfg["pff_OFFTEAM"] == team]
        fgb = epfg[epfg["pff_DEFTEAM"] == team]
        dict = {"PUNT": p,
                "KICKOFF_RETURN": kor,
                "PUNT_RETURN": pr,
                "KICKOFF": ko,
                "FIELDGOAL": fg,
                "FIELDGOAL_BLOCK": fgb}
        return dict
