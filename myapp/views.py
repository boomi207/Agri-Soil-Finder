from django.shortcuts import render, get_object_or_404,redirect
from .models import Region, Soil, Crop
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def base(request):
    return render(request,'base.html')


@login_required(login_url='login')
def about(request):
    return render(request,'about.html')


@login_required(login_url='login')
def contact(request):
    return render(request,'contact.html')

def region_list(request):
    regions = Region.objects.all()
    return render(request, 'region.html', {'regions': regions})

def soil_list(request, region_id):
    region = get_object_or_404(Region, id=region_id)
    soils = Soil.objects.filter(region=region)
    return render(request, 'soil.html', {
        'region': region,
        'soils': soils
    })


def crop_list(request, soil_id):
    soil = get_object_or_404(Soil, id=soil_id)
    crops = Crop.objects.filter(soil=soil)
    return render(request, 'crop.html', {
        'soil': soil,
        'crops': crops
    })


def crop_detail(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    return render(request, 'crop_detail.html', {'crop': crop})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('region_list')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')   # ✅ safe
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('region_list')  # change if needed
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')