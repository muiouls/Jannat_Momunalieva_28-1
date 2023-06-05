from django.shortcuts import HttpResponse, render, redirect
from posts.models import Product, Review
from posts.forms import ProductCreateForm, ReviewCreateForm
from posts.constants import PAGINATION_LIMIT
from django.views.generic import ListView, FormView, DetailView


# Create your views here.
""" MVC - Model View Controller """

""" Controller's """


class MainPageCBV(ListView):
    model = Product
    template_name = 'layouts/index.html'


class ProductsCBV(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'products/products.html'

    def get(self, request, *args, **kwargs):
        products = self.queryset
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
        return render(request, self.template_name, context=context)


class ProductDetailCBV(DetailView, FormView):
    model = Product
    template_name = 'products/detail.html'
    form_class = ReviewCreateForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Review.objects.filter(product=self.object)
        return context

    def form_valid(self, form):
        product = self.get_object()
        Review.objects.create(
            text=form.cleaned_data.get('text'),
            product_id=product.id
        )
        return redirect(f'/products/{product.id}/')


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