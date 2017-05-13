from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from ..core.models import Program, Day
from ..users.models import User


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:program-detail')
    owner = serializers.HyperlinkedRelatedField(view_name='api:user-detail', read_only=True)

    class Meta:
        model = Program
        fields = ('id', 'url', 'owner', 'title', 'slug')


class DaySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Day

    nameservers = HyperlinkedIdentityField(
        view_name='domain-nameservers-list',
        lookup_url_kwarg='domain_pk'
    )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    programs = serializers.HyperlinkedRelatedField(view_name='api:program-detail', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_superuser', 'programs')
