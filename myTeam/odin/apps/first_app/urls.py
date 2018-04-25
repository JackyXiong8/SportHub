from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^nba$', views.nbaindex),
    url(r'^mlb$', views.mlbindex),
    url(r'^nfl$', views.nflindex),
    url(r'^music$', views.music),
    url(r'^about$', views.about)
]