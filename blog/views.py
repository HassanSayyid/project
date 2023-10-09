from django.shortcuts import render

def index(request):
    return  render(request, 'index.html')
def voter(request):
    return render(request, 'voters.html')
def candidate(request):
    return render(request,'candidates.html') 
