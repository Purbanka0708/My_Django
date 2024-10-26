from django.shortcuts import render
from .models import MyVarity,store
from django.shortcuts import get_object_or_404
from .forms import MyVarityForm

# Create your views here.
def all_my(request):
    mine = MyVarity.objects.all()
    return render(request,'my/all_my.html',{'mine':mine})

def my_detail(request,my_id):
    my=get_object_or_404(MyVarity,pk=my_id)
    return render(request,'my/my_detail.html',{'my':my})

def my_store_view(request):
    stores=None
    if request.method=='POST':
        form=MyVarityForm(request.POST)
        if form.is_valid():
            my_variety=form.cleaned_data['my_varity']
            stores=store.object.filter(my_varities=my_variety)
    else:
        form=MyVarityForm()
    return render(request,'my/my_stores.html',{'stores':stores,'form':form})
