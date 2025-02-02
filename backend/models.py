from googletrans import Translator
from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.pk:  # Check if this is a new object
            try:
                self.question = translator.translate(self.question, dest='en').text
                self.answer = translator.translate(self.answer, dest='en').text
            except Exception as e:
                self.question = self.question  # fallback to original
                self.answer = self.answer  # fallback to original
        super().save(*args, **kwargs)
