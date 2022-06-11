from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'LAMASIA KERALA FC Administration'
admin.site.site_title = 'LAMASIA KERALA FC Admin Portal'
admin.site.index_title = 'Welcome To Lamasia Kerala FC'