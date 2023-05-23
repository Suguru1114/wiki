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
    
# def entry_page(request, title):
#     entry = get_object_or_404(Entry, title=title)

#     if entry:
#         # Entry exists, render the entry template
#         return render(request, 'encyclopedia/entry.html', {'entry': entry})
#     else:
#         # Entry doesn't exist, redirect to the error page
#         return redirect('error')