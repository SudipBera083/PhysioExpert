from django.shortcuts import render, redirect
from .models import Package, About, Review, Appointment
from .forms import ReviewForm, AppointmentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.core.paginator import Paginator

def index(request):
    packages = Package.objects.all()
    about = About.objects.all()
    
    # Paginate reviews
    all_reviews = Review.objects.all().order_by('-created_at')
    paginator = Paginator(all_reviews, 6)  # Show 5 reviews per page
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)
    
    form = ReviewForm()
    appointment_form = AppointmentForm()
    show_modal = request.session.pop('show_appointment_modal', False)

    

    context = {
        'packages': packages,
        'about': about,
        'reviews': reviews,  # Now it's a Page object, not a QuerySet
        'form': form,
        'appointment_form': appointment_form,
        'show_appointment_modal': show_modal,
    }
    return render(request, 'core/index.html', context)



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


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, 'Your appointment has been booked successfully! We will contact you soon.')
            
            # Store in session that we should show the modal
            request.session['show_appointment_modal'] = True
            
            # Redirect to the same page with a flag to show the modal
            return HttpResponseRedirect(reverse('main:mainPage'))
    
    # If GET request or invalid form, redirect to main page
    return redirect('main:mainPage')