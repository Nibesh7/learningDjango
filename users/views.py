from django.shortcuts import redirect, render
from .forms import NewuserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
def register(request):
    if request.method =='POST':
        form = NewuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('myapp/products')
        else:
            print(form.data['email'],form.data)
    form = NewuserForm()
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request,'users/profile.html')

def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user
        profile = Profile(user=user,image=image,contact_number=contact_number)
        profile.save()
    return render(request,'users/createprofile.html')