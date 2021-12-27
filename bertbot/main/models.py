from django.db import models

# Create your models here.
# Will be implemented into SQL database
class Question(models.Model):
    #   each field is represented by a Class
    question = models.TextField(null=False)
    wiki_terms = models.CharField(max_length=200, null=False)
    wiki_text = models.TextField(null=False)
    answer = models.CharField(max_length=200)
    prediction_score = models.FloatField(default=0)
