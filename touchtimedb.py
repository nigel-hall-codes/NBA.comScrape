from peewee import *

db = SqliteDatabase('touchtime.db')

class TeamAbbrev(Model):
    teamId = IntegerField()
    abbreviation = TextField()
    teamName = TextField()
    simpleName = TextField()
    location = TextField()

    class Meta:
        database = db

class Player(Model):
    Player = TextField()
    Team = TextField()
    GP = FloatField()
    W = FloatField()
    L = FloatField()
    MIN = FloatField()
    PTS = FloatField()
    TOUCHES = FloatField()
    FrontCTTouches = FloatField()
    TimeOfPoss = FloatField()
    AvgSecPerTouch = FloatField()
    AvgDribPerTouch = FloatField()
    PTSPerTouch = FloatField()
    ElbowTouches = FloatField()
    PostTouches = FloatField()
    PaintTouches = FloatField()
    PTSPerElbowTouch = FloatField()
    PTSPerPostTouch = FloatField()
    PTSPerPaintTouch = FloatField()

    class Meta:
        database = db

class DefensiveZoneChart(Model):
    team = TextField()
    restM = FloatField()
    restA = FloatField()
    restP = FloatField()
    painM = FloatField()
    painA = FloatField()
    painP = FloatField()
    midrM = FloatField()
    midrA = FloatField()
    midrP = FloatField()
    leftM = FloatField()
    leftA = FloatField()
    leftP = FloatField()
    righM = FloatField()
    righA = FloatField()
    righP = FloatField()
    abovM = FloatField()
    abovA = FloatField()
    abovP = FloatField()

    class Meta:
        database = db


db.connect()
db.create_tables([Player, DefensiveZoneChart, TeamAbbrev], safe=True)

def changeabbre(orig, new):
    team = TeamAbbrev.get(TeamAbbrev.abbreviation == orig)
    team.abbreviation = new
    team.save()
    print 'done'

def checkabbrev(new):
    team = TeamAbbrev.get(TeamAbbrev.abbreviation == new)
    print team.teamName








