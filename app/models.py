from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)


    def __str__(self):
        return self.topic_name





class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    Url=models.URLField()

    def __str__(self):
        return self.name



class Access(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100,default='aaa')
    date=models.DateField()
    
    def __str__(self):
        return self.author

    