from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to Spy Cat Agency API. Use /api/ for endpoints."})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cats.urls')),
    path('', home_view),
]