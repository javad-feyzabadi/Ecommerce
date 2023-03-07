from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.views import View

from . models import Product,Category
from . tasks import all_bucket_objects_task,delete_object_task,download_object_task

from utils import IsAdminUserMixin


class HomeView(View):
    def get(self,request,category_slug=None):
        products = Product.objects.filter(avilable = True)
        categories = Category.objects.filter(is_sub = False)
        if category_slug:
             category = Category.objects.get(slug = category_slug)
             products = products.filter(category = category)
        return render(request,'home/home.html',{'products':products,'categories':categories})


class ProductDetailView(View):
    def get(self,request,slug):
        product = get_object_or_404(Product,slug = slug)
        return render(request,'home/detail.html',{'product':product})
    

class BucketHomeView(IsAdminUserMixin,View):
    template_name = 'home/bucket.html'
    
    def get(self,request):
        objects  = all_bucket_objects_task()
        return render(request,self.template_name,{'objects':objects})


class DeleteBucketObject(IsAdminUserMixin,View):

    def get(self,request,key):
        delete_object_task.delay(key)
        messages.success(request,'your obect will be delete soon','succes')
        return redirect('home:bucket')


class DownloadBucketObject(IsAdminUserMixin,View):
	def get(self, request, key):
		download_object_task.delay(key)
		messages.success(request, 'your download will start soon.', 'info')
		return redirect('home:bucket')