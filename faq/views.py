from django.views.generic import ListView
from .models import FAQ  # Assuming you have an FAQ model

class FAQListView(ListView):
    model = FAQ
    template_name = 'faq/faq_list.html'  # Update to your template path
    context_object_name = 'faqs'
