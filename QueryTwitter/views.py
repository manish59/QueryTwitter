from django.shortcuts import render
def index(request):
    context={"Title":"QueryTwitter"}
    return render(request,"QueryTwitter/index.html",context)