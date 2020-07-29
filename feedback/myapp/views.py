from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import Feedback
from .forms import FeedbackForm

# Create your views here.

def feedbackView(request):

    form = FeedbackForm()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid:
            send_mail(
                'Thank You Mail For Your Feedback',
                'Aapka bahot bahot dhanyawad apne vicharon ko prakat kr k humare aache k liye hume bataya iske liye aapka bahot bahot dhanyawad.',
                'badrisharma333@gmail.com',
                [request.POST.get('email')],
                # fail_silently=False,
            )
            redirect('thanks')

    context = {'form': form}
    return render(request, 'myapp/feedback_form.html', context)

def thankYou(request):

    return render(request, 'myapp/thank_you.html')
