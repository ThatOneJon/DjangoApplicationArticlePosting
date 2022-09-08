from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from personalBlog.forms.forms import register_Form, new_Article
from .models import Article,User, UserProfile
#from django.contrib.auth import get_user_model
from django.contrib import messages


#User = get_user_model()

def register_view(request):
   
    if request.method=="GET":
        form = register_Form()
        context = {
            "form" : form
        }
        return render(request, "register.html", context)

    elif request.method == "POST":
        user=request.POST['username']
        
        if request.POST['password1'] == request.POST['password2']:
            passw=request.POST['password1']

        mail=request.POST['email']
        newUser =User.objects.create_user(username=user, password=passw, email=mail)
        #The objects.create_user() method has to be used, since Django will hash the pass !!! User()...just creating new entry will not work!
        newUser.save()

        return HttpResponseRedirect(reverse("index"))

#NAME OF VIEWS CANNOT BE LOGIN; SINCE THE NAME IS TAKEN IN auth!!
def login_view(request):
    context={}

    if request.method == "POST":
        name=request.POST["username"]
        passw=request.POST["password"]
        print(passw, name)

        user = authenticate(username=name, password=passw)
        print(user)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        else:
            context["message"] = "Login Data incorrect!"
            return render(request, "login.html", context)

    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


#INDEX SITE--------- Shows all Posts ------------------------

def index(request):

    if request.method == "GET":
        articles = Article.objects.all()

    context={
        "headline":"WELCOME TO THE FOO-BLOG-PAGE!",
        "articles": articles
    }
    return render(request, "index.html", context)

#NEW POST -----------------------------------------------

def new_Post(request):    
    PostForm = new_Article()
    context={
        "form":PostForm
    }
    if request.method == "GET":
        return render(request, "newPost.html", context)

    elif request.method == "POST":
    # create form object, bound to input data from the POST request
        form = new_Article(request.POST)
    # check if all fields are valid
        if form.is_valid():
    #cleaned data on wholeform gives a dict with values and keys
            data = form.cleaned_data
            topic = data["headline"]
            this_content=data["body"]
            this_author= request.user
    #top=form.cleaned_data["headline"] #gives data for one specific form field
    #request.POST.get("headline") --> gets value directly => NO VALIDATION ETC

    #check if article with topic already exists
            if not Article.objects.filter(headline=topic).exists():
                article= Article(author=this_author, headline=topic,content=this_content)
                article.save()
                messages.add_message(request, messages.SUCCESS, 'New Article created!')
                return HttpResponseRedirect(reverse("new_Post"))

            else:
    # using django messages framework, to display success message or article already created warning
                messages.add_message(request, messages.SUCCESS, 'Article with this title already exists!')
                return HttpResponseRedirect(reverse("new_Post"))


def one_Article(request,  id):
    this_Article = Article.objects.get(id=id)
    context={
        "article":this_Article
    }

    return render(request, "oneArticle.html", context)

#update field
def edit(request, id):

    if request.method == "POST":
        if 'edit_IT' in request.POST:

            this_Article = Article.objects.get(id=id)
            this_Article.headline=request.POST["newHeader"] 
            this_Article.content=request.POST["newContent"]
            this_Article.save()
            # get the article and edit it -> save

            return HttpResponseRedirect(reverse("index"))
        

        else:
            this_Article = Article.objects.get(id=id)
            this_Article.delete()
            return HttpResponseRedirect(reverse("index"))
    else:
            return HttpResponseRedirect(reverse("index"))

def profile(request,id):
    if request.method=="GET":
        this_Profile=UserProfile.objects.get(username=request.user)
        my_Posts=Article.objects.filter(author=request.user)
        context={
            "profile":this_Profile,
            "posts":my_Posts
        }
        return render(request, "profile.html", context)

    else:
        this_Profile=UserProfile.objects.get(username=request.user)
        this_Profile.bio= request.POST["new_Bio"]
        this_Profile.profileName= request.POST["new_Name"]
        this_Profile.save()
        return HttpResponseRedirect(request.path_info)