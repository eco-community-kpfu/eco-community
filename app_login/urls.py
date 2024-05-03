from django.urls import path
from app_login.views import signup, login, logout, profile, profile_update, profile_extra, profile_extra_update, password_change

app_name = 'app_login'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('update/', profile_update, name='update'),
    path('extra/', profile_extra, name='extra'),
    path('modify/', profile_extra_update, name='modify'),
    path('password/', password_change, name='password'),
]
