from django.contrib import admin
from .models import category,qstns,choice
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "category_name"]

admin.site.register(category, CategoryAdmin)

class ChoiceInline(admin.StackedInline):
    model = choice
    extra = 4

class QstnsAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","category", "question", "date_added", "right_choice","marks"]
	list_filter = ['date_added']
	fielsets = [(None, {'fields':['category']}), ({'fields':['question']}),({'fields':['right_choice']}), 
	({'fields':['marks']}),('date information', {'fields':['date_added'],'classes':['collapse']})]
	inlines = [ChoiceInline]
admin.site.register(qstns, QstnsAdmin)

# admin.site.register(choice) 
# class ChoiceAdmin(admin.ModelAdmin):
# 	list_display = ["__unicode__","question","choice_text"]
# admin.site.register(choice, ChoiceAdmin)

