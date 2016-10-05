from touchtimedb import *
from peewee import *
from playhouse.shortcuts import model_to_dict
import json
from collections import OrderedDict

import pandas as pd
import numpy as np
from pandas.io import sql
import sqlite3
import matplotlib.pyplot as plt


con = sqlite3.connect("touchtime.db")
df = pd.read_sql_query("SELECT * from DefensiveZoneChart", con)
df2 = pd.read_csv('FanDuel-NBA-2016-10-04-16525-players-list.csv')

def worstRest(feat):
    list = []
    teams = df.sort_values(feat).head().team

    for team in teams:
        list.append(team)
    return list

# verify that result of SQL query is stored in the dataframe
def findPlayers():
    playersList = OrderedDict()
    targets = {}
    feats = ['restP', 'painP', 'midrP', 'leftP', 'righP', 'abovP']
    for feat in feats:
        targets[feat] = worstRest(feat)

    for i, d in enumerate(df2.Opponent):
        opp = TeamAbbrev.get(TeamAbbrev.abbreviation == d).teamName
        for feat in feats:
            if (opp in targets[feat]) == True:
                name = df2.iloc[[i]]['First Name'].values + " " + df2.iloc[[i]]['Last Name'].values
                name = str(name)[2:-2]

                playersList[str(name)] = feat
    return playersList



players = findPlayers()

for player in players:
    print player, players[player]


con.close()








