from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import TouristReview


# Create your views here.
def review_list(request):
    if request.method=='GET':
        reviews=TouristReview.objects.all()
        return render(request,'review.html',{'reviews':reviews})

def add_review(request):
    if request.method=='POST':
        form=ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review=form.save(commit=False)
            review.save()
            return redirect('review_list')
    else:
        form=ReviewForm()
    return render(request,'review.html',{'form':form})
