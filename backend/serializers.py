from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def to_representation(self, instance):
        lang = self.context.get('request').query_params.get('lang', 'en')
        data = super().to_representation(instance)

        if lang == 'hi':
            data['question'] = getattr(instance, f'question_{lang}', instance.question)
            data['answer'] = getattr(instance, f'answer_{lang}', instance.answer)

        return data
