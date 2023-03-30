from django.db import models

# Create your models here.
class Character(models.Model):
    
    nsme = models.CharField(max_length=255)
    health = models.IntegerField(default=0)
    attak = models. IntegerField(default=8)
    defense = models.IntegerField(default=8)
    luck = models.IntegerField(7)
    magic = models.IntegerField(10)
    
    class Meta:
        abstract:True
    
    def __str__(self):
        return name
    
class Item(models.Model):
    name = models.CharField(max_length=255)
        
    def __str__(self):
        return name
    
class PlayerCharacter(Character):
    backpack = models.ManyToManyField(Item)
        
class EnemyCharacter(Character):
    description = models.TextField()
    
    