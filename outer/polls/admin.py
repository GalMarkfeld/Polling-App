from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text']
    inlines = [ChoiceInline]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

