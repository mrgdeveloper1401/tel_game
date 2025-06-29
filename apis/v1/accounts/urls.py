from rest_framework import routers, urls

from . import views

app_name = "v1_accounts_api"

urlpatterns = [
    urls.path("telegram_login/", views.LoginView.as_view(), name="telegram_login"),

]
