#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


class dataCollector:
    def readfile(self, fileName):
        data = pd.read_csv(fileName)
        return data
