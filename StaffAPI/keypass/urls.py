from django.urls import path
from .views import Register,Login,Protected,Logout


urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('protected/',Protected.as_view(),name='protected'),
    path('logout/',Logout.as_view(),name='logout')
]