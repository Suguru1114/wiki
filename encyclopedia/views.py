from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.shortcuts import render, get_object_or_404, redirect
from . import util
from django.shortcuts import render, redirect
import markdown



# def index(request):
#     return render(request, "encyclopedia/index.html", {
#         "entries": util.list_entries()
#     })

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {"message": "Page not found"})
    else:
        return render(request, "encyclopedia/entry.html", {"title":title, "content":content})


def index(request):
    if request.method == "GET":
        query = request.GET.get('q', '')
        entries = util.list_entries()
        if query:
            # Filter the entries based on the search query
            entries = [entry for entry in entries if query.lower() in entry.lower()]

            # If there is an exact match for the search query, redirect to the entry page
            if query.lower() in [entry.lower() for entry in entries]:
                return redirect('entry', title=query)

        return render(request, "encyclopedia/index.html", {"entries": entries, "query": query})
    # else:
    #     return redirect('index')