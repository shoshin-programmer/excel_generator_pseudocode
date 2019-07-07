from django.urls import path
from . import views as attrition_views
from django.conf.urls.static import static # new
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    # path('', attrition_views.index, name='attrition-index'),
    path('', RedirectView.as_view(url='/upload/')),
    path('upload/', attrition_views.upload, name='upload'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)