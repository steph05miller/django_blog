from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post

class PostListView(ListView):
    template_name = 'blogging/lists.html'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(published_date__exact=None)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.published_date is None:
            raise Http404("Post does not exist or is not published.")
        return obj

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

