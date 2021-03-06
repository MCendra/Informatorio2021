from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)
from apps.accounts.models import Author
from apps.blog.forms import CommentForm, PostForm
from apps.blog.models import Category, Newsletter, Post, Comment

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        featured_posts = Post.objects.filter(featured=True)[0:3]
        if self.request.user.is_authenticated:
            nofeatured_posts = Post.objects.filter(featured=False).filter(author=self.request.user.author).order_by("-timestamp")[0:3]
        else:
            nofeatured_posts = False
        latest_posts = Post.objects.order_by("-timestamp")[0:3]
        context = {"featured_posts": featured_posts, "latest_posts": latest_posts, "nofeatured_posts": nofeatured_posts}
        return render(request, "blog/index.html", context=context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()
        messages.info(request, "Te has suscripto corretamente!")
        return redirect("index")


class PostDetailView(DetailView):

    model = Post
    template_name = "blog/post_detail.html"
    _comment_form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by("-timestamp")[0:3]
        context["categories"] = Category.objects.all()
        context["comment_form"] = self._comment_form
        return context

    def post(self, request, *args, **kwargs):
        _post = self.get_object()
        _comment_form = CommentForm(request.POST)
        if _comment_form.is_valid():
            _comment_form.instance.user = request.user.author
            _comment_form.instance.post = _post
            _comment_form.save()
            return redirect(_post)


class PostListView(ListView):

    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.all().order_by("-timestamp")[0:3]
        context["categories"] = Category.objects.all()
        return context

class PostCategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.filter(category=self.kwargs['pk']).all()[0:3]
        context["categories"] = Category.objects.all()
        return context
    
class SearchView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get("q", "")
        search_result = Post.objects.filter(
            Q(title__icontains=q) | Q(overview__icontains=q)
        ).all()
        context = {"search_result": search_result}
        return render(request, "blog/search.html", context=context)

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = Author.objects.filter(user=self.request.user).first()
        form.save()
        return redirect(reverse("post_detail", kwargs={"slug": form.instance.slug}))


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    form_class = PostForm

    def form_valid(self, form):
        if form.instance.author == self.request.user.author:
            form.save()
            return redirect(reverse("post_detail", kwargs={"slug": form.instance.slug}))


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("index")

class LicenseView(TemplateView):
    template_name = "blog/license.html"

class PolicityView(TemplateView):
    template_name = "blog/policity.html"

class ContactView(TemplateView):
    template_name = "blog/contact.html"

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"
    success_url = reverse_lazy("index")

