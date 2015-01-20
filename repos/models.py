from django.db import models
from django.contrib.auth.models import User

class Repo(models.Model):
    name = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True, null=True)
    latest_hash = models.CharField(max_length=30, blank=True, null=True)
    submitting_user = models.ForeignKey(User)

def update_repos():
    repos = Repo.objects.all()
    for repo in repos:
        update_repo(repo)

def update_repo(repo):
    print repo.name
