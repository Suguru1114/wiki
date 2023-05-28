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
    
def index(request):
    if request.method == "GET":
        query = request.GET.get('q', '')    
        entries = util.list_entries()
        if query:
            # Filter the entries based on the search query
            entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/index.html", {"entries": entries, "query": query})
    else:
        return redirect('index')

# def entry_page(request, title):
#     entry = get_object_or_404(Entry, title=title)

#     if entry:
#         # Entry exists, render the entry template
#         return render(request, 'encyclopedia/entry.html', {'entry': entry})
#     else:
#         # Entry doesn't exist, redirect to the error page
#         return redirect('error')

# add search function 