
from django.contrib import admin
from django.urls import path, include
from cicd import urls as you

urlpatterns = [
    path('frs_docker/admin/', admin.site.urls),
    path('frs_docker/cicd/', include(you)),
]


# usermod -a -G sudo jenkins