from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Client
from .forms import ContactForm, SubscriptionForm

def landing_page(request):
    if request.method == 'POST':
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, "Your consultation request has been sent!")
                return redirect('landing_page')
        
        elif 'subscribe' in request.POST:
            sub_form = SubscriptionForm(request.POST)
            if sub_form.is_valid():
                sub_form.save()
                messages.success(request, "Thank you for subscribing to our newsletter!")
                return redirect('landing_page')
            else:
                messages.error(request, "Invalid email or already subscribed.")

    context = {
        'projects': Project.objects.all(),
        'clients': Client.objects.all(),
        'contact_form': ContactForm(),
        'sub_form': SubscriptionForm(),
    }
    return render(request, 'landing_page.html', context)