"""VueShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
import xadmin
from VueShop.settings import MEDIA_ROOT
from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from goods.views_base import GoodsListView
# from goods.views import GoodsListView

from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet, GoodsCategoryListViewSet

from rest_framework.authtoken import views

router = DefaultRouter()
# 配置goods的router
router.register(r'goods', GoodsListViewSet)
router.register(r'categorys', GoodsCategoryListViewSet)


# goods_list = GoodsListView.as_view({
#        'get': 'list',
# })


urlpatterns = [
       path('xadmin/', xadmin.site.urls),
       re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

       # 商品详情页
       # path('goods/', GoodsListView.as_view()),
       # path('goods/', goods_list, name='good-list'),
       re_path(r'^', include(router.urls)),

       re_path(r'^api-auth/', include('rest_framework.urls')),
       re_path(r'^api-token-auth/', views.obtain_auth_token),
       path('docs/', include_docs_urls('docs')),

]
