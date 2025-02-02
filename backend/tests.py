import pytest
from .models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(question="What is Django?", answer="A web framework.")
    assert faq.question == "What is Django?"
    assert faq.answer == "A web framework."

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(question="Hola", answer="Como estas?")
    assert faq.question == "Hello"  # Assuming translation to English
    assert faq.answer == "How are you?"
