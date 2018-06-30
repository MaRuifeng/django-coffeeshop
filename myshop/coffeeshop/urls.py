from django.urls import path

from . import views

app_name = 'coffeeshop'
urlpatterns = [
    path('', views.OrderCreateView.as_view(), name='index'),
    path('ajax/load-drinktypes/', views.load_drinktypes, name='ajax_load_drinktypes'),
    path('ajax/load-sizes/', views.load_sizes, name='ajax_load_sizes'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-list/', views.OrderListView.as_view(), name = 'order_list'),
    path('filtered-order-list/', views.FilteredOrderListView.as_view(), name = 'filtered_order_list'),
]
