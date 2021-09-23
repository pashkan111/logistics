from django.urls import path
from tracking import views
# from tracking.views import Search

urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
    path('api/get-track-info/', views.Trak.as_view()),
]