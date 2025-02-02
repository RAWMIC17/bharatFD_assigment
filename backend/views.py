from django.core.cache import cache
from django.http import JsonResponse
from .models import FAQ
from googletrans import Translator

def faq_list(request):
    lang = request.GET.get('lang', 'en')  # Default language is English

    # Try fetching from cache first
    cache_key = f'faq_list_{lang}'
    faq_data = cache.get(cache_key)

    if not faq_data:
        # Fetch from DB and translate if not found in cache
        faqs = FAQ.objects.all()
        translated_faqs = []

        for faq in faqs:
            translator = Translator()
            translated_question = translator.translate(faq.question, dest=lang).text
            translated_answer = translator.translate(faq.answer, dest=lang).text
            translated_faqs.append({
                'question': translated_question,
                'answer': translated_answer
            })

        faq_data = translated_faqs

        # Store the translated FAQ list in cache for 1 hour
        cache.set(cache_key, faq_data, timeout=3600)

    return JsonResponse(faq_data, safe=False)
