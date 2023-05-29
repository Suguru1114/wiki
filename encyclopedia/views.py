from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Entry


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {"message": "Page not found"})
    else:
        return render(request, "encyclopedia/index.html", {"title":title, "content":content})
    
# def index(request):
#     if request.method == "GET":
#         query = request.GET.get('q', '')    
#         entries = util.list_entries()
        
#         if query:
#             # Filter the entries based on the search query
#             entries = [entry for entry in entries if query.lower() in entry.lower()]
#         return render(request, "encyclopedia/index.html", {"entries": entries, "query": query})
#     else:
#         return redirect('index')


from django.shortcuts import render, redirect
from . import util

def index(request):
    if request.method == "GET":
        query = request.GET.get('q', '')
        entries = util.list_entries()

        if query:
            # Filter the entries based on the search query
            filtered_entries = [entry for entry in entries if query.lower() in entry.lower()]

            # Check if the search query matches any entry
            if filtered_entries:
                # Retrieve the first matched entry
                first_entry = filtered_entries[0]
                content = util.get_entry(first_entry)

                return render(request, "encyclopedia/entry.html", {"title": first_entry, "content": content})
            else:
                return render(request, "encyclopedia/error.html", {"message": "Page not found"})

        return render(request, "encyclopedia/index.html", {"entries": entries, "query": query})
    else:
        return redirect('index')
