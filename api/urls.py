from django.urls import path
from .views import UserView, ClientView, UserDetail, ClientDetail


urlpatterns = [
    path('users/', UserView.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),

    path('clients/', ClientView.as_view()),
    path('client/<int:pk>', ClientDetail.as_view()),
]


