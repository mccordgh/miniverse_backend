from django.contrib import admin
# from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('adventure_creator.urls'))
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)