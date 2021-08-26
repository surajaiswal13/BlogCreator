from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from blog.models import BlogCreate
from blog.forms import BlogCreateForm
from  django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import Http404
from BlogCreatorWeb.logger import get_log

logger = get_log('blog')

# Create your views here.
from accounts.models import User

class BlogCreateView(LoginRequiredMixin,CreateView):
    """
    BlogCreateView class is used for creating a view for Blog Creation
    """

    form_class = BlogCreateForm
    model = BlogCreate
    template_name = "blogcreate.html"

    def form_valid(self, form):
        """
        form_valid() ,ethod is used when valid form data has been Posted and 
            also we overside it to some modification
        """

        try:
            # With these our form will automatically select the user as current logged in user
            form.instance.user = self.request.user  
        except Exception as e:
            logger.error('The error in BlogCreateView - form_valid method is :'+str(e))
            print(e)
        else:
            logger.info('BlogCreateView Form Validation Success')
            return super().form_valid(form)

class BlogDetailView(DetailView):
    """
    BlogDetailView class is used for creating a view for displaying Blog details
    """

    model = BlogCreate
    template_name = "blogdetail.html"
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    """
    BlogDetailView class is used for creating a view for displaying Blog details
    """
    
    model = BlogCreate
    form_class = BlogCreateForm
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'
    template_name = 'blogcreate_update_form.html'

    def get_absolute_url(self):
        """
        It tells our class if a new instance of our class BlogCreate is created then where to go
        """

        try:
            logger.info('BlogUpdateView - get_absolute_url success')
            return reverse('blog:blogdetail',
                            kwargs={'username': self.user.username,
                                    'blog_slug': self.blog_slug,
                                    # 'pk':self.user.pk
                                    })
        except Exception as e:
            logger.error('The error in BlogUpdateView - get_absolute_url method is :'+str(e))
            print(e)

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    """
    BlogDeleteView class is used for creating a view for displaying Blog details
    """

    model = BlogCreate
    template_name = 'blogcreate_confirm_delete.html'
    success_url = reverse_lazy('home')
    slug_field = 'blog_slug'
    slug_url_kwarg = 'blog_slug'

class BlogListView(LoginRequiredMixin,ListView):
    """
    BlogListView class is used for creating a view for displaying Blog details
    """

    model = BlogCreate
    template_name = 'blogcreate_list.html'
    context_object_name = 'blogs'
    success_url = reverse_lazy('blog:bloglist')
    ordering = ["-created_at"]
    paginate_by = 8

## get queryset is written already we are overwriting it for custom list of post of logged in users
## self.request.field will fetch you the current object details
    def get_queryset(self):
        try:
            ## user__username is used because user is a foreignKey
            user = BlogCreate.objects.filter(user__username= self.request.user.username)
        except Exception as e:
            logger.error('The error in BlogListView - get_queryset method is :'+str(e))
            print(e)
        else:
            logger.info('BlogListView -get_queryset Success')
            return user

class Search(LoginRequiredMixin,ListView):
    """
    Search class is used for creating a view for displaying Blog details
    """

    model = BlogCreate
    context_object_name = 'searchs'
    template_name = "search_list.html"
    paginate_by = 8

    def get_queryset(self):
        """
        It is used to modify the resultset which will be displayed 
        """

        try:
            self.search_input = self.request.GET['query']
        except Exception as e:
            logger.error('The error in Search - get_queryset method is :'+str(e))
            print(e)
        else:
            logger.info('Search - get_queryset Success')
            return BlogCreate.objects.filter(Q(blog_title__icontains= self.search_input) | Q(blog_content__icontains= self.search_input))
            


    def get_context_data(self,**kwargs):
        """
        It is used to fill a dictionary with extra content 
           which we need to display on template
        """

        try:
            context = super().get_context_data(**kwargs)
            context['search_input'] = self.search_input
        except Exception as e:
            logger.error('The error in Search - get_context_data method is :'+str(e))
            print(e)
        else:
            logger.info('Search - get_context_data Success')
            return context
