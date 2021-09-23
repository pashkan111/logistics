from django.urls import path

from . import views

urlpatterns = [
    # path('offices/', views.t, name='offices'),
    path('offices/', views.OfficeView.as_view(), name='offices'),
    path('api/create-office', views.OfficeApiView.as_view()),
]