from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.blog import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.PostListView.as_view(), name="post_list"),
    path("post/<slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/category/<int:pk>", views.PostCategoryListView.as_view(), name="post_category_list"),    
    path("search/", views.SearchView.as_view(), name="search"),
    path('license/', views.LicenseView.as_view(), name="license"),
    path('policity/', views.PolicityView.as_view(), name="policity"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path(
        "posts/create/",
        login_required(views.PostCreateView.as_view()),
        name="post_create",
    ),
    path(
        "posts/update/<slug>/",
        login_required(views.PostUpdateView.as_view()),
        name="post_update",
    ),
    path(
        "posts/delete/<slug>/",
        login_required(views.PostDeleteView.as_view()),
        name="post_delete",
    ),
    path('comment/delete/<pk>', views.CommentDeleteView.as_view(), name="comment_delete"),

]