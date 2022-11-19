import sys
sys.path.insert(0,'/home/josh2297/project/bert_summarize')

from worker import conn
from rq import Queue
from django.shortcuts import render,redirect
from django.views.generic import FormView,DetailView
from .form import SummaryForm
from bert_summarize.summarize_code import Summary

q = Queue(connection=conn)
# Create your views here.

class GenerateSummaryView(FormView):
    form_class=SummaryForm
    template_name='generate_summary.html'
    # success_url="/summary/display/"


    def form_valid(self,form):
        updated=form.cleaned_data
        title=updated.get('book_title')
        pages=updated.get('page_process') or updated.get('page_omit') or []
        sum_object=Summary(updated.get('book_path'),pages)
        text=q.enqueue(sum_object.summarize)
        print('Text: ',text)
        self.text=text;self.title=title
        return render(self.request,'summary.html',{'text_summary':text,'title':title})