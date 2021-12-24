from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.accounts import views

# Create your urls here.
urlpatterns = [
    path(
        "accounts/register/", views.AuthorCreateView.as_view(), name="accounts_register"
    ),
    path(
        "accounts/profile/",
        login_required(views.AuthorUpdateView.as_view()),
        name="accounts_update",
    ),
]