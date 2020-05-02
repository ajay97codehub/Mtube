from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movies
from pytube import YouTube
import os.path


# Create your views here.
# This is home page
def home_page(request):

    mlist=Movies.objects.all()
    movie_list=[]
    for m in mlist:
        temp={
            "mid":m.id,
            "mtitle":m.mtitle,
            "murl":m.murl,
            "mimg":m.mimg,
            "mduration":m.mduration,
            "mimdb":m.mimdb,
            "mplot":m.mplot,
            "mdirectors":m.mdirectors,
            "mactors":m.mactors,
            "mgenres":m.mgenres,
            "mlanguage":m.mlanguage
        }
        movie_list.append(temp)

    context = {
        'movie_list':movie_list
    }
    return render(request,'home_page.html', context)

# This is Search page
def search_page(request):
    
    search=request.GET.get('search')
    if search:

        slist = Movies.objects.filter(mtitle__contains=search)
        movie_list=[]
        for m in slist:
            temp={
                "mid":m.id,
                "mtitle":m.mtitle,
                "murl":m.murl,
                "mimg":m.mimg,
                "mduration":m.mduration,
                "mimdb":m.mimdb,
                "mplot":m.mplot,
                "mdirectors":m.mdirectors,
                "mactors":m.mactors,
                "mgenres":m.mgenres,
                "mlanguage":m.mlanguage
            }
            movie_list.append(temp)

        context = {
            'movie_list':movie_list
        }
        return render(request, 'search_page.html', context)
    else:
        return redirect('/home_page/')
# This contact page
def contact_page(request):
    return render(request,'contact_page.html')

# This is about page
def about_page(request):
    return render(request,'about_page.html')


#***********************This is download page*********************************

def download_page(request,m_id):
    homedir = os.path.expanduser("~")
    m=Movies.objects.get(pk=m_id)
    # context={"data":data}
    # url1="https://www.youtube.com/watch?v=H48ZVjoPuZw&list=RDMMWM0i4jhKRxc&index=14"
    # YouTube(url1).streams.first().download(homedir +'/Downloads')
    # return render(request, )
    data={
        "mid":m.id,
        "mtitle":m.mtitle,
        "mimg":m.mimg,
        "mduration":m.mduration,
        "mimdb":m.mimdb,
        "mdirectors":m.mdirectors,
        "mactors":m.mactors,
        "mgenres":m.mgenres,
        'path':'Downloading in the path : '+homedir +'/Downloads'
    
    }
    return render(request,'download_page.html',data)

    # ***************This is for confirm downloading **************************************
def confirm(request,mid):
    homedir = os.path.expanduser("~")
    m=Movies.objects.get(pk=mid)
    movie_url=m.murl
    YouTube(movie_url).streams.first().download(homedir +'/Downloads')
    

