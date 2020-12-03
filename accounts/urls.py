from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name="login"),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
    url(r"profile/$", views.Profile.as_view(), name="profile"),
    url(r"password_reset/$",
         auth_views.PasswordResetView.as_view(
             template_name="accounts/password_reset.html"
         ),
         name="password_reset"),
    url(r"password_reset/done/$",
         auth_views.PasswordResetDoneView.as_view(
             template_name="accounts/password_reset_done.html"
         ),
         name="password_reset_done"),
    url(r"reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_confirm.html"
         ),
         name="password_reset_confirm"),
    url(r"reset/done/$",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="accounts/password_reset_complete.html"
         ),
         name="password_reset_complete"),
]
