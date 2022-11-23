from django.shortcuts import render

# Create your views here.
def faseeha(request):
    return render(request,'faseeha.html',context={'name':'faseeha pandu','birthday':'birthday'})