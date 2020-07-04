from core.models import Repo, Commit
from vinta_teste import celery_app
import requests
import datetime
import json

@celery_app.task(name="create_commits")
def create_commits(request, data):    
    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    lastMonth = lastMonth.replace(day=1)
    lastMonth = lastMonth.strftime('%Y-%m-%dT%H:%M:%SZ')  

    headers = ""
    access_token = request.user.social.extra_data.get("access_token")
    if access_token:
        headers = {'Authorization':'token ' + access_token}  
    r = requests.get('https://api.github.com/repos/'+data.get('owner')+'/'+data.get('name')+'/commits?since='+lastMonth,headers=headers)    
    object_list = []
    if r.status_code == 200:
        for commit in r.json():
            object_list.append(Commit(author=commit.get('commit').get('author').get('name'),
                url=commit.get('commit').get('url'),
                date=commit.get('commit').get('author').get('date'),
                repo=Repo.objects.get(id=data.get('id'))))

        Commit.objects.bulk_create(object_list)

@celery_app.task(name="create_web_hook")
def create_web_hook(request, data):     
    config = {
        "name": "web",
        "active": True,
        "events": [
            "push"         
        ],
        "config": {
            "url": 'https://'+request.get_host() +"/repos/" + str(data.get('id')) + '/update_commits/',
            "content_type": "json",
            "insecure_ssl": "0"
        }
    }    
    headers = ""
    access_token = request.user.social.extra_data.get("access_token")
    if access_token:
        headers = {'Authorization':'token ' + access_token}
    r = requests.post('https://api.github.com/repos/'+data.get('owner')+'/'+data.get('name')+'/hooks', data=json.dumps(config),headers=headers)
    print(r.json())
    print(r.text)