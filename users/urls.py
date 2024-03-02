from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, UserLogin, UserLogout, ProfileUpdate, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/new_password/', generate_new_password, name='generate_new_password'),
    # path('verifications/', var_url, name='var_url'),

]