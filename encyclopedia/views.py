from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.urls import reverse
import markdown2
from random import choice

from . import util

class NewEntryForm(forms.Form):
    new_title = forms.CharField(label="New Title      ")
    new_entry = forms.CharField(label="New Entry")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def add(request): 
    if request.method == "POST":
        form = NewEntryForm(request.POST)

        if form.is_valid():
            entry_title = form.cleaned_data["new_title"]
            entry_text = form.cleaned_data["new_entry"]
            
            if not util.get_entry(entry_title):
                util.save_entry(entry_title, entry_text)
                messages.success(request, "Entry added!")

                return HttpResponseRedirect(reverse("wiki:index"))
            
            else:
                raise forms.ValidationError("Entry already in encyclopedia")
        
    else:
        return render(request, "encyclopedia/add.html", {
        "form": NewEntryForm()
    })


def new_page(request):
    ...


def random_page(request):
    ...


def search(request):
    if request.method == "POST":
        q = request.POST["query"]
        if q:
            content = markdown2.markdown(util.get_entry(q))
            
            if content:
                return render(request, "encyclopedia/q.html", {
                "title": q, 
                "content": content
            })

            else:
                return render(request, "encyclopedia/error.html", {
                "message": "Entry not found"
            })

        else:
            return render(request, "encyclopedia/error.html", {
            "message": "Must enter a query"
        })
        
    else:
       return render(request, "encyclopedia/search.html" )


def wiki(request, q):
    content = util.get_entry(q)
    
    if content:
        content = markdown2.markdown(content)
        return render(request, "encyclopedia/q.html", {
           "title": q, 
           "content": content
        })

    else:
        return render(request, "encyclopedia/error.html", {
            "message": "Entry not found"
        })
    

def error(request, message):
    return render(request, "encyclopedia/error.html", {
        "message": message
    })

