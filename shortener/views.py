from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from .models import URL

from .forms import ShortenerForm


def home(request):
    template = 'shortener/home.html'

    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        form = ShortenerForm(request.POST)

        if form.is_valid():
            url_object = form.save()

            context = {
                'short_url': url_object.short_url,
                'long_url': url_object.long_url,
                'short_url_hash': url_object.hash,
            }

            return render(request, template, context)

        context['errors'] = form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    try:
        url = URL.objects.get(hash=shortened_part)

        url.clicked()

        return HttpResponseRedirect(url.long_url)

    except:
        raise Http404('Sorry this link is broken :(')


def clicked_view(request, shortened_part):
    try:
        url_object = URL.objects.get(hash=shortened_part)
        template = 'shortener/clicked.html'
        context = {
            'short_url': url_object.short_url,
            'long_url': url_object.long_url,
            'short_url_hash': url_object.hash,
            'clicks': url_object.clicks
        }

        return render(request, template, context)

    except:
        raise Http404('Sorry this link is broken :(')