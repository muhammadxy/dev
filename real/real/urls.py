from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('muhammadxy/', admin.site.urls),
    # path('', include(apps.user.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Virtual Estate Admin"
admin.site.site_title = "Virtual Estate Admin Portal"
admin.site.index_title = "Welcome to the Virtual Estate Portal"
