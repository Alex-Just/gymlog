from rest_framework import permissions, viewsets

from .behaviors import RetrievableByIdOrSlug, RetrievableByIdOrUsernameOrCurrent
from .serializers import ProgramSerializer, UserSerializer
from ..core.models import Program
from ..users.models import User


class ProgramViewSet(RetrievableByIdOrSlug, viewsets.ModelViewSet):
    """
    This endpoint presents Goals.
    The **owner** of the Goal may update or delete instances of the Goal.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Program.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(RetrievableByIdOrUsernameOrCurrent, viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
