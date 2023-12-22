from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.Mainpage, name ="Home"),
    path('About_us', views.About, name = 'About'),
    path('News', views.News, name = 'News'),
    path('Contacts', views.Contacts, name = 'Contacts'),
    path('News/<int:pk>', views.News_view.as_view(), name='News_view')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)