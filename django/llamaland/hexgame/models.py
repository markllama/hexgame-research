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
    game = models.ForeignKey(Game)
    match = models.ForeignKey(Match, null=True)
    size = models.CharField(max_length=7)
    origin = models.CharField(max_length=7)

    def __unicode__(self):
        return self.name

class Hex(models.Model):
    hx = models.IntegerField()
    hy = models.IntegerField()
    map = models.ForeignKey(Map)

    def __unicode__(self):
        return u"Hex(%d,%d)" % (self.hx, self.hy)
    
class Terrain(models.Model):
    name = models.CharField(max_length=30)    
    game = models.ForeignKey(Game)
    map = models.ForeignKey(Map)
    locations = models.ManyToManyField(Hex)

    def __unicode__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=30)    
    game = models.ForeignKey(Game)
    map = models.ForeignKey(Map)
    location = models.ForeignKey(Hex)

    def __unicode__(self):
        return self.name
