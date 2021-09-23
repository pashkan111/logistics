from django.urls import path

from accounts import views

urlpatterns = [
    # path('signInUp/', views.signin, name='signin'),
    # path('signInUp/', views.signin, name='signin'),
    # path('signInUp/', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
    path('test/', views.test, name='test'),
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path("logout_user", views.logout_user, name='logout_user'),
    path("personal-cabinet/<str:id>", views.PersonalCabinet.as_view(), name='personal-cabinet'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
]
