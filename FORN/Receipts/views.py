
from django.shortcuts import render
from django.template import RequestContext
from django.template.context_processors import csrf

from .forms import ReceiptForm
from .models import Receipt
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def add_csrf(request, **kwargs):
    d = dict(user=request.user, **kwargs)
    d.update(csrf(request))
    return d


def index(request):
    all_receipts = Receipt.objects.order_by('-pub_date')
    return render(request, 'homePage1.html', {'all_receipts': all_receipts})


def detail(request, receipt_id):
    try:
        r = Receipt.objects.get(id=receipt_id)
    except:
        raise Http404("Такого рецепта нет!")

    all_comments = r.comment_set.order_by('-id')[:10]

    return render(request, 'detail.html', {'Receipt': r, 'all_comments' : all_comments})


def leave_comment(request, receipt_id):
    try:
        r = Receipt.objects.get(id=receipt_id)
    except:
        raise Http404("Такого рецепта нет!")

    r.comment_set.create(comment_author=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('Receipts:detail', args=(r.id,)))


def create_receipt(request):
    form = ReceiptForm()

    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)

        if form.is_valid():
            form.author_name = request.user
            request.user.profile.rating += 1
            request.user.save()

            form.save()
            return HttpResponseRedirect(reverse('Receipts:index'), RequestContext(request))

    return render(request, 'create_receipt.html', add_csrf(request, form=form))


