# from django.urls import path
# from .views import SpyCatView, SpyCatDetailView, MissionView, MissionDetailView

# urlpatterns = [
#     path('cats/', SpyCatView.as_view(), name='spycat-list'),
#     path('cats/<int:pk>/', SpyCatDetailView.as_view(), name='spycat-detail'),
#     path('missions/', MissionView.as_view(), name='mission-list'),
#     path('missions/<int:pk>/', MissionDetailView.as_view(), name='mission-detail'),
# ]

from django.urls import path
from .views import SpyCatView, MissionView, MissionDetailView

urlpatterns = [
    path('cats/', SpyCatView.as_view(), name='spycat-list'),
    path('missions/', MissionView.as_view(), name='mission-list'),
    path('missions/<int:pk>/', MissionDetailView.as_view(), name='mission-detail'),
]
