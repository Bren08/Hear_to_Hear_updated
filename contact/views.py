from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def contactview(request):
    name = ''
    email = ''
    message = ''

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")

        if request.user.is_authenticated():
            subject=str(request.user)+ "s Message"
        else:
            subject = "A Visitor's Message"

        comment = name + "with email," + email + ", sent the following message:\n\n" + message,
        send_mail(subject, message, 'brenande@gmail.com', [email])

        context = {'form': form}
        return render(request, 'home.html', context)
    else:
        context = {'form': form}
        return render(request, 'contact.html', context)