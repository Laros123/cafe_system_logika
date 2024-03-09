from django.shortcuts import render
from cafe.models import Review

# Create your views here.

def review_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        review = Review.objects.create(title=title,
            content=content,
            author=request.user
            )
    reviews = Review.objects.all()
    context={
        'reviews': reviews
        }
    return render(request, 'cafe/review_list.html', context)
