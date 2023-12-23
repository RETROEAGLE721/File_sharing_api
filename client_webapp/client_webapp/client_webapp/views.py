from datetime import datetime
from django.shortcuts import render
import requests
global username


def load_index(request):
    return render(request,'index.html')

def Signin(request):
    return render(request,'login.html')

def Signup(request):
    return render(request,'create.html')

def download(request):
    return render(request,'download_file.html',{'download':""})

def create_user(request):
    print(request.POST.get('passw1'))
    print(request.POST.get('passw2'))
    if request.POST.get('passw1') == request.POST.get('passw2'):
        data = {
            'name': request.POST.get('username'),
            'password': request.POST.get('passw1'),
        }
        x = requests.post('http://127.0.0.1:8001/User_data',data=data)
        print(x)
        return render(request,'login.html')
    return render(request,'create.html',{'info':'Password and confirm password do not match'}) 
    
    
def check_details(request):
    global username
    if request.method == 'POST':
        x = requests.get('http://127.0.0.1:8001/User_data/'+request.POST.get('username'))
        print(x)
        if x.status_code != 200:
            return render(request,'login.html',{"info":'Invalid username'})
        username = request.POST.get('username')
        return render(request,'download_file.html',{'info':None})


def downlaod_file(request):
    x = requests.get('http://127.0.0.1:8001/file_data/'+request.POST.get('url'))
    if x.status_code != 200:
        return render(request,'download_file.html',{"info":'Invalid Link'})
    print(x.json()['name'])
    return render(request,'download_file.html',{'downlaod_url':"http://127.0.0.1:8001"+x.json()['name'],'file_name':x.json()['name']})
    