from django.shortcuts import render

def main_view(request):
    return render(request, "home.html")

def civil_view(request):
    return render(request, "civil.html")

def military_view(request):
    return render(request, "military.html")

def cargo_view(request):
    return render(request, "cargo.html")

def health_view(request):
    return render(request, "health.html")

def disaster_view(request):
    return render(request, "disaster.html")
