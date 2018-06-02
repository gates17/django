from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = [
            'url',
            'id',
            'date_created',
        ]
        read_only_fields = ['id']

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_order_url(request=request)

    def validate_title(self, value):
        qs = Order.objects.filter(name__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This order has already been used")
        return value