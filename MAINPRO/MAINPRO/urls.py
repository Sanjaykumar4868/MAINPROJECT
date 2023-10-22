
from django.contrib import admin
from django.urls import path,include
from App.views import home,productpage
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('',home, name='home'),
     path('admin/', admin.site.urls),
     path('productpage/',productpage, name='productpage'),
     path('',include('userprofile.urls')),
     path('',include('store.urls')),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
