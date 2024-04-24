from django.shortcuts import render, redirect

from articles.models import Articles
from .models import Contact
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact')
    ctx = {
        'form': form,
        'footer': Articles.objects.all()[:2]
    }
    return render(request, 'contact.html', ctx)
