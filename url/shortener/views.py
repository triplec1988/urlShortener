from django.shortcuts import redirect, render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
import string

from url.shortener import models


def short_url_gen(url, size=7):
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(size))
    short = url + code
    return short



def shortened_list(request):

    paginator = Paginator(models.Link.objects.all().order_by('id'), 10)
    page = request.GET.get('page')
    try:
        urls = paginator.page(page)
    except PageNotAnInteger:
        urls = paginator.page(1)
    except EmptyPage:
        urls = paginator.page(paginator.num_pages)

    if request.POST:
        print request.POST
        short = short_url_gen('http://payperks.com/')
        models.Link.objects.create(long_url=request.POST['long_url'], short_url=short)
        return redirect(shortened_list)

    return render(request, 'shortener/list.html', {'urls': urls, })


def url_delete(request, url_id):
    try:
        url = models.Link.objects.get(pk=url_id)
    except models.Link.DoesNotExist:
        raise Http404
    url.delete()
    return redirect('shortened_list')


def url_redirect(request, url_id):
    try:
        url = models.Link.objects.get(pk=url_id)
    except models.Link.DoesNotExist:
        raise Http404
    return redirect(url.long_url)
