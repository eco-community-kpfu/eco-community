from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.views.generic.base import TemplateView
from app_blog.models import Blog, Like
from uuid import uuid4
from app_blog.forms import CommentForm, BlogForm
from slugify import slugify


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'app_blog/create_blog.html'
    form_class = BlogForm

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        blog_obj.image = self.request.FILES['image']
        blog_obj.slug = slugify(blog_obj.title) + '-' + str(uuid4())
        blog_obj.save()
        form.save_m2m()
        return HttpResponseRedirect(reverse('app_blog:blogs'))


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'app_blog/edit_blog.html'
    form_class = BlogForm

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        blog_obj.image = self.request.FILES.get('image', blog_obj.image)
        blog_obj.slug = slugify(blog_obj.title) + '-' + str(uuid4())
        blog_obj.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('app_blog:blog', kwargs={'slug': self.object.slug})


class MyBlog(LoginRequiredMixin, TemplateView):
    template_name = 'app_blog/my_blogs.html'


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/all_blogs.html'


def single_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    liked = False
    if request.user.is_authenticated:
        already_liked = Like.objects.filter(blog=blog, user=request.user)
        if already_liked:
            liked = True
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('app_blog:blog', kwargs={'slug': slug}))
    context = {'blog': blog, 'comment_form': comment_form, 'liked': liked}
    return render(request, 'app_blog/single_blog.html', context)


@login_required
def like_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked = Like(blog=blog, user=user)
        liked.save()
    return HttpResponseRedirect(reverse('app_blog:blog', kwargs={'slug': blog.slug}))


@login_required
def dislike_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('app_blog:blog', kwargs={'slug': blog.slug}))


class DeleteBlogView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'app_blog/my_blogs.html'
    success_url = reverse_lazy('app_blog:manage')

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


