from django.urls import path
from api.views import UserView

urlpatterns = [
    path('profile/<int:pk>', UserView.as_view()),
]
