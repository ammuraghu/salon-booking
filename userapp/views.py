from django.shortcuts import render,redirect
from .models import*
from adminapp .models import*
import datetime


# Create your views here.
def userindex(request):
    use=SERVICES.objects.all()
    return render(request,'userindex.html',{'use':use})
def registration(request):
    return render(request,'registration.html')
def regstore(request):
    if request.method=='POST':
        Uname=request.POST['uname']
        Age=request.POST['age']
        Phn=request.POST['phn']
        Email=request.POST['email']
        Address=request.POST['address']
        Pincode=request.POST['pincode']
        Password=request.POST['pwd']
        Repass=request.POST['pswd']
        # if Password!=Repass:
        #     return render(request,'registration.html',{'msg':"Invalid"})
        restore=Reg(Uname=Uname,Age=Age,Phn=Phn,Email=Email,Address=Address,Pincode=Pincode,Password=Password,Repass=Repass)
        restore.save()
    return redirect('registration')
def log(request):
    return render(request,'login.html')


def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        if Reg.objects.filter(Uname=username,Password=password).exists():
           data = Reg.objects.filter(Uname=username,Password=password).values('Age','Phn','Email','Address','id','Pincode','Password','Repass').first()
           request.session['age_u'] = data['Age']
           request.session['phn_u'] = data['Phn']
           request.session['email_u'] = data['Email'] 
           request.session['address_u'] = data['Address'] 
           request.session['u_id'] = data['id']
           request.session['pincode_u'] = data['Pincode'] 
           request.session['repass_u'] = data['Repass'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('userindex') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('log')
def userlogout(request):
    del request.session['age_u']
    del request.session['phn_u']
    del request.session['email_u']
    del request.session['address_u']
    del request.session['u_id']
    del request.session['pincode_u']
    del request.session['repass_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('userindex')
def viewbranch(request):
    branchhstore=BRANCHES.objects.all()
    return render(request,'viewbranch.html',{'branchhstore':branchhstore})
def viewsalons(request,branch):
    if(branch=="all"):
       salstore=SALOON.objects.all()
    else:
        salstore=SALOON.objects.filter(Branch=branch)
    return render(request,'viewsalons.html',{'salstore':salstore})
def viewserv(request,sal):
    if(sal=="full"):
       servstore=SERVICES.objects.all()
    else:
        servstore=SERVICES.objects.filter(Salon=sal)
    return render(request,'viewservice.html',{'servstore':servstore})
def contact(request):
    return render(request,'contact.html')
def contstore(request):
    if request.method=='POST':
        Fname=request.POST['fname']
        Lname=request.POST['lname']
        Email=request.POST['email']
        Subject=request.POST['subject']
        Message=request.POST['message']
        constore=CONT(Fname=Fname,Lname=Lname,Email=Email,Subject=Subject,Message=Message)
        constore.save()
    return redirect('contact')
def viewmore(request,id):
    more=SERVICES.objects.filter(id=id)
    return render(request,'viewmore.html',{'more':more})
def about(request):
    return render(request,'about.html')
def booking(request,id):
    if 'u_id' in request.session:
       se=SERVICES.objects.filter(id=id)
       return render(request,'booking.html',{'se':se})
    return render(request,'login.html',{'msg1':"you need to login first to access  this page"})
def bookstore(request,id):
    if request.method=='POST':
        Userreg=request.session.get('u_id')
        Date=request.POST['date']
        Time=request.POST['time']
        Note=request.POST['note']
        bukstore=BOOK(Date=Date,Note=Note,Time=Time,userreg=Reg.objects.get(id=Userreg),ServiceID=SERVICES.objects.get(id=id),saloID=SALOON.objects.get(id=id))
        bukstore.save()
    return redirect('history')
def history(request):
    regusers=request.session.get('u_id')
    his=BOOK.objects.filter(userreg=regusers)
    return render(request,'history.html',{'his':his})




