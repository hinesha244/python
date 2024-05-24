from django.db import models

# Create your models here.

class Playercategory(models.Model):
    categoryname=models.CharField(max_length=20)
    categorydesc=models.TextField()

    def __str__(self):
        return self.categoryname

class Playerteam(models.Model):
    teamname=models.CharField(max_length=30)
    teamdesc=models.TextField()

    def __str__(self):
        return self.teamname

class Player(models.Model):
    Name=models.CharField(max_length=30)
    category=models.ForeignKey(Playercategory,on_delete=models.CASCADE)
    teamname=models.ForeignKey(Playerteam,on_delete=models.CASCADE)
    runs=models.IntegerField()
    wickets=models.IntegerField()
    Hundreads=models.IntegerField()
    fiftys=models.IntegerField()
    jersyno=models.IntegerField()

    def __str__(self):
        return self.Name

class Playerfeedback(models.Model):
    Playername=models.ForeignKey(Player,on_delete=models.CASCADE)
    rating=models.FloatField()
    review=models.TextField()
    Feedback=models.DateField(auto_now_add=True)