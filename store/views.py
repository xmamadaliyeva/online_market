from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product(request, slug):
    ctg = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    product = Product.objects.filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'product': product,
    }
    return render(request, 'products.html', ctx)

def single(request, pk=None):
    ctg = Category.objects.all()
    product_pk = Product.objects.get(pk=pk)
    form = ChoiseForm()
    if request.POST:
        forms= ChoiseForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            root=forms.save()
            root=Buy.objects.get(pk=root.id)
            root.product=product_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
