from django.contrib import admin
from django.urls import path,include
from movies import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls'))
]
