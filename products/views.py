from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from .forms import ProductForm, RowProductForm

# Create your views here.


def product_create_view(request):
    initial_data = {
        'title': "My title initial title"
    }
    obj = Product.objects.get(id=1)
    #form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        # form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)
# def product_create_view(request):
#     my_form = RowProductForm()
#     if request.method == 'POST':
#         my_form = RowProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#     context = {
#         "form": my_form
#     }
#     return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     # form = ProductForm(request.POST or None)
#     # if form.is_valid():
#     #     form.save()
#     #     form = ProductForm()
    
#     # context = {
#     #     'form': form
#     # }
#     if request.method == "POST":
#         new_title = request.POST.get("title")
#         print(new_title)
#     context = {}
#     return render(request, 'products/product_create.html', context)

def product_details_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)

    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        "obj": obj
    }
    return render(request, 'product/details.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'obj': obj
    }
    return render(request, 'products/product_delete.html', context)

def product_list(request):
    product_list_object = Product.objects.all()
    context = {
        'product_list_object': product_list_object
    }
    return render(request, 'products/product_list.html', context)

