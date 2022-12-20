from bert_summarize.summarize_code import Summary
from bert_summarize.qa_code import QA
from worker import conn
from rq import Queue
from .forms import QAForm
from django.views.generic import FormView, DetailView
from django.shortcuts import render, redirect
import sys
sys.path.insert(0, '/home/josh2297/project/bert_summarize')


q = Queue(connection=conn)

# Create your views here.


class GenerateQAView(FormView):
    form_class = QAForm
    template_name = 'qa_form.html'

    def form_valid(self, form):
        updated = form.cleaned_data
        title = updated.get('book_title')
        pages = updated.get('page_process') or updated.get('page_omit') or []
        sum_object = Summary(updated.get('book_path'), pages)
        text = sum_object.text_extractor()
        qa_object = q.enqueue(QA(text).get_answers)
        return render(
            self.request, 'qa.html', {
                'text_qa': qa_object, 'title': title})
