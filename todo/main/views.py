from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Todo 
from .forms import Todo_form 

# Create your views here.
def home(request):
    return render(request,'main/index.html')

def v(request):
    tasks = Todo.objects.all()
    return render(request,'main/view.html',{'tasks':tasks})  

def create(request):
    return render(request,'main/add.html')  

def add(request):
    form = Todo_form()
    context = {'formulario':form}
    return render(request,'main/add.html',context)

@csrf_exempt
def add_todo(request):  
    content = request.POST['name']
    desc = request.POST['alt']
    current_date = timezone.now()
    print(content)
    Todo.objects.create(added_date=current_date,text=content,alt_text=desc)
    return render(request,'main/view.html') 
