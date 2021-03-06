from rest_framework import serializers

from core.serializers import APIModelSerializer, ModelSerializer
from authentication.models import User, UserType
from sales.models import Order

RelatedField = serializers.PrimaryKeyRelatedField


class UserTypeSerializer(ModelSerializer):

    class Meta:
        model = UserType
        fields = ('id', 'name')


class UserSerializer(APIModelSerializer):

    orders = RelatedField(queryset=Order.objects.all(), many=True, required=False)

    included_serializers = {
        'orders': 'sales.serializers.OrderSerializer',
        'associations': 'sales.serializers.AssociationSerializer',
    }

    def to_representation(self, instance) -> dict:
        data = super().to_representation(instance)
        data['is_admin'] = instance.is_admin
        return data

    class Meta:
        model = User
        fields = '__all__'
        # read_only_fields = tuple()
