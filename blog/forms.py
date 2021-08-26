from django import forms
from blog.models import BlogCreate
from BlogCreatorWeb.logger import get_log

logger = get_log('blog')

class BlogCreateForm(forms.ModelForm):
    """
    BlogCreateForm class is used for creating blog creation form
    """

    def __init__(self, *args, **kwargs):
        """
        __init__ method is used for Initialization of BlogCreateForm class
        """

        try:
            super(BlogCreateForm, self).__init__(*args, **kwargs)
            self.fields['user'].empty_label = None

            ## pop method is used for removing the user field from fomr
            self.fields.pop('user')
        except Exception as e:
            logger.error('The error in BlogCreateForm - __init__ method is :'+str(e))
            print(e)

    class Meta():
        model = BlogCreate
        fields = ('user','blog_title','blog_content','image','file','video')