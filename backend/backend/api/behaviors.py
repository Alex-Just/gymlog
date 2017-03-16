from rest_framework import viewsets
from rest_framework.exceptions import NotFound


class RetrievableByIdOrSlug(viewsets.ModelViewSet):
    def get_object(self):
        pk = self.kwargs.get('pk')

        try:
            pk_int = int(pk)
        except ValueError:
            pk_int = None

        queryset = self.get_queryset()

        # Allow to query objects by `id`
        obj = None
        if pk_int:
            obj = queryset.filter(id=pk_int).first()

        # Or by `slug`
        if not obj:
            obj = queryset.filter(slug=pk).first()

        if obj:
            return obj

        raise NotFound()


class RetrievableByIdOrUsernameOrCurrent(viewsets.ModelViewSet):
    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == 'current':
            return self.request.user

        try:
            pk_int = int(pk)
        except ValueError:
            pk_int = None

        queryset = self.get_queryset()

        # Allow to query Users by `id`
        obj = None
        if pk_int:
            obj = queryset.filter(id=pk_int).first()

        # Or by `username`
        if not obj:
            obj = queryset.filter(username=pk).first()

        if obj:
            return obj

        raise NotFound()


class OwnedAndViewedByCurrentUser(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
