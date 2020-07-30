from django.shortcuts import render, redirect, reverse
from .models import Article,Account
from .forms import ItemForm
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def index(request):
    queryset = Article.objects.all()
    context = {
        'articles': queryset,
    }
    return render(request, 'article/index.html', context=context)

def retrieve(request, pk):
    article = Article.objects.get(id=pk)

    context = {
        'article': article,
    }

    return render(request, 'article/retrieve.html', context=context)

# def create(request, article=None):
#     if request.method == 'POST':
#         form = ItemForm(request.POST, request.FILES, instance=article)
#         if form.is_valid():
#             article = form.save()
#             pk = article.id
#             url = reverse('article:retrieve', kwargs={'pk': pk})
#             return redirect(to=url)
#     else:
#         form = ItemForm(instance=article)
#     return render(request, 'article/create.html', {
#         'form':form,
#     })
#
# def update(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     # Get
#     if request.method == 'GET':
#         form = ItemForm(instance=article)
#         return render(request, 'article/create.html', {
#             'form': form,
#         })
#
#     else:
#         form = ItemForm(request.POST, request.FILES, instance=article)
#         if form.is_valid():
#             article = form.save()
#             return(article)

create = CreateView.as_view(model=Article, form_class=ItemForm)

update = UpdateView.as_view(model=Article, form_class=ItemForm)



def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()

    url = reverse('article:list')
    return redirect(to=url)


def create_account(request):
    # Get
    if request.method == 'GET':
        return render(request, 'article/create_account.html', context={})
    # Post
    name = request.POST['name']
    call = request.POST['call']
    address = request.POST['address']
    account = Account.objects.create(name=name, call=call, address=address)
    pk = account.id
    url = reverse('article:index_account')
    return redirect(to=url)


def index_account(request):
    queryset = Account.objects.all()
    context = {
        'accounts': queryset,
    }
    return render(request, 'article/index_account.html', context=context)


def retrieve_account(request, pk):
    account = Account.objects.get(id=pk)
    article = str(account.article_set.all()).replace('QuerySet','').replace('Article:','')

    context = {
        'account': account,
        'article': article,
    }

    return render(request, 'article/retrieve_account.html', context=context)


def update_account(request, pk):
    account = Account.objects.get(id=pk)
    # Get
    if request.method == 'GET':
        context = {
            'account': account,
        }
        return render(request, 'article/update_account.html', context=context)

    # POST
    # request 에서 받아온 내용들
    name = request.POST['name']
    call = request.POST['call']
    address = request.POST['address']

    # 데이터베이스에 바꿀 내용들
    account.name = name
    account.call = call
    account.address = address
    account.save()

    url = reverse('article:retrieve_account', kwargs={'pk': pk})
    return redirect(to=url)


def delete_account(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()

    url = reverse('article:index_account')
    return redirect(to=url)

@require_POST
def amount_ajax(request):
    pk = request.POST.get("pk")
    status = request.POST.get("status")
    article = get_object_or_404(Article, pk=pk)

    if status == "plus":
        article.amount += 1
    else:
        if article.amount > 0:
            article.amount -= 1
        else:
            url = reverse('article:list')
            redirect(to=url)
    article.save()
    ctx = {
        "amount": article.amount,
    }
    return JsonResponse(ctx)