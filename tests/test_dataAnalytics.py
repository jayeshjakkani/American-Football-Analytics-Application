from backend.src.dataAnalytics import dataAnalytics
from backend.src.playsSeperator import playsSeperator
from backend.src.dataCollector import dataCollector
import warnings
import pytest
warnings.simplefilter(action='ignore', category=FutureWarning)


da = dataAnalytics()
dc = dataCollector()
data = dc.readfile("https://github.com/jayeshjakkani/American-Football-Analytics-Application/blob/master/backend/src/NCSU.csv")
ps = playsSeperator()
all_plays = ps.getDataframesByPlays("NCST", data, "Season", "2019")
offensive_plays = {"PUNT", "KICKOFF_RETURN", "FIELDGOAL"}
defensive_plays = {"PUNT_RETURN", "KICKOFF", "FIELDGOAL_BLOCK"}


def test03():
  for playType, playData in all_plays.items():

    if playType in offensive_plays:
      formations = playData["pff_OFFPLAYERS"]
      ratings = playData["pff_OFFPLAYERSRATINGS"]

    elif playType in defensive_plays:
      formations = playData["pff_DEFPLAYERS"]
      ratings = playData["pff_DEFPLAYERSRATINGS"]

    countsAndRatings = da.generateTotalCountsAndRatings(formations, ratings)

    assert countsAndRatings is not None

