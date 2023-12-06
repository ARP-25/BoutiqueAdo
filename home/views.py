from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A view rto return the idnex page.
    """
    return render(request, 'home/index.html')