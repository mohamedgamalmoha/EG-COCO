from drf_writable_nested.serializers import WritableNestedModelSerializer

from order.models import PackageOrder, CustomOrder
from accounts.api.serializers import CustomerSerializer


class PackageOrderSerializer(WritableNestedModelSerializer):
    customer = CustomerSerializer(allow_null=False, many=False)

    class Meta:
        model = PackageOrder
        exclude = ('created', 'updated')


class CustomOrderSerializer(WritableNestedModelSerializer):
    customer = CustomerSerializer(allow_null=False, many=False)

    class Meta:
        model = CustomOrder
        exclude = ('created', 'updated')
