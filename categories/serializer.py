from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = [
            'url',
            'id',
            'name',
        ]
        read_only_fields = ['id']



    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_category_url(request=request)

    def validate_title(self, value):
        qs = Category.objects.filter(name__iexact=value)  # including instance
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError("This name has already been used")
        return value