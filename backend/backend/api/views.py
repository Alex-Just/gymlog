from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .behaviors import RetrievableByIdOrSlug, RetrievableByIdOrUsernameOrCurrent, OwnedAndViewedByCurrentUser
from .serializers import ProgramSerializer, UserSerializer, DaySerializer
from ..core.models import Program, Day
from ..users.models import User


class ProgramViewSet(RetrievableByIdOrSlug,
                     OwnedAndViewedByCurrentUser,
                     viewsets.ModelViewSet):
    """
    This endpoint presents Programs.
    The **owner** of the Program may update or delete instances of the Program.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DayViewSet(viewsets.ViewSet):
    """
    This endpoint presents Days.
    The **owner** of the Day may update or delete instances of the Day.
    """
    queryset = Day.objects.all()

    def list(self, request, program_pk=None):
        queryset = self.queryset.filter(program=program_pk)
        serializer = DaySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, program_pk=None):
        queryset = self.queryset.get(pk=pk, program=program_pk)
        item = get_object_or_404(queryset, pk=pk)
        serializer = DaySerializer(item)
        return Response(serializer.data)


class UserViewSet(RetrievableByIdOrUsernameOrCurrent,
                  viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
