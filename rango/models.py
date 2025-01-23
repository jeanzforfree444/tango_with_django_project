from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    NAME_MAX_LENGTH = 128

<<<<<<< HEAD
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)

    views = models.IntegerField(default=0)

    likes = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)
=======
    name = models.CharField(max_length = NAME_MAX_LENGTH, unique = True)

    views = models.IntegerField(default = 0)

    likes = models.IntegerField(default = 0)

    slug = models.SlugField(unique = True)
>>>>>>> origin

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    class Meta:

        verbose_name_plural = 'Categories'

    def __str__(self):

        return self.name

class Page(models.Model):

    TITLE_MAX_LENGTH = 128

    URL_MAX_LENGTH = 200

<<<<<<< HEAD
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=TITLE_MAX_LENGTH)

    url = models.URLField()

    views = models.IntegerField(default=0)
=======
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    title = models.CharField(max_length = TITLE_MAX_LENGTH)

    url = models.URLField()

    views = models.IntegerField(default = 0)
>>>>>>> origin

    def __str__(self):

        return self.title
    
class UserProfile(models.Model):

<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE)
=======
    user = models.OneToOneField(User, on_delete = models.CASCADE)
>>>>>>> origin

    website = models.URLField(blank=True)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):

        return self.user.username