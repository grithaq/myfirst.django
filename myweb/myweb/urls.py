
from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexView.as_view(),name='index'),
    path('core',coreView.as_view(),name='core'),
    ]
