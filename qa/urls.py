from django.urls import path, include, re_path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path(
        '',
        views.GenerateQAView.as_view(),
        name="generate_qa"),
    re_path(
        r'help/?',
        TemplateView.as_view(
            template_name="qa_help.html"),
        name="qa_help"),
]
