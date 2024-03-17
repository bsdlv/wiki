from django.shortcuts import render, redirect
from django.contrib import messages
from markdown2 import Markdown
from random import choice
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


def add(request): 
    if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["content"]
            
            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                    "message": "Entry already in database"
                })
            
            else:
                util.save_entry(title, content)
                messages.success(request, "Entry added!")
                markdowner = Markdown()
                return render(request, "encyclopedia/entry.html", {
                    "title": title,
                    "content": markdowner.convert(content)
                })
        
    else:
        return render(request, "encyclopedia/add.html")


def entry(request, q):
    content = util.get_entry(q)
    content = Markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": q,
        "content": content
    })


def random_page(request):
    ...


def search(request):
    if request.method == "POST":
        q = request.POST["q"]
        
        try:
            content = util.get_entry(q)
            markdowner = Markdown()
            html = markdowner.convert(content)

            if html:
                return render(request, "encyclopedia/entry.html", {
                "title": q,
                "content": html 
                })
            
        except TypeError:
            entries = util.list_entries()
            matches = []
            for entry in entries:
                if q in entry:
                    matches.append(entry)
            
            if not matches:
                return render(request, "encyclopedia/error.html", {
                    "message": "No matches found"
                })
            
            return render(request, "encyclopedia/search.html", {
            "matches": matches
            })


def wiki(request, q):
    content = util.get_entry(q)
    
    if content:
        markdowner = Markdown()
        content = markdowner.convert(content)
      
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



