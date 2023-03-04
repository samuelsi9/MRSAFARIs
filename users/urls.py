from django.urls import path
from django.urls import include, path
from users import views 
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('login',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('register',views.register,name="register"),
    path('profile',views.profile,name="profile"),
    path('profileupdate',views.profileupdate,name="profileupdate"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
         
    path('send_message/',views.send_message, name='send_message'),
    path('inbox/',views.inbox, name='inbox'),
    path('view_message/<int:message_id>/', views.view_message, name='view_message'),
    path('change_password/', views.change_password, name='change_password'),
    path('password_change_done/', views.password_change_done, name='password_change_done'),
    path('admin-only/', views.admin_only_view, name='admin_only'),
    
] 