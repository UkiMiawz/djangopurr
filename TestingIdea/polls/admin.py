from django.contrib import admin
from polls.models import Question
from polls.models import Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
