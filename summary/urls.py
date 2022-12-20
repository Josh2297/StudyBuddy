from django.urls import path, include, re_path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.GenerateSummaryView.as_view(), name="generate_summary_view"),
    re_path(
        r'help/?',
        TemplateView.as_view(
            template_name="generate_help.html"),
        name="summary_help")
    # path('display/',views.SummaryView.as_view(),name="summary")
]
