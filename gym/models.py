from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug.settings import slugify
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

class AuthenticationBackendAnonymous:
    '''
        This is for automatically signing in the user after signup etc.
    '''
    def authenticate(self, user=None):
        # make sure they have a profile and that they are anonymous
        # if you're not using profiles you can just return user
        if not user.get_profile() or not user.get_profile().anonymous:
            user = None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="ProfileImages", default="/user.png")
    bio = models.TextField(null=True, blank=True)
    twitter = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name

class Tag(models.Model):
    tag = models.CharField(max_length=30, unique=True, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tag

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, null=True)
    slug = AutoSlugField(populate_from='category_name', unique=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.category_name)

class Blog(models.Model):
    def custom_slugify(value):
        return slugify(value).replace(' ', '_')
    category = models.ForeignKey(Category, on_delete=models.CharField, null=True, blank=True)
    tag = models.ForeignKey(Tag, blank=True, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='blogimages')
    intro = models.TextField()
    description = RichTextUploadingField()
    quote = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',
                         unique_with=['category', 'tag', 'pub_date__month'],
                         slugify=custom_slugify,
                         null=True
                         )
    active = models.BooleanField(null=True)
    draft = models.BooleanField(null=True)

    def __str__(self):
        return self.title

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(reply=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, obj_id=obj_id).filter(reply=None)
        return qs

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    reply = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    def children(self): #replies
        return Comment.objects.filter(reply=self)

    @property
    def is_reply(self):
        if self.reply is not None:
            return False
        else:
            return True

    def save(self, *args, **kwargs):
        self.comm_name = slugify('comment by' + '-' + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)


    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return '{} . {}'.format(self.blog.title, str(self.author))


