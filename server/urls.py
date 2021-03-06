from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from team.views import get_members
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from android_app.views import latest_build
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="ECell Main Server API",
      default_version='v1',
      description="Swagger API UI for ecell main server",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0), name = 'schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('sponsors/', include('sponsors.urls')),
    path('mentors/', include('mentors.urls')),
    path('team/', include('team.urls')),
    path('speakers/', include('speakers.urls')),
    path('portal/', include('caportal.urls')),
    path('gallery/', include('gallery.urls')),
    path('is_update_available/', latest_build),
    path('bquiz/', include('bquiz.urls')),
    path('feedback/', include('feedback.urls')),
    path('iportal/', include('iportal.urls')),
    path('investors/', include('investors.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('core/',include('core.urls'))
]
urlpatterns+=staticfiles_urlpatterns()
# for the media urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# connecting the react
urlpatterns.append(re_path('', TemplateView.as_view(template_name="index.html")))

