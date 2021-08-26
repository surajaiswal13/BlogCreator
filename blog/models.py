from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from ckeditor.fields import RichTextField

from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()

from BlogCreatorWeb.logger import get_log

logger = get_log('blog')
# Create your models here.

class BlogCreate(models.Model):
    """
    BlogCreate class is used for creatng model for blog
    """
    
    user = models.ForeignKey(User,related_name='blog',on_delete=models.CASCADE,null=False)
    created_at = models.DateTimeField(auto_now=True)
    blog_title = models.CharField(max_length=500,unique=True)
    blog_slug = models.SlugField(allow_unicode=True,unique=True)
    blog_content = RichTextField(null=True)
    image = models.ImageField(upload_to='blog_images',blank=True,null=True)
    video = models.FileField(upload_to='blog_videos',blank=True,null=True)
    file = models.FileField(upload_to='blog_files',blank=True,null=True)

    def __str__(self):
        """
        __str__ method is used for defining the string which will
            be displayed when the object of BlogCreate class is printed
            eg: In admin page
        """

        try:
            return "{} - {}".format(self.user.username,self.blog_title)
        except Exception as e:
            logger.error('The error in BlogCreate - __str__ method is :'+str(e))
            print(e)

    def save(self, *args, **kwargs):
        """
        The save method is an inherited method from models.Model 
            which is executed to save an instance into a particular Model.
            Whenever one tries to create an instance of a model either from admin 
            interface or django shell, save() function is run. 
        """

        try:
            self.blog_slug = slugify(self.blog_title)
            super().save(*args, **kwargs)
        except Exception as e:
            logger.error('The error in BlogCreate - save method is :'+str(e))
            print(e)


    def get_absolute_url(self):
        """
        It tells our class if a new instance of our class BlogCreate is created then where to go
        """

        try:
            logger.info('BlogCreate - get_absolute_url success')
            return reverse('blog:blogdetail',
                            kwargs={
                                    'username': self.user.username,
                                    'blog_slug': self.blog_slug,
                                    # 'pk': self.user.pk
                                    })
        except Exception as e:
            logger.error('The error in BlogCreate - get_absolute_url method is :'+str(e))
            print(e)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "blog_title"]