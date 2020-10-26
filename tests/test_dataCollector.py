from backend.src.dataCollector import dataCollector
import pandas
import pytest

data_collector = dataCollector()


def test_method():
  assert data_collector.readfile('https://github.com/jayeshjakkani/American-Football-Analytics-Application/blob/master/backend/src/NCSU.csv?raw=true') is not None
