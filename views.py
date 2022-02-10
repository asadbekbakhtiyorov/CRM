import p as p
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views import View

# Create your views here.
from app_1.models import Ombor, Product

from CRM.app_1.models import Client, Stats


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        user = request.POST.get('login')
        password = request.POST.get('password')
        users = authenticate(request, username=user, password=password)
        if users is None:
            return redirect('login')
        else:
            login(request, users)
            return redirect('bolim')

class BolimView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect('login')

class MahsulotEdit(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            product = Product.objects.get(id=son)
            return render(request, 'product_update.html', {'all_products':p})
        else:
            return redirect('login')
    def post(self):
        if request.user.is_authenticated:
            product = Product.objects.get(id=son)
            product.nom = request.POST

class ClientView(View):
    def get(self,  request):
        return render(request, 'clients.html')

class Clients_updateView(View):
    def get(self, request):
        return render(request, 'client_update.html')

class ProductView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            p = Product.objects.filter(ombor=o)
        return render(request, 'products.html')
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        Product.objects.create(
            nom = request.POST('pr_name'),
            brend_nomi=request.POST('pr_brand'),
            maxsulot_narxi=request.POST('pr_price'),
            ombor=ombor,
            maxsulot_miqdori=request.POST('pr_amount')
        )
        return redirect('maxsulotlar')

class Product_updateView(View):
    def get(self, request):
        return render(request, 'product_update.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class StatsView(View):
    def get(self):
        stats = Stats.object.all
        client = Client.objects.filter(ombor=o)
        produscts = Product.objects.filter(ombor=o)
        return render(request, 'state.html', {'all_stats': stats, 'products': produscts, 'clients': client})
