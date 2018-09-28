from django.conf.urls import url
from .views import *

app_name = 'TheDistro'

urlpatterns = [

    # HTTP URLs
    url(r'^get-data/', get_data),
    url(r'^post-data/$', post_data),

    # AJAX URLs

]
