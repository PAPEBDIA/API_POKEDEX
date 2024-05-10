"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import (
    ItemList, ItemDetail,
    LocationList, LocationDetail,
    MoveList, MoveDetail,
    PokemonList, PokemonDetail,
    PokemonEggGroupList, PokemonEggGroupDetail,
    PokemonFormGenerationList, PokemonFormGenerationDetail,
    PokemonMoveList, PokemonMoveDetail,
    PokemonStatList, PokemonStatDetail,
    PokemonTypeList, PokemonTypeDetail,
    StatList, StatDetail,
    TypeList, TypeDetail,
    EggGroupList, EggGroupDetail,
)

urlpatterns = [
    # Item URLs
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),

    # Location URLs
    path('locations/', LocationList.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),

    # Move URLs
    path('moves/', MoveList.as_view(), name='move-list'),
    path('moves/<int:pk>/', MoveDetail.as_view(), name='move-detail'),

    # Pokemon URLs
    path('pokemon/', PokemonList.as_view(), name='pokemon-list'),
    path('pokemon/<int:pk>/', PokemonDetail.as_view(), name='pokemon-detail'),

    # PokemonEggGroup URLs
    path('pokemon-egg-groups/', PokemonEggGroupList.as_view(), name='pokemon-egg-group-list'),
    path('pokemon-egg-groups/<int:pk>/', PokemonEggGroupDetail.as_view(), name='pokemon-egg-group-detail'),

    # PokemonFormGeneration URLs
    path('pokemon-form-generations/', PokemonFormGenerationList.as_view(), name='pokemon-form-generation-list'),
    path('pokemon-form-generations/<int:pk>/', PokemonFormGenerationDetail.as_view(), name='pokemon-form-generation-detail'),

    # PokemonMove URLs
    path('pokemon-moves/', PokemonMoveList.as_view(), name='pokemon-move-list'),
    path('pokemon-moves/<int:pk>/', PokemonMoveDetail.as_view(), name='pokemon-move-detail'),

    # PokemonStat URLs
    path('pokemon-stats/', PokemonStatList.as_view(), name='pokemon-stat-list'),
    path('pokemon-stats/<int:pk>/', PokemonStatDetail.as_view(), name='pokemon-stat-detail'),

    # PokemonType URLs
    path('pokemon-types/', PokemonTypeList.as_view(), name='pokemon-type-list'),
    path('pokemon-types/<int:pk>/', PokemonTypeDetail.as_view(), name='pokemon-type-detail'),

    # Stat URLs
    path('stats/', StatList.as_view(), name='stat-list'),
    path('stats/<int:pk>/', StatDetail.as_view(), name='stat-detail'),

    # Type URLs
    path('types/', TypeList.as_view(), name='type-list'),
    path('types/<int:pk>/', TypeDetail.as_view(), name='type-detail'),

    # EggGroup URLs
    path('egg-groups/', EggGroupList.as_view(), name='egg-group-list'),
    path('egg-groups/<int:pk>/', EggGroupDetail.as_view(), name='egg-group-detail'),


]

