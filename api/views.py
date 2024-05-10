from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import (
    Item, Location, Move, Pokemon, PokemonEggGroup,
    PokemonFormGeneration, PokemonMove, PokemonStat,
    PokemonType, Stat, Type, EggGroup
)
from .serializers import (
    ItemSerializer, LocationSerializer, MoveSerializer,
    PokemonSerializer, PokemonEggGroupSerializer,
    PokemonFormGenerationSerializer, PokemonMoveSerializer,
    PokemonStatSerializer, PokemonTypeSerializer,
    StatSerializer, TypeSerializer, EggGroupSerializer,
)


# Item views
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Location views
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated,)

# Move views
class MoveList(generics.ListCreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    permission_classes = (IsAuthenticated,)

class MoveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    permission_classes = (IsAuthenticated,)

# Pokemon views
class PokemonList(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = (IsAuthenticated,)

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = (IsAuthenticated,)

# PokemonEggGroup views
class PokemonEggGroupList(generics.ListCreateAPIView):
    queryset = PokemonEggGroup.objects.all()
    serializer_class = PokemonEggGroupSerializer
    permission_classes = (IsAuthenticated,)

class PokemonEggGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonEggGroup.objects.all()
    serializer_class = PokemonEggGroupSerializer
    permission_classes = (IsAuthenticated,)

# PokemonFormGeneration views
class PokemonFormGenerationList(generics.ListCreateAPIView):
    queryset = PokemonFormGeneration.objects.all()
    serializer_class = PokemonFormGenerationSerializer
    permission_classes = (IsAuthenticated,)

class PokemonFormGenerationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonFormGeneration.objects.all()
    serializer_class = PokemonFormGenerationSerializer
    permission_classes = (IsAuthenticated,)

# PokemonMove views
class PokemonMoveList(generics.ListCreateAPIView):
    queryset = PokemonMove.objects.all()
    serializer_class = PokemonMoveSerializer
    permission_classes = (IsAuthenticated,)

class PokemonMoveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonMove.objects.all()
    serializer_class = PokemonMoveSerializer
    permission_classes = (IsAuthenticated,)

# PokemonStat views
class PokemonStatList(generics.ListCreateAPIView):
    queryset = PokemonStat.objects.all()
    serializer_class = PokemonStatSerializer
    permission_classes = (IsAuthenticated,)

class PokemonStatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonStat.objects.all()
    serializer_class = PokemonStatSerializer
    permission_classes = (IsAuthenticated,)

# PokemonType views
class PokemonTypeList(generics.ListCreateAPIView):
    queryset = PokemonType.objects.all()
    serializer_class = PokemonTypeSerializer
    permission_classes = (IsAuthenticated,)

class PokemonTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PokemonType.objects.all()
    serializer_class = PokemonTypeSerializer
    permission_classes = (IsAuthenticated,)

# Stat views
class StatList(generics.ListCreateAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = (IsAuthenticated,)

class StatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    permission_classes = (IsAuthenticated,)

# Type views
class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (IsAuthenticated,)

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (IsAuthenticated,)

# EggGroup views
class EggGroupList(generics.ListCreateAPIView):
    queryset = EggGroup.objects.all()
    serializer_class = EggGroupSerializer

class EggGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EggGroup.objects.all()
    serializer_class = EggGroupSerializer
    permission_classes = (IsAuthenticated,)

