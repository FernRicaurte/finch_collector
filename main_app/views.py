from django.shortcuts import render

# Define the home view
def home(request):
  # Include an .html file extension 
  return render(request, 'home.html')

# Define the about view
def about(request):
  # Include an .html file extension 
  return render(request, 'about.html')

# Define the all_finches view
def all_finches(request):
  # Include an .html file extension
  return render(request, 'all_finches/index.html')

# Add this finches list below the imports
finches = [
  {'name': 'Jose', 'breed': 'House finch', 'description': 'red feathers', 'age': 1},
  {'name': 'Carlos', 'breed': 'Purple finch', 'description': '[purple feathers]', 'age': 2},
]
