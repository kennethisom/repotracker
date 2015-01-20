from django.shortcuts import render
from django.contrib.auth.models import User
from repos.models import Repo

def index(request):
    if 'url' in request.POST:
        new_url = request.POST['url']
        repo_name = new_url.rsplit('/', 1)[1]
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        u = User.objects.get(username='kenneth')
        new_repo = Repo(name=repo_name, url=new_url, submitting_user=u)
        new_repo.save()
    current_repos = Repo.objects.all()
    context = {'current_repos': current_repos}
    return render(request, 'repos/index.html', context)
