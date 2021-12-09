"""Users views"""

# django
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView, FormView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


# exception
from django.db.utils import IntegrityError

# models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile


# forms
from users.forms import SignupForm


# our class based views
class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = "users/detail.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    queryset = User.objects.all()
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filter(user=user).order_by("-created")
        return context

class SignUpView(FormView):
    """Users sign up view"""

    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view"""

    template_name = "users/update_profile.html"
    model = Profile
    fields = ["website", "biography", "phone_number", "picture"]

    def get_object(self):
        """Return user profile"""

        return self.request.user.profile
    def get_success_url(self):
        """Return to user's profile"""
        username = self.object.user.username
        return reverse("users:detail", kwargs={"username":username})


class LoginView(auth_views.LoginView):
    """Login view"""

    template_name = "users/login.html"

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""

    template_name = "users/logout.html"







