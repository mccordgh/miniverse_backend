from adventure_creator import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

# Base view at /
urlpatterns = [
    url(r'^$', views.index_view, name='index'),
]

# Adventure Creation URLs
urlpatterns += [
    url(r'^create_adventure/', views.create_adventure_view, name='create_adventure'),
    url(r'^create_room/', views.create_room_view, name='create_room'),
    url(r'^create_item/', views.create_item_view, name='create_item'),
    url(r'^create_interactive/', views.create_interactive_view, name='create_interactive'),
]

# URL for viewing all the current users adventures
urlpatterns += [
    url(r'^view_my_adventures/', views.adventures_view, name='view_my_adventures')
]