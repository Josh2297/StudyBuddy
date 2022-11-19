"""bert_summarize URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import sys
sys.path.insert(0,'/home/josh2297/project/bert_summarize')
from summary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('User.urls')),
    path('summary/',include('summary.urls')),
    path('',views.GenerateSummaryView.as_view(),name="home_summary_view"),
    path('qa/',include('qa.urls')),
    path('how_to',TemplateView.as_view(template_name="study_help.html"),name="study_help")
]