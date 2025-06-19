from django.urls import path


urlpatterns = [
    path('login/', 'auth_system.views.login_view', name='login'),
    path('logout/', 'auth_system.views.logout_view', name='logout'),
    path('register/', 'auth_system.views.register_view', name='register'),
    path('profile/', 'auth_system.views.profile_view', name='profile'),
    path('profile/edit/', 'auth_system.views.edit_profile_view', name='edit_profile'),
]