from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        # Handle the case when the entry does not exist
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found"
        })
    else:
        # Display the entry content
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })

