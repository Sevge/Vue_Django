from django.shortcuts import render
from .serializers import GoodsSerializers, CategorySerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters

from .models import Goods, GoodsCategory

from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter

# Create your views here.


# class GoodsListView(APIView):
#     """
#     list all goods
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializers = GoodsSerializers(goods, many=True)
#         return Response(goods_serializers.data)


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    pagination_class = GoodsPagination  # 分页

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['name', 'shop_price']
    filter_class = GoodsFilter  # 过滤
    search_fields = ['name', 'goods_brief']  # 搜索
    ordering_fields = ['sold_num', 'shop_price']  # 排序


class GoodsCategoryListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品类别
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializers
