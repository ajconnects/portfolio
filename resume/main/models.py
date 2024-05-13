from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    score = models.IntegerField(default=70, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)
    is_code_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    def __str__(self) -> str:
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=300, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

class ContactProfile(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.EmailField(verbose_name="Email")
    phone = models.SmallIntegerField(verbose_name="Phone Number", null=True)
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    def __str__(self) -> str:
        return self.name

class Testimonial(models.Model):
    thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonial")
    name = models.CharField(max_length=250, blank=True, null=True)
    role = models.CharField(max_length=250, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

class Media(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

class Portfolio(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='blog')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

class Certificate(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=600, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="certificate")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    def __str__(self) -> str:
        return self.name

