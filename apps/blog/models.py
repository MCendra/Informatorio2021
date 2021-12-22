from django.db import models
from io import BytesIO
from django.core.files.storage import default_storage
from django.shortcuts import reverse
from django.utils.text import slugify
from PIL import Image
from tinymce.models import HTMLField
from apps.accounts.models import Author

# Create your models here.
class Category(models.Model):

    title = models.CharField("Título", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(models.Model):

    title = models.CharField("Título", max_length=70)
    overview = models.TextField("Reseña", default="")
    timestamp = models.DateTimeField("Timestamp", auto_now=True)

    content = HTMLField(verbose_name="Contenido", default="")
    featured = models.BooleanField("Publicar", default=False)
    category = models.ManyToManyField(
        Category, verbose_name="Categoría", related_name="post"
    )
    author = models.ForeignKey(
        Author, verbose_name="Author", on_delete=models.CASCADE
    )
    thumbnail = models.ImageField(
        "Imagen", upload_to="thumbnail", default="thumbnail/default.png", blank=True
    )
    slug = models.SlugField("Slug", blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("post_update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("post_delete", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        if self.thumbnail:
            img = Image.open(default_storage.open(self.thumbnail.name))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            if img.height > 1080 or img.width > 1920: 
                output_size = (1920, 1080)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.thumbnail.name, buffer)


class Comment(models.Model):

    user = models.ForeignKey(Author, verbose_name="user", on_delete=models.CASCADE, related_name="comments")
    timestamp = models.DateTimeField("Timestamp", auto_now=True)
    content = models.TextField("Comenta")
    post = models.ForeignKey(
        Post, verbose_name="post", on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return self.user


class Newsletter(models.Model):

    email = models.EmailField("Email", max_length=254)
    timestamp = models.DateTimeField("Timestamp", auto_now=True)

    class Meta:
        verbose_name = "newsletter"
        verbose_name_plural = "newsletters"

    def __str__(self):
        return self.email