from django.http import HttpResponseRedirect
from django.shortcuts import render

from encyclopedia.forms import AddPageForm
from . import util
from django.shortcuts import render, redirect
from django import forms
# from .forms import AddPageForm
import markdown
from django.shortcuts import render,redirect, get_object_or_404
# gets an object by id or redirects to the 404 page if the id doesn’t exist.
import random


def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
             "title": title,
             "content": html_content
            })  

 
# def index(request):
#     if request.method == "GET":
#         query = request.GET.get('q', '')
#         entries = util.list_entries()
#         if query:
#             # Filter the entries based on the search query
#             entries = [entry for entry in entries if query.lower() in entry.lower()]

#             # If there is an exact match for the search query, redirect to the entry page
#             if query.lower() in [entry.lower() for entry in entries]:
#                 return redirect('entry', title=query)

#         return render(request, "encyclopedia/index.html", {"entries": entries, "query": query})
#     # else:
#     #     return redirect('index') 


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html",{
                "title": entry_search,
                "content": html_content
            })  
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation" : recommendation
            })

# def add_page(request):
#     if request.method == "POST":
#         form = AddPageForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             # Save the new page using the `util` module or your desired method
#             # ...
#             util.save_entry(title, content)  # Save the new page using the util module
#             return redirect('entry', title=title)

#     else:
#         form = AddPageForm()
#     return render(request, "encyclopedia/add.html", {'form': form})

def add_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/add.html") 
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html",{
                "message": "Entry page already exists. Please use different name"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
        
def edit_page(request):
    # existing_content = util.get_entry(title)
    # content = request.POST['content']

    # if existing_content is None:
    #     return render (request, "encyclopedia/error.html", {
    #         "message": "This entry does not exist"
    #     })
    
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request,"encyclopedia/edit.html", {
            "title":title,
            "content":content
                      
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html",{
        "title":rand_entry,
        "content":html_content
    })