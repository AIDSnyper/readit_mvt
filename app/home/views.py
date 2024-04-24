from django.shortcuts import render
from django.views.generic import ListView
from articles.models import Articles


#
# def index(request):
#     model = Articles.objects.all()
#     ctx = {}
#     return render(request, 'index.html', ctx)

class Index(ListView):
    template_name = 'index.html'
    model = Articles
    context_object_name = 'model'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = self.request.GET.get('page')
        context['footer'] = Articles.objects.all()[:2]
        return context
