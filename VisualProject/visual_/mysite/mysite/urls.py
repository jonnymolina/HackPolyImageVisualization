from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'visual_.views.index', name='index'),
    url(r'^clarifai/', 'visual_.views.clarifai', name='clarifai'),
    url(r'^setup/', 'visual_.views.setup', name='setup'),
    url(r'^add/', 'visual_.views.add', name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

