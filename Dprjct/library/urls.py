from django.urls import path
from . import views

urlpatterns = [
    # /library/
    path('', views.index, name='index'),
    # /library/1/
    path('<int:books_id>/', views.detail, name='detail'),

]
