from django.urls import include, path


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
]