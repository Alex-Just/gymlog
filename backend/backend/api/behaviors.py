from rest_framework import viewsets


class RetrievableByIdOrSlug(viewsets.ModelViewSet):
    def get_object(self):
        pk = self.kwargs.get('pk')

        try:
            pk_int = int(pk)
        except ValueError:
            pk_int = None

        # Allow to query objects by `id`
        obj = None
        if pk_int:
            obj = self.queryset.filter(id=pk_int).first()

        # Or by `slug`
        if not obj:
            obj = self.queryset.filter(slug=pk).first()

        return obj


class RetrievableByIdOrUsernameOrCurrent(viewsets.ModelViewSet):
    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == 'current':
            return self.request.user

        try:
            pk_int = int(pk)
        except ValueError:
            pk_int = None

        # Allow to query Users by `id`
        obj = None
        if pk_int:
            obj = self.queryset.filter(id=pk_int).first()

        # Or by `username`
        if not obj:
            obj = self.queryset.filter(username=pk).first()

        return obj
