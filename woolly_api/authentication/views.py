from authentication.serializers import WoollyUserSerializer, WoollyUserTypeSerializer
from authentication.models import WoollyUserType, WoollyUser
from sales.models import AssociationMember
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework_json_api.views import RelationshipView


class WoollyUserViewSet(viewsets.ModelViewSet):
    """support Post request to create a new WoollyUser"""
    queryset = WoollyUser.objects.all()
    serializer_class = WoollyUserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(
            type_id=self.kwargs['woollyusertype_pk']
        )

    def get_queryset(self):
        queryset = self.queryset.filter(login=self.request.user.login)

        if 'woollyuser_pk' in self.kwargs:
            association_pk = self.kwargs['woollyuser_pk']
            queryset = queryset.filter(user__pk=association_pk)

        return queryset


class WoollyUserTypeViewSet(viewsets.ModelViewSet):
    queryset = WoollyUserType.objects.all()
    serializer_class = WoollyUserTypeSerializer

    def get_queryset(self):
        queryset = self.queryset

        # if this viewset is accessed via the 'association-detail' route,
        # it wll have been passed the `association_pk` kwarg and the queryset
        # needs to be filtered accordingly; if it was accessed via the
        # unnested '/portes' route, the queryset should include all Portes
        if 'itemspec_pk' in self.kwargs:
            itemspec_pk = self.kwargs['itemspec_pk']
            queryset = queryset.filter(specs__pk=itemspec_pk)

        if 'user_pk' in self.kwargs:
            user_pk = self.kwargs['user_pk']
            queryset = queryset.filter(users__pk=user_pk)

        return queryset


class WoollyUserRelationshipView(RelationshipView):
    queryset = WoollyUser.objects
