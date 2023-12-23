from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView, Response
from .models import Users,operation,file_datas
from .serializers import Users_serializers,file_datas_serializers,Operation_serializers
import uuid

class User_data(APIView):
    
    def get(self, request ,client_name=None):
            
        try:
            self.check = Users.objects.get(name=client_name)
            self.check = Users_serializers(self.check)
            return Response(self.check.data,200)
        except Exception as e:
            print(e)
            return Response(status=204)
        
    
    def post(self,request):
        self.check = Users_serializers(data=request.data)
        if self.check.is_valid():      
            self.check.save()
            return Response(self.check.data, 200)
        return Response(self.check.data,304)
    
    # def put(self,request,client_name):
    #     self.check = Users.objects.get(name = client_name)
    #     self.check = Users_serializers(self.check,data=request.data,partial=True)
    #     if self.check.is_valid():
    #         self.check.save()
    #         return Response(self.check.data, 200)
    #     return Response(self.check.errors,400)
    
    # def delete(self,request,client_name):
    #     self.check = Users.objects.get(name = client_name)
    #     self.check.delete()
    #     return Response(status=204)



class file_data(APIView):
    
    def get(self, request ,file_id=None):
            
        try:
            self.check = file_datas.objects.get(id=file_id)
            self.check = file_datas_serializers(self.check)
            return Response(self.check.data,200)
        except Exception as e:
            print(e)
            return Response(status=204)
        
    
    def post(self,request):
        self.check = Users_serializers(data=request.data)
        if self.check.is_valid():      
            self.check.save()
            return Response(self.check.data, 200)
        return Response(self.check.data,304)
    
    
    # def delete(self,request,client_name):
    #     self.check = Users.objects.get(name = client_name)
    #     self.check.delete()
    #     return Response(status=204)
    
    

def upload(request):
    return render(request,'upload_file.html',{'info':"","url":None})

def Signin(request):
    return render(request,'login.html')

def check_details(request):
    username = request.POST.get('username')
    passw = request.POST.get('password')
    try:
        username = operation.objects.get(name=username , password=passw)
        return render(request,'upload_file.html')
    except :
        return render(request,'login.html',{'info':"Try Again"})
    
    
def upload_file(request):
    # try:
    if request.method == 'POST':
        print(request.FILES.get('get_file'))
        file_id = str(uuid.uuid1().int)
        data = file_datas()
        data.id = file_id
        data.name=request.FILES.get('get_file')
        data.unique_id =file_id
        data.file_url= settings.MEDIA_ROOT+"\\"+str(request.FILES.get('get_file'))
        data.save()
        return render(request,'upload_file.html',{'info':file_id,"url":"show"})
    else:
        return render(request,'upload_file.html',{'info':"htisdj"})
