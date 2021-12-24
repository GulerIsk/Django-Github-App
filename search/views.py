from django.shortcuts import render,HttpResponse
from .models import Search
import requests

base_url = "https://api.github.com/users/" # github user API

def index(request):
    if request.method == "POST":
            githubname = request.POST['githubname'] 
            response_user = requests.get(base_url + githubname)
            response_repos = requests.get(base_url + githubname + '/repos')

            user_info = response_user.json()
            repositories = response_repos.json()            
            errorm = "THE GITHUB USER COULD NOT BE FOUND!"

            data ={
                'profile' : user_info,
                'repos'   : repositories            
            }
            if "login" in user_info:  
                if Search.objects.filter(userName=githubname): # prevent inserting the same users into the database
                    pass
                else:                                          # insert into the database
                    liste = get_data(data.get('profile'),data.get('repos'))
                    database = Search(userName=githubname, fullName=liste[0],email=liste[1],blog=liste[2],profile_url=liste[3],description=liste[4],location=liste[5],company=liste[6],createDate=liste[7],pPhoto=liste[8],reposName=liste[9],reposLanguages=liste[10])
                    database.save() 
                return render(request,"index.html",data)
            
            elif "message" in user_info:
                data1 = {
                    'error' : errorm
                }
                return render(request,"index.html",data1)
            else:
                pass
            
    else: 
         return render(request,"index.html")


def get_data(data,repos): #get data for insert database
    name = data['name']
    email = data['email']
    blog = data['blog']
    profile_url = data['html_url']
    description = data['bio']
    location = data['location']
    company = data['company']
    createdDate = data['created_at']
    photo = data['avatar_url']
    r_names = []
    r_lang = []

    for repo in repos:        
        r_names.append(repo['name'])
        r_lang.append(repo['language'])

    liste= [name,email,blog,profile_url,description,location,company,createdDate,photo,r_names,r_lang,]
    return liste

