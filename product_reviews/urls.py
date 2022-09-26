from django.urls import path
from . import views

urlpatterns = [
    path('',views.reviews_list),
    path('<int:pk>/',views.reviews_detail),
    path('filter/<int:fk>/',views.reviews_by_product),
]
