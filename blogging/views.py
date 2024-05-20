from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.generic import ListView, DetailView
from blogging.models import Post
from blogging.forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

class PostListView(ListView):
    template_name = "blogging/lists.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(published_date__exact=None)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.published_date is None:
            raise Http404("Post does not exist or is not published.")
        return obj

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.published_date = timezone.now()  # Set the published date to now
            post.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogging/add.html', {'form': form})

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
