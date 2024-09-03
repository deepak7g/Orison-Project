from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import storeDB
# Create your views here.

def home(request):
    print("Recived Save Request!...")

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        #print("name", name)
        #print("email", email)
        #print("message", message)
        #print(request.POST)
        user = storeDB.objects.create(name=name, email=email, message=message)
        user.save()
        if user is not None:
            messages.success(request, "Data Stored....")
            return redirect('home')
            #return HttpResponse("Your data has been saved!")
    
    return render(request, 'home.html')















#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("textarea")
        
#         if name and email and message:
#             storeDB.objects.create(name=name, email=email, message=message)
#             return HttpResponse('Your message has been sent!')
            # storeDB.objects.create(name=name, email=email, message=message)
            # messages.success(request,  'Succesfully Submitted')
            # return redirect('home')
        # else:
        #     messages.success(request,  'not Submitted')
        #     return redirect('home')