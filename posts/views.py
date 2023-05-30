from django.shortcuts import HttpResponse, render, redirect
from posts.models import Product, Review
from posts.forms import ProductCreateForm, ReviewCreateForm
from posts.constants import PAGINATION_LIMIT


# Create your views here.
""" MVC - Model View Controller """

""" Controller's """


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        max_page = products.__len__() / PAGINATION_LIMIT
        if search:
            products = products.filter(title__icontains=search) | products.filter(description__icontains=search)

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)
        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]
        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)

        }
        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.review_set.all(),
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(id=id)
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product
            )

            return redirect('/products/')

        return render(request, 'products/detail.html', context={
            'form': form
        })


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                quantity=form.cleaned_data.get('quantity')
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })