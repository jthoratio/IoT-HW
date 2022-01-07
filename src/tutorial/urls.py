from django.urls import path, re_path

from .views import FibonacciView
from .views import LogsView

urlpatterns = [

    re_path(r'^fibonacci/?$', FibonacciView.as_view()),
    re_path(r'^logs/?$', LogsView.as_view()),
]
