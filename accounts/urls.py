from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("login/", LoginView.as_view(
        redirect_authenticated_user=False, #後でTrueに変更
        template_name="accounts/login.html"
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]