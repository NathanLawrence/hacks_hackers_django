from django.contrib import admin

# Register your models here.

from .models import Quiz, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    max_num = 4

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('quiz', 'text', 'order')
    list_filter = ['quiz']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)