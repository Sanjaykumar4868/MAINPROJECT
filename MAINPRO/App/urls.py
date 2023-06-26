from App import views
from django.urls import path,include

urlpatterns = [
    path('accounds/',include('django.contrib.auth.urls')),
    path('',views.home,name="home"),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.user_logout,name="logout"),
    path('login/',views.user_login,name="login")
    
]