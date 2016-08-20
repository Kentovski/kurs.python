from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'auto', views.AutoViewSet)
router.register(r'manufacturer', views.ManufacturerViewSet)
router.register(r'warehouse', views.WarehouseViewSet)
router.register(r'orders', views.OrdersViewSet)
router.register(r'buyer', views.BuyerViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
