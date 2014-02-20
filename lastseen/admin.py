from django.contrib import admin
from lastseen.models import User, Badge, Submission, Comment

# Register your models here.
class SubmissionInline(admin.TabularInline):
	model = Submission

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		('Firstname',	{'fields': ['firstname']}),
		('Lastname',	{'fields': ['lastname']}),
		('Email',		{'fields': ['email']}),
		('Date Joined',	{'fields': ['join_date']}),
	]
	list_display = ('firstname', 'lastname', 'email', 'join_date')
	list_filter = ['firstname']
	search_fields = ['firstname']
	inlines = [SubmissionInline]

class CommentInline(admin.TabularInline):
	model = Comment

class SubmissionAdmin(admin.ModelAdmin):
	fieldsets = [
		('Submission Date',	{'fields': ['submission_date']}),
		('Latitude',		{'fields': ['latitude']}),
		('Longitude',		{'fields': ['longitude']}),
		('Details',			{'fields': ['details']}),
		('Found',			{'fields': ['found']}),
	]
	list_display = ('submission_date', 'latitude', 'longitude', 'details', 'was_found')
	list_filter = ['submission_date']
	inlines = [CommentInline]

admin.site.register(User, UserAdmin)
admin.site.register(Badge)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Comment)