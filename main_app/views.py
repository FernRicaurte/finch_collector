from django.shortcuts import render
from .models import Finch

# Define the home view
def home(request):
  # Include an .html file extension 
  return render(request, 'home.html')

# Define the about view
def about(request):
  # Include an .html file extension 
  return render(request, 'about.html')

# Define the finches_index view
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })

