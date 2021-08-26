from django.db import models
from django.contrib.auth.models import User ,PermissionsMixin
from BlogCreatorWeb.logger import get_log

logger = get_log('blog')
# Create your models here.

class User(User,PermissionsMixin):

    def __str__(self):

        """
        __str__ method is used for defining the string which will
            be displayed when the object of BlogCreate class is printed
            eg: In admin page
        """

        try:
            return self.username
        except Exception as e:
            logger.error('The error in User - __str__ method is :'+str(e))
            print(e)