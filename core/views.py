from django.shortcuts import render,redirect
from .models import student
from django.views import View
from .form import addstudentform

class Home(View):
    def get(self,request):
        stu_data=student.objects.all()
        return render(request,"core/home.html",{"studat":stu_data})
    
class Add_Student(View):
    def get(self,request):
        fm = addstudentform()
        return render(request,"core/add_student.html",{"form":fm})
    def post(self,request):
        fm = addstudentform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("/")
        else:
            return render(request,"core/add_student.html",{"form":fm})



class delete_student(View):
    def post(self, request):
        data=request.POST
        id=data.get('id')
        studata=student.objects.get(id=id)
        studata.delete()
        return redirect('/')


class update_student(View):
    def get(self,request,id):
        stu= student.objects.get(id=id)
        fm=addstudentform(instance=stu)
        return render(request,"core/edit-student.html",{"form":fm})
    def post(self,request,id):
        stu= student.objects.get(id=id)
        fm=addstudentform(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
            
