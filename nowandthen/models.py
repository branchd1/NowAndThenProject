from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Pictures(models.Model):
    TITLE_MAX_LENGTH = 190
    DESCRIPTION_MAX_LENGTH = 1000
    TAG_MAX_LENGTH = 50
    ERA_MAX_LENGTH = 20
    image = models.ImageField(upload_to='shared_pics', unique=True) 
    title = models.CharField(max_length=TITLE_MAX_LENGTH, blank=True)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH, blank=True)
    tag_one = models.CharField(max_length=TAG_MAX_LENGTH, blank=True)
    tag_two = models.CharField(max_length=TAG_MAX_LENGTH, blank=True)
    era = models.CharField(max_length= ERA_MAX_LENGTH, blank=True)
    when_added = models.DateTimeField(auto_now_add = True)
    #slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['when_added']

    def __str__(self):
        return self.title

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __str__(self):
        return self.user.username
