from django.contrib import admin
from llamaland.hexgame.models import Player, Game, Match, GameMap, MatchMap, GameHex, MatchHex, GameTerrain, MatchTerrain, GameUnit, MatchUnit

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Match)
admin.site.register(GameMap)
admin.site.register(MatchMap)
admin.site.register(GameHex)
admin.site.register(MatchHex)
admin.site.register(GameTerrain)
admin.site.register(MatchTerrain)
admin.site.register(GameUnit)
admin.site.register(MatchUnit)
