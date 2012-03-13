from django.db import models

# Create your models here.
class Player(models.Model):

    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Game(models.Model):

    name = models.CharField(max_length=30, unique=True)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    copyright = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Match(models.Model):
    game = models.ForeignKey(Game)
    players = models.ManyToManyField(Player)
    
    def __unicode__(self):
        return u"Match(%s)" % (self.game.name,)
    
class Map(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=7)
    origin = models.CharField(max_length=7)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class GameMap(Map):

    game = models.ForeignKey(Game)


class MatchMap(Map):

    match = models.ForeignKey(Match, null=True)


class Hex(models.Model):

    hx = models.IntegerField()
    hy = models.IntegerField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return u"Hex(%d,%d)" % (self.hx, self.hy)
    

class GameHex(Hex):
    map = models.ForeignKey(GameMap)

class MatchHex(Hex):
    map = models.ForeignKey(MatchMap)


class Terrain(models.Model):

    name = models.CharField(max_length=30)    

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class GameTerrain(Terrain):

    game = models.ForeignKey(Game)
    map = models.ForeignKey(GameMap)
    locations = models.ManyToManyField(GameHex)


class MatchTerrain(Terrain):

    match = models.ForeignKey(Match)
    map = models.ForeignKey(MatchMap)
    locations = models.ManyToManyField(MatchHex)

class Unit(models.Model):

    name = models.CharField(max_length=30)    

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class GameUnit(Unit):

    game = models.ForeignKey(Game)
    location = models.ForeignKey(GameHex)

class MatchUnit(Unit):

    match = models.ForeignKey(Match)
    location = models.ForeignKey(MatchHex)


