from rest_framework import serializers
from .models import Goods, GoodsCategory


class CategorySerializers3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializers2(serializers.ModelSerializer):
    sub_cat = CategorySerializers3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    sub_cat = CategorySerializers2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Goods
        fields = '__all__'

