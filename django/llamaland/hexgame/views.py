# Create your views here.
from django.views.generic.base import TemplateView


from django.views.generic import ListView

from hexgame.models import Game

class GameListView(ListView):
    context_object_name = "game_list"
    queryset = Game.objects
    template_name = 'game_list.html'

    #def get_context(self, **kwargs):
    #    return {"name": "game_list" }

class MapListView(TemplateView):

    template_name = 'map_list.html'

    def get_context(self, **kwargs):
        return {"name": "maplist" }

