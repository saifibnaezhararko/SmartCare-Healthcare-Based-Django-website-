# smart_care/views.py

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from . import serializers

# API-এর জন্য আপনার পুরনো কোডটি এখানে রাখা হলো
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# --- ওয়েবসাইট দেখানোর জন্য নতুন ফাংশনগুলো নিচে যোগ করা হলো ---

def index(request):
    # এই ফাংশনটি index.html ফাইলটি ব্রাউজারে দেখাবে
    return render(request, 'index.html')

def login(request):
    # এই ফাংশনটি login.html ফাইলটি দেখাবে
    return render(request, 'login.html')

def logout(request):
    # লগআউটের কোড এখানে লিখতে হবে, আপাতত হোমপেজে পাঠিয়ে দেওয়া হলো
    from django.shortcuts import redirect
    return redirect('home')

def registration(request):
    # এই ফাংশনটি registration.html ফাইলটি দেখাবে
    return render(request, 'registration.html')

def all_appointments(request):
    # সকল অ্যাপয়েন্টমেন্ট দেখানোর জন্য
    return render(request, 'allAppointments.html')

def doc_details(request):
    # ডাক্তারের বিস্তারিত তথ্য দেখানোর জন্য
    return render(request, 'docDetails.html')

def pdf_view(request):
    # পিডিএফ ভিউ দেখানোর জন্য
    return render(request, 'pdf.html')

def user_details(request):
    # ব্যবহারকারীর বিস্তারিত তথ্য দেখানোর জন্য
    return render(request, 'userDetails.html')

def blood_bank_page(request):
    # Blood Bank পেজ দেখানোর জন্য
    return render(request, 'blood_bank.html')

def vaccine_page(request):
    # Vaccine পেজ দেখানোর জন্য
    return render(request, 'vaccine.html')

def contact_us_page(request):
    # Contact Us পেজ দেখানোর জন্য
    if request.method == 'POST':
        from contact_us.models import ContactUs
        from django.contrib import messages
        
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        problem = request.POST.get('problem')
        
        # ডাটাবেসে সেভ করা
        ContactUs.objects.create(
            name=name,
            phone=phone,
            problem=problem
        )
        
        messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
        return render(request, 'contact_us.html')
    
    return render(request, 'contact_us.html')

def doctors_page(request):
    # Doctors পেজ দেখানোর জন্য
    return render(request, 'doctors.html')