import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from peewee import *
import touchtimedb
import itertools


playerList = []
playerstats = {}
players = []
stats = []
categories = ['Player', 'Team','GP','W','L','MIN','PTS','TOUCHES','FrontCTTouches','TimeOfPoss','AvgSecPerTouch',
'AvgDribPerTouch', 'PTSPerTouch','ElbowTouches','PostTouches','PaintTouches','PTSPerElbowTouch','PTSPerPostTouch',
'PTSPerPaintTouch']
url = 'http://stats.nba.com/tracking/#!/player/possessions/?sort=TIME_OF_POSS&dir=1'
driver = webdriver.Chrome("/Users/Hallshit/Downloads/chromedriver")
driver.get(url)

playersd = driver.find_elements_by_css_selector('td.player.ng-scope')
for player in playersd:
    players.append(player.text)

statsd = driver.find_elements_by_css_selector('td.ng-binding')
for stat in statsd:
    stats.append(stat.text)


# categoriesd = driver.find_elements_by_css_selector('th.sortable.cf.ng-scope')
# for category in categoriesd:
#     category = category.text
#     category = category.replace('/n', '')
#     print category
#
#     categories.append(category)
#
#
# print categories
#
#
statmultiplier = 0
for player in players:
    for i, c in enumerate(categories):
        if c == 'Player':
            playerstats[c] = player
        else:
            playerstats[c] = stats[(i-1) + statmultiplier]

    playerList.append(playerstats)
    playerstats = {}
    statmultiplier += 18
#
#
#
#
for list in playerList:
    touchtimedb.Player.create(**list)
#
print "Done"
#








driver.close()