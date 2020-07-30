from .views import index, create, retrieve, update, delete, create_account, index_account, retrieve_account, update_account, delete_account, amount_ajax
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'article'

urlpatterns = [
    path('', index, name='list'),
    path('create/', create, name='create'),
    path('article/<int:pk>/', retrieve, name='retrieve'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create_account/', create_account, name='create_account'),
    path('index_account/', index_account, name='index_account'),
    path('account/<int:pk>/', retrieve_account, name='retrieve_account'),
    path('update_account/<int:pk>/',update_account, name='update_account'),
    path('delete_account/<int:pk>/',delete_account, name='delete_account'),
    path('amount/',amount_ajax, name='amount_ajax'),
]