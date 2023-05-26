from django.urls import path
from markers.views import MarkersMapView, ticket_system_view

app_name = "markers"

urlpatterns = [
    path("", ticket_system_view),
    path("map/", MarkersMapView.as_view()),
]
