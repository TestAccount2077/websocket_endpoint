from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^TheDistro/', include('TheDistro.urls')),
    url(r'^admin/', admin.site.urls),
]
