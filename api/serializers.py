from rest_framework import serializers
from .models import Item, Location, Move, Pokemon, PokemonEggGroup, PokemonFormGeneration, PokemonMove, PokemonStat, PokemonType, Stat, Type, EggGroup


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

class PokemonEggGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonEggGroup
        fields = '__all__'

class PokemonFormGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonFormGeneration
        fields = '__all__'

class PokemonMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonMove
        fields = '__all__'

class PokemonStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonStat
        fields = '__all__'

class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = '__all__'

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class EggGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EggGroup
        fields = '__all__'
        
