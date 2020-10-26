from backend.src.playsSeperator import playsSeperator
from backend.src.dataCollector import dataCollector

data_collector = dataCollector()
data = data_collector.readfile("https://github.com/jayeshjakkani/American-Football-Analytics-Application/blob/master/backend/src/NCSU.csv")
play_separator = playsSeperator()
plays = play_separator.getDataframesByPlays("NCST", data,'Season','2019')

def test02():
  for k, v in plays.items():
    assert v is not None
