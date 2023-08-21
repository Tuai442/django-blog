from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import core.views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("api/", include('core.api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


