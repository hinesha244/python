from django.contrib import admin
from .models import Playercategory,Playerteam,Player,Playerfeedback
# Register your models here.

class showPlayercategory(admin.ModelAdmin):
    list_display = ['categoryname', 'categorydesc']
admin.site.register(Playercategory,showPlayercategory)

class showPlayerteam(admin.ModelAdmin):
    list_display = ['teamname', 'teamdesc']
admin.site.register(Playerteam,showPlayerteam)

class showPlayer(admin.ModelAdmin):
    list_display = ['Name', 'category', 'teamname', 'runs', 'wickets', 'Hundreads', 'fiftys', 'jersyno']
admin.site.register(Player,showPlayer)

class showPlayerfeedback(admin.ModelAdmin):
    list_display = ['Playername', 'rating', 'review', 'Feedback']
admin.site.register(Playerfeedback,showPlayerfeedback)