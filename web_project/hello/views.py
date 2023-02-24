from django.http import HttpResponse
import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django import forms
from .models import Bets
#from hello.models import LogMessage

# class LogMessageForm(forms.ModelForm):
#     class Meta:
#         model = LogMessage
#         fields = ("message",)


def home(request):
    data = Bets.objects.all()

    bet = {
        "Bet": data
    }

    return render(request, "hello/home.html", bet )

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# def log_message(request):
#     form = LogMessageForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.log_date = datetime.now()
#             message.save()
#             return render(request, "")
#         else:
#             return render(request, "hello/log_message.html", {"form": form})