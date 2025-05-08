from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('products/',views.productListView.as_view()),
    path('products/create',views.productCreateAPIView.as_view()),
    path('products/',views.productListCreateAPIView.as_view()),
    # path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    # path('orders/',views.order_list),
    # path('products-info/',views.product_info),
    # path('products/filter/',views.productFilterView.as_view()),
    path('products/<int:productId>/',views.productRetrieveView.as_view()),
    # path('products/info',views.ProductInfoSerializer.as_views())
    path('products/info', views.ProductInfoView.as_view()),
    # path('user-orders/',views.UserOrderListAPIView.as_view())
]

router = DefaultRouter()
router.register('orders',views.OrderViewSet)
urlpatterns += router.urls