"""Post views"""
# django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

#forms
from posts.forms import PostForm

# models 
from posts.models import Post


# Create your views here.
class PostFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""

    template_name = "posts/feed.html"
    model = Post
    ordering = ("-created",)
    paginate_by = 30
    context_object_name = "posts"

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return the details of a post"""

    template_name = "posts/detail.html"
    queryset = Post.objects.all()
    context_object_name = "post"

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post view"""

    template_name = "posts/new.html"
    form_class = PostForm
    success_url = reverse_lazy("posts:feed")

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context


