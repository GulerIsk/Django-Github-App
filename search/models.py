from django.db import models


class Search(models.Model):
    
    fullName = models.TextField()    
    userName = models.TextField()
    email = models.TextField() 
    location = models.TextField() 
    company = models.TextField() 
    description = models.TextField()       #bio description
    blog = models.TextField()              #blog 
    profile_url = models.TextField()       # github profile
    pPhoto = models.TextField()  #profile photo
    createDate = models.TextField()        #joined Github
    reposName = models.TextField()         #repository name
    reposLanguages = models.TextField()    #repository language
    
    def __str__(self):
        return self.name


