from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from random import random, choice

import markdown2


from . import util

def index(request):
    if request.method == "POST":
        for item in util.list_entries():
            if item == request.POST["q"]:
                return entry(request, request.POST["q"])
            if item != request.POST["q"]:
                Substring_Matches = [item for item in util.list_entries() if request.POST["q"] in item]
        return render(request, "encyclopedia/search.html",{
                "Substring_Matches": Substring_Matches
                })

    else:           
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
})

def entry(request, title):
    if request.method == "POST":
        HttpResponse("test")
    if util.get_entry(title):
        html = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/wiki/entry.html", {
            "entry": html,
            "title": title
        })
    else:
        return error(request, "404", "This entry does not exist")

def newpage(request):
    if request.method == "POST":
        for item in util.list_entries():
            if item == request.POST["EntryTitle"]:
                return error(request, "403", "This entry already exists")
        util.save_entry(request.POST["EntryTitle"], request.POST["EntryContent"])
        return HttpResponseRedirect(reverse(entry, args=[request.POST["EntryTitle"]]))
    else:
        return render(request, "encyclopedia/newpage.html")

def edit(request):
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "title": request.GET["title"],
            "entry": util.get_entry(request.GET["title"])
        })
    if request.method == "POST":
        util.save_entry(request.POST["EntryTitle"], request.POST["EntryContent"])
        return HttpResponseRedirect(reverse(entry, args=[request.POST["EntryTitle"]]))

def randompage(request):
    list = util.list_entries()
    return HttpResponseRedirect(reverse(entry, args=[choice(list)]))

def error(request, errorcode, errortext):
    return render(request, "encyclopedia/error.html", {
        "errorcode": errorcode,
        "errortext": errortext
    })
