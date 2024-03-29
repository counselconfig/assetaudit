from django.shortcuts import render,redirect
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator

from django.core import serializers
from django.http import JsonResponse

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.filter(Email_address__exact=q)
    else:
        posts=''
    # Pagintion
    paginator=Paginator(posts,2)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'home.html',{'posts':posts_obj})

# Add Method
def add(request):
	if request.method=='POST':
		Reference_No=request.POST['Reference_No']
		Serial_No=request.POST['Serial_No']
		CMDB_item_type=request.POST['CMDB_item_type']
		User_name=request.POST['User_name']
		Email_address=request.POST['Email_address']
		Organisation=request.POST['Organisation']
		
		Post.objects.create(Reference_No=Reference_No,Serial_No=Serial_No,CMDB_item_type=CMDB_item_type,User_name=User_name,Email_address=Email_address,Organisation=Organisation)
		messages.success(request,'Data has been added')
	return render(request,'add.html')

# Update Method
def update(request,id):
	if request.method=='POST':
		Reference_No=request.POST['Reference_No']
		Serial_No=request.POST['Serial_No']
		CMDB_item_type=request.POST['CMDB_item_type']
		User_name=request.POST['User_name']
		Email_address=request.POST['Email_address']
		Organisation=request.POST['Organisation']
		
		Post.objects.filter(id=id).update(Reference_No=Reference_No,Serial_No=Serial_No,CMDB_item_type=CMDB_item_type,User_name=User_name,Email_address=Email_address,Organisation=Organisation)
		messages.success(request,'Data has been updated')
	post=Post.objects.get(id=id)
	return render(request,'update.html',{'post':post})

# Delete Method
def delete(request,id):
    Post.objects.filter(id=id).delete()
    return redirect('/')

# Load More
def load_more(request):
    offset=int(request.POST['offset'])
    limit=2
    posts=Post.objects.all()[offset:limit+offset]
    totalData=Post.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })
