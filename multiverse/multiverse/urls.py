from django.contrib import admin
from django.conf.urls import url, include
from adventure_creator import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'adventures', views.AdventureViewSet)
router.register(r'interactives', views.InteractiveViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get_adventure/(?P<pk>\d+)', views.get_adventure, name='get_adventure'),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', views.LoginView.as_view()),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
