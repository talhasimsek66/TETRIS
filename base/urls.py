from django.urls import path
from .views import main_view, civil_view, military_view, cargo_view, health_view, disaster_view

urlpatterns = [
    path("", main_view),
    path("civil", civil_view),

    path("military", military_view),
    path("cargo", cargo_view),
    path("health", health_view),
    path("disaster", disaster_view)


]
