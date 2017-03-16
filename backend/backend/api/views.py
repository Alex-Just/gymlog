from rest_framework import viewsets

from .behaviors import RetrievableByIdOrSlug, RetrievableByIdOrUsernameOrCurrent, OwnedAndViewedByCurrentUser
from .serializers import ProgramSerializer, UserSerializer
from ..core.models import Program
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


class UserViewSet(RetrievableByIdOrUsernameOrCurrent,
                  viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
