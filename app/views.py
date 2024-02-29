from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
from .forms import ProductCreateForm, UserLoginForm, UserRegisterForm
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Author, Product
# ProductLike

# Create your views here.
# class HomeView(View):
#     def get(self, request):
#        return render(request, 'index.html')
    

def homeView(request):
    products = Product.objects.all().order_by("ends_in")
    size = request.GET.get("size", 2)
    page = request.GET.get("page", 1)
    paginator = Paginator(products, size)
    page_obj = paginator.page(page)
    context = {
        "products": page_obj.object_list, 
        "page_obj": page_obj, 
        "num_pages": paginator.num_pages
    }
    return render(request, "index.html", context=context)
    
class ExploreView(View):
    def get(self, request):
        return render(request, 'explore.html')
    
class DetailsView(View):
    def get(self, request):
        return render(request, 'details.html')
    
class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        # products = Author.product_set.all()
        context = {
            'authors': authors,
            # 'products': products
        }
        return render(request, 'author.html', context=context)

    
class CreatView(View):
    def get(self, request):
        form = ProductCreateForm() 
        return render(request, 'create.html', {'form' : form})
    
    def post(self, request):
       form = ProductCreateForm(request.POST, request.FILES)
       if form.is_valid():
            product = form.save(commit=False)
            # product.owner = request.user
            product.save()
            return redirect ('home-page')
       else:
           return render (request, 'create.html', {'form' : form})
       
# class LikeProductView(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         opinion = Product.objects.get(pk=pk)
#         like, created = ProductLike.objects.get_or_create(user=request.user, opinion=opinion)
#         if not created:
#             like.delete()
#         return redirect(reverse("gap:room", kwargs={"pk": opinion.room.pk}))
    
class UserLoginview(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "login.html", {'form': form})
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f"you have logged in as {username}")
                return redirect ('create-page')
            else:
                messages.erorr(request, "Wrong username or password")
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})
        

class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render (request, "register.html", {'form': form})
    
    def post (self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Sucessfully registered")
            return redirect("login-page")
        else:
            return render(request, "register.html", {'form':form})

class UserLogout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "user successfully logged out!")
        return redirect ('home-page')
    

