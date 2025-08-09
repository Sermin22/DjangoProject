from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls', namespace='students')),
    path('newapp/', include('newapp.urls', namespace='newapp')),
    path('dogs/', include('dogs.urls', namespace='dogs')),
    path('library/', include('library.urls', namespace='library')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('students/', include('students.urls', namespace='students')),
#     path('courses/', include('courses.urls', namespace='courses'))
# ]
