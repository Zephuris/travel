from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Travel
from .forms import TravelAddForm

# Create your views here.

def TravelViewSet(request):
    qs = Travel.objects.all()
    return render(request=request,template_name='travel-dashboard.html',context={'travels':qs})

@login_required
def AddTravelViewSet(request):
    if request.method == 'POST':
        form = TravelAddForm(data = request.POST, user = request.user)
        if form.is_valid():
            print("VALIDATED!")
            form.save()
            messages.success(request, 'Your travle added Succefully!')
        messages.error(request, "Unsuccessful travel registering!")
    form = TravelAddForm()
    return render(request=request,
                  template_name='travel-add.html',
                  context={'form':form})