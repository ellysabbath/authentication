from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import  MemberListView, DeaconListView

# url patterns
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Use LoginView for login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Corrected to LogoutView
    path('logged-out/', views.logged_out, name='logged_out'), 
    path('', views.home, name='home'),
# password change
    path('password_change/', auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('services/', views.services, name='services'),
    path('forms/', views.forms, name='forms'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.setie, name='settings'),  # Settings page
    path('password-reset-request/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # urls for getting data and creating  data
    path('manage/create_informations/', views.create_member, name='create_member'),
    path('view/list_members/', MemberListView.as_view(), name='list_members'), 
    path('deacon/create-report/',views.create_report, name='create_report'),  # Endpoint for creating a new deacon
    path('deacons/view-report/', DeaconListView.as_view(), name='deacon_list'),
    # the end

]
