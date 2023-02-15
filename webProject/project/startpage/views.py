from operator import contains
from pickle import GET
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Student
from .models import Complaints
# Create your views here.
def WelcomePage(request):
    return render(request,'welcome page/signup.html')

def AddNewStudent(request):
    if request.method == 'POST':
        newS=Student(
            name=request.POST['name'],
            gpa=request.POST['gpa'],
            birth=request.POST['DateOfbirth'],
            email=request.POST['email'],
            mobNum=request.POST['mob'],
            level=request.POST['level'],
            gender=request.POST['gender'],
        )
        newS.save()
        return redirect('/AddStu')
    return render(request,'add_student.css/add_student.html')



def EditStudent(request,theid):
    if request.method == 'POST':
        x=request.POST['click']
        if x == 'delete':
            sid=request.POST['id']
            Student.objects.filter(id=sid).delete()
            return redirect('/All')
        else:
            sid=request.POST['id']
            Student.objects.filter(id=sid).update(name=request.POST['name'])
            Student.objects.filter(id=sid).update(email=request.POST['email'])
            Student.objects.filter(id=sid).update(gpa=request.POST['gpa'])
            Student.objects.filter(id=sid).update(birth=request.POST['birthdate'])
            Student.objects.filter(id=sid).update(mobNum=request.POST['number'])
            Student.objects.filter(id=sid).update(active=request.POST['activation'])
            Student.objects.filter(id=sid).update(level=request.POST['level'])
            return render(request,'editStudent/editstudent.html',{'x':Student.objects.get(id=theid)})
    return render(request,'editStudent/editstudent.html',{'x':Student.objects.get(id=theid)})

def SelectDepartment(request,theid):
    if request.method == 'POST':
        if request.POST['level'] == '3' or request.POST['level'] == '4':
            Student.objects.filter(id=theid).update(department=request.POST['department'])
    return render(request,'selectD/select_department.html',{'x':Student.objects.get(id=theid)})

def AllStudents(request,sname=""):
    if request.method == 'POST':
        x=request.POST['buttonn']
        if x == 'GoEdit':
            theid=request.POST['TheId']
            return redirect('/Edit/'+theid)
        elif x == 'ToFalse':
            theid=request.POST['TheId']
            Student.objects.filter(id=theid).update(active=False)
            return redirect('/All/'+sname)
        elif x == 'ToTrue':
            theid=request.POST['TheId']
            Student.objects.filter(id=theid).update(active=True)
            return redirect('/All/'+sname)
        else:
            theid=request.POST['TheId']
            return redirect('/Select/'+theid)
    pro=Student.objects.all() 
    return render(request,'allstudent/allstudents.html',{'x':pro.filter(name__contains=sname ,active =True)})
def AllStudentss(request):
    if request.method == 'POST':
        x=request.POST['buttonn']
        if x == 'GoEdit':
            theid=request.POST['TheId']
            return redirect('/Edit/'+theid)
        elif x == 'ToFalse':
            theid=request.POST['TheId']
            Student.objects.filter(id=theid).update(active=False)
            return redirect('all')
        elif x == 'ToTrue':
            theid=request.POST['TheId']
            Student.objects.filter(id=theid).update(active=True)
            return redirect('all')
        else:
            theid=request.POST['TheId']
            return redirect('/Select/'+theid)
    pro=Student.objects.all() 
    return render(request,'allstudent/allstudents.html',{'x':pro})
def Search(request):
    if request.method == 'POST':
        sname=request.POST['name']
        return redirect('/All/'+sname)
    return render(request,'search/search.html')

def InqComPage(request):
    if request.method == 'POST':
        newC=Complaints(
            stuID=request.POST['sid'],
            type=request.POST['a'],
            content=request.POST['content']
        )
        newC.save()
    return render(request,'CompAndInq/CompAndInq.html')

def AllComp(request):
    return render(request,'ComplaintList/ComplaintsList.html',{'x':Complaints.objects.all()})



