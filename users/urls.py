from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, UserLogin, UserLogout, ProfileUpdate

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),

]