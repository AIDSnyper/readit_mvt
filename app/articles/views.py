from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView

from .forms import CommentForm
from .models import Articles, Tag, Category, Comment


class ArticlesView(ListView):
    template_name = 'blog.html'
    model = Articles
    context_object_name = 'model'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['footer'] = Articles.objects.all()[:2]

        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            context['model'] = Articles.objects.filter(
                Q(title__icontains=q) | Q(category__cat__icontains=q) | Q(tag__tag__icontains=q))
        return context


def sblog(request, pk):
    model = Articles.objects.get(id=pk)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    blogs = Articles.objects.all()[:3]
    connected_comments = Comment.objects.filter(post=model)
    number_of_comments = connected_comments.count()
    form = CommentForm()
    if request.GET:
        q = request.GET.get('/?q')
        return redirect(f'/articles/?q={q}')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = model
            user_comment.user = request.user
            user_comment.save()
            return redirect('sblog', pk)
    ctx = {
        'comments': connected_comments,
        'no_of_comments': number_of_comments,
        'comment_form': form,
        'model': model,
        'tags': tags,
        'cats': categories,
        'blogs': blogs,
        'footer': Articles.objects.all()[:2]
    }
    return render(request, 'blog-single.html', ctx)
