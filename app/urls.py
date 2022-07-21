from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='indexfile'),
    path('sports', views.sports, name='sportsfile'),
    path('business', views.business, name='businessfile'),
    path('entertainment', views.entertainment, name='entertainmentfile'),
    path('politics', views.politics, name='politicsfile'),
    path('tech', views.tech, name='techfile'),
    path('startup', views.startup, name='startupfile'),
    path('world', views.world, name='worldfile'),
    path('national', views.national, name='nationalfile'),
    path('miscellaneous', views.miscellaneous, name='miscellaneousfile'),
    path('unconventional', views.hatke, name='hatkefile'),
    path('science', views.science, name='sciencefile'),
    path('automobile', views.automobile, name='automobilefile'),
]