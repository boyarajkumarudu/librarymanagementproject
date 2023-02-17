from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from libraryapp.models import Student, Course, Book, Issue_Book


# Create your views here.
def login_fun(request):

    return render(request,'login.html',{'data':''})


def logindata_fun(request):
    name = request.POST['txtname']
    pswd = request.POST['txtpass']
    Student_name = request.POST['txtname']
    Student_pswd = request.POST['txtpass']
    user1 = authenticate(username=name, password=pswd)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('ahome')
        else:
            return render(request, 'login.html', {'data': 'not match'})
    elif Student.objects.filter(Q(Student_name=Student_name) & Q(Student_pswd=Student_pswd)).exists():
        request.session['S_name']=Student_name

        return render(request,'stu_home.html',{'studata':request.session['S_name']})

    else:
        return render(request,'login.html',{'data':'chek name and password'})


def admin_fun(request):
    return render(request,'admin.html',{'data':''})


def admindata_fun(request):
    NAME=request.POST['txtname']
    PASSWORD=request.POST['txtpass']
    EMAIL=request.POST['txtemail']
    if User.objects.filter(Q(username=NAME)|Q(email=EMAIL)).exists():
        return render(request,'admin.html',{'data':'username email is alredy exists'})
    else:
        u1=User.objects.create_superuser(username=NAME,email=EMAIL,password=PASSWORD)
        u1.save()
        return redirect('log')




def student_fun(request):
    course=Course.objects.all()
    return render(request,'student.html',{'course_data':course})


def studentdata_fun(request):
    s1=Student()
    s1.Student_name=request.POST['txtname']
    s1.Student_phone=request.POST['txtphon']
    s1.Student_sem=request.POST['txtsem']
    s1.Student_pswd=request.POST['txtpass']
    s1.Student_Course_id=Course.objects.get(Course_name=request.POST['ddlcourse'])
    s1.save()
    return redirect('log')


def shome_fun(request):
    return render(request,'stu_home.html')


def adminhome_fun(request):
    return render(request,'adminhome.html')


def addbook_fun(request):
  course=Course.objects.all()
  return render(request,'addbook.html',{'course_data':course})


def addbookdata_fun(request):
    b1=Book()
    b1.Book_name=request.POST['txtbook']
    b1.Author_name=request.POST['txtauthor']
    b1.Course_id=Course.objects.get(Course_name=request.POST['ddlcourse'])
    b1.save()
    return redirect('add')


def display_fun(request):
    b1 = Book.objects.all()
    return render(request,'displaybook.html',{'bookdata':b1})


def update_fun(request,id):
    b1=Book.objects.get(id=id)
    course=Course.objects.all()
    if request.method=='POST':
        b1.Book_name = request.POST['txtbook']
        b1.Author_name = request.POST['txtauthor']
        b1.Course_id = Course.objects.get(Course_name=request.POST['ddlcourse'])
        b1.save()
        return redirect('display')
    return render(request,'updatebook.html',{'bdata':b1,'course_data':course})


def del_fun(request,id):
    b1 = Book.objects.get(id=id)
    b1.delete()

    return redirect('display')


def logout_fun(request):
    return redirect('log')


def assign_fun(request):
    course=Course.objects.all()
    student=Student.objects.all()
    book=Book.objects.all()
    return render(request,'assignbook.html',{'course_data':course,'stu_data':student,'book_data':book})

def assingdata_fun(request):
    stud = Student.objects.filter(Q(Student_sem=request.POST['txtsam']) & Q(Student_Course_id=Course.objects.get(Course_name=request.POST['ddlcourse'])))
    book = Book.objects.filter(Course_id=Course.objects.get(Course_name=request.POST['ddlcourse']))
    return render(request, 'assignbook.html', {'stud_data': stud, 'book_data': book})



def assreaddata_fun(request):
    i1 = Issue_Book()
    i1.S_name = Student.objects.get(Student_name=request.POST['textname'])
    i1.S_Book_name = Book.objects.get(Book_name=request.POST['txtbook'])
    i1.Start_date = request.POST['txtsdate']
    i1.Start_end = request.POST['txtedate']
    i1.save()
    return redirect('ass')

def issueddisplay_fun(request):
    i1 = Issue_Book.objects.all()
    return render(request,'issuebook.html',{'bdata': i1})




def assingdate_fun(request,id):
    i1=Issue_Book.objects.get(id=id)
    s1=Student.objects.get(id=i1.S_name_id)
    b1=Book.objects.filter(Course_id=s1.Student_Course_id)
    if request.method=='POST':
        i1.S_name = Student.objects.get(Student_name=request.POST['textname'])
        i1.S_Book_name=Book.objects.get(Book_name=request.POST['txtbook'])
        i1.Start_date=request.POST['txtsdate']
        i1.Start_end=request.POST['txtedate']
        i1.save()
        return redirect('issu')
    return render(request,'update2.html',{'issdata':i1,'bdata':b1})



def assingdelet_fun(request,id):
    i1 = Issue_Book.objects.get(id=id)
    i1.delete()
    return redirect('issu')


def studentprofile_fun(request):
    s1=Student.objects.get(Student_name=request.session['S_name'])
    return render(request,'student_profile.html',{'data':s1})


def updateprof_fun(request,id):
    s1=Student.objects.get(id=id)
    if request.method=='POST':
        s1.Student_name = request.POST['txtname']
        s1.Student_phone = request.POST['txtphon']
        s1.Student_sem = request.POST['txtsem']
        s1.Student_pswd = request.POST['txtpass']
        s1.save()
        return redirect('stpro')
    return render(request,'student_update.html',{'data':s1})


def studentissue_fun(request):
    a1=Issue_Book.objects.filter(S_name=Student.objects.get(Student_name=request.session['S_name']))
    return render(request,'sissue_book.html',{'ddata':a1})


def slogout_fun_fun(request):
    return redirect('log')