from django.shortcuts import render, redirect
from .models import Package, About, Review
from .forms import ReviewForm

def index(request):
    packages = Package.objects.all()
    about  = About.objects.all()
    reviews = Review.objects.all().order_by('-created_at')  # Fetch existing reviews
    form = ReviewForm()  # Ensure the form is available in the context

    obj = {
        'packages': packages,
        'about': about,
        'reviews': reviews,
        'form': form  # Pass form to the template
    }
    return render(request, 'core/index.html', obj)

def submit_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:mainPage')  # Redirect back to the homepage

    return redirect('main:mainPage')  # Redirect even if the form is invalid


def all_reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'core/all_reviews.html', {'reviews': reviews})
