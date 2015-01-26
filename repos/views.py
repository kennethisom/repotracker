from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from repos.models import Repo

@login_required
def index(request):
    if 'url' in request.POST:
        error = False
        error_msg = ''
        new_url = request.POST['url'].strip()
        full_repo_name = ''
        if new_url.startswith('https://github.com/'):
            full_repo_name = new_url[19:]
        elif new_url.startswith('git@github.com:'):
            full_repo_name = new_url[15:]
        else:
            error = True
            error_msg = "Must provide a Github repo url."
        if not error:
            if full_repo_name.endswith('.git'):
                full_repo_name = full_repo_name[:-4]
            short_repo_name = full_repo_name.rsplit('/', 1)[1]
            u = User.objects.get(username='kenneth')
            new_repo = Repo(name=full_repo_name, short_name=short_repo_name, url=new_url, submitting_user=u)
            new_repo.save()
    current_repos = Repo.objects.all()
    context = {'current_repos': current_repos}
    return render(request, 'repos/index.html', context)
