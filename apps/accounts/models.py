from django.db import models
from io import BytesIO
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.
class Author(models.Model):

    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    picture = models.ImageField(
        _("Picture"), upload_to="thumbnail", default="thumbnail/noimage.png", blank=True
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture: 
            img = Image.open(default_storage.open(self.picture.name))
            if img.mode != 'RGB':
                img = img.convert('RGB') 
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.picture.name, buffer)