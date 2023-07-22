from django.shortcuts import render
from django import forms
from random import choice
from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title ")
    body = forms.CharField(label="Body ")
    
class EditForm(forms.Form):
    body = forms.CharField(label="Body ")

# Homepage
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Display Pages
def content(request, name):
    getName = util.get_entry(name)
    if getName is None:
        return render(request, "encyclopedia/404.html", {
        "entries": name
    })
    else:
        return render(request, "encyclopedia/content.html", {
            "entries": getName.split(),
            "name": name
        })

# Add new page
def add(request):
    if request.method == "POST":

        form = NewPageForm(request.POST)

        if form.is_valid():
           
           title = form.cleaned_data["title"]
           body = form.cleaned_data["body"]
           allEntries = util.list_entries()

           for filename in allEntries:
                if title.lower() == filename.lower():
                    form = NewPageForm()
                    error = "Error Title already exists"
                    return render(request, "encyclopedia/add.html", {
                        "form": form,
                        'error': error
                    })
                
        # Add new page with title and body to list
        util.save_entry(title, body)
        return content(request, title)
    else:
        return render(request, "encyclopedia/add.html", {
        "form": NewPageForm()
        })

def edit(request, name):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            
            body = form.cleaned_data["body"]
            util.save_entry(name, body)

            # After editing, go to page
            return content(request, name)
        else:
            return render(request, "encyclopedia/404.html")
    else:
        return render(request, "encyclopedia/edit.html", {
           "form": EditForm(),
           "body": util.get_entry(name)
        })
    


def search(request):
    search = request.GET.get('q')
    getEntry = util.get_entry(search)

    if getEntry is not None:
        return content(request, search.capitalize())
    else:
        subString = []
        allEntries = util.list_entries()

        for entries in allEntries:
            if search.lower() in entries.lower():
                subString.append(entries)

                return render(request, "encyclopedia/search.html", {
                    "entries": subString,
                    "search": search
                })
        else:
            return render(request, "encyclopedia/search.html", {
                "search": search,
                "error": "Cant find anything related to your search"
            })
        
def random(request):
    return content(request, choice(util.list_entries()))





