from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'aplikasi' : 'real_mashop',
        'name': 'Raffi Dewangga Susanto',
        'class': 'PBP E',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = {
                'id': str(product_entry.id),
                'name': product_entry.name,
                'price': product_entry.price,
                'description': product_entry.description,
                'thumbnail': product_entry.thumbnail,
                'category': product_entry.category,
                'is_featured': product_entry.is_featured,
                'rating': product_entry.rating,
                'user_username': product_entry.user.username if product_entry.user_id else None,
            }
            return JsonResponse(data)
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [ 
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'rating': product.rating,
            'user_id': product.user_id,
        }          
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
   
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'rating': product.rating,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                data = {
                    'status': 'success',
                    'username': user.username,
                    'message': 'Your account has been successfully created!'
                }
                return JsonResponse(data)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.get_json_data()
                return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                response = JsonResponse({
                    'status': 'success',
                    'username': user.username,
                    'message': 'Login successful'
                })
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.get_json_data()
                return JsonResponse({'status': 'error', 'errors': errors}, status=400)
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        updated_product = form.save()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = {
                'id': str(updated_product.id),
                'name': updated_product.name,
                'price': updated_product.price,
                'description': updated_product.description,
                'thumbnail': updated_product.thumbnail,
                'category': updated_product.category,
                'is_featured': updated_product.is_featured,
                'rating': updated_product.rating,
                'user_username': updated_product.user.username if updated_product.user_id else None,
            }
            return JsonResponse(data)
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': 'Product deleted'})
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    rating = request.POST.get("rating")
    user = request.user

    new_product = Product(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        rating=rating,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)