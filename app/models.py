from django.db import models
import json
from django.utils import timezone





class UserInfo(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='user_info')
    name = models.CharField(max_length=50, default='新用户')
    def __str__(self):
        return self.name




class Entry(models.Model):
    word=models.CharField(max_length=30)
    level=models.SmallIntegerField()

    definitions=models.TextField(default='[]')
    def set_definitions(self, x):
        self.definitions = json.dumps(x)
    def get_definitions(self):
        return json.loads(self.definitions)

    definition_rates=models.TextField(default='{}')
    def set_definition_rates(self, x):
        self.definition_rates = json.dumps(x)
    def get_definition_rates(self):
        return json.loads(self.definition_rates)

    phonetic=models.TextField(default='{}')
    def set_phonetic(self, x):
        self.phonetic = json.dumps(x)
    def get_phonetic(self):
        return json.loads(self.phonetic)

    sentences=models.TextField(default='[]')
    def set_sentences(self, x):
        self.sentences = json.dumps(x)
    def get_sentences(self):
        return json.loads(self.sentences)



class Repo(models.Model):
    name=models.CharField(max_length=50,default='new repo')
    words=models.TextField(default=[])
    amount=models.IntegerField(default=0)
    def set_words(self, x):
        self.words = json.dumps(x)
    def get_words(self):
        return json.loads(self.words)



class SyncData(models.Model):
    user=models.ForeignKey('auth.User',related_name='sync_data')
    sync_time=models.DateTimeField(auto_now=True)
    data=models.TextField(default={})
    def set_data(self, x):
        self.data = json.dumps(x)
    def get_data(self):
        return json.loads(self.data)

