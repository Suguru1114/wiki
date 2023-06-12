from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.shortcuts import render, get_object_or_404, redirect
from . import util
from django.shortcuts import render, redirect
import markdown


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
        
def add_page(request):
    if request.method == "POST":
        from = add_page(request.POST)

        if form.is_valid():
        title = form.cleaned_data


    