from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from userapp .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def adminindex(request):
    totalbr=BRANCHES.objects.all().count()
    totalsal=SALOON.objects.all().count()
    totalserv=SERVICES.objects.all().count()
    totregusers=Reg.objects.all().count()
    totfeedback=CONT.objects.all().count()
    pendingbooking=BOOK.objects.filter(status='disapprove').count()
    approved=BOOK.objects.filter(status='approved').count()
    declined=BOOK.objects.filter(status='declined').count()
    return render(request,'adminindex.html',{'totalbr':totalbr,'totalsal':totalsal,'totalserv':totalserv,'totregusers':totregusers,'totfeedback':totfeedback,'pendingbooking':pendingbooking,'approved':approved,'declined':declined})
def branches(request):
    return render(request,'branches.html')
def branchtable(request):
    tab=BRANCHES.objects.all()
    return render(request,'branchestable.html',{'tab':tab})
def branchstore(request):
    if request.method=='POST':
        Name=request.POST['name']
        Image=request.FILES['image']
        branchdata=BRANCHES(Name=Name,Image=Image)
        branchdata.save()
    return redirect('branchtable')
def branchedit(request,id):
    bredit=BRANCHES.objects.filter(id=id)
    return render(request,'branchedit.html',{'bredit':bredit})
def breditstore(request,id):
    if request.method=='POST':
        Name=request.POST['name']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = BRANCHES.objects.get(id=id).Image
        BRANCHES.objects.filter(id=id).update(Name=Name,Image=file)
    return redirect('branchtable')
def brdelete(request,id):
    BRANCHES.objects.filter(id=id).delete()
    return redirect('branchtable')
def saloon(request):
    drop=BRANCHES.objects.all()
    return render(request,'saloon.html',{'drop':drop})
def saltable(request):
    ta=SALOON.objects.all()
    return render(request,'saaloontable.html',{'ta':ta})
def salstore(request):
    if request.method=='POST':
        Sname=request.POST['sname']
        Description=request.POST['description']
        Branch=request.POST['branch']
        Emage=request.FILES['emage']
        saldata=SALOON(Sname=Sname,Description=Description,Branch=Branch,Emage=Emage)
        saldata.save()
    return redirect('saltable')
def saledit(request,id):
    saedit=SALOON.objects.filter(id=id)
    braedit=BRANCHES.objects.all()
    return render(request,'saloonedit.html',{'saedit':saedit,'braedit':braedit})
def saloostore(request,id):
    if request.method=='POST':
        Sname=request.POST['sname']
        Description=request.POST['description']
        Branch=request.POST['branch']
        try:
            img_c = request.FILES['emage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = SALOON.objects.get(id=id).Emage

        SALOON.objects.filter(id=id).update(Sname=Sname,Description=Description,Branch=Branch,Emage=file)
    return redirect('saltable')
def saldelete(request,id):
    SALOON.objects.filter(id=id).delete()
    return redirect('saltable')
def service(request):
    down=SALOON.objects.all()
    return render(request,'services.html',{'down':down})
def servtable(request):
    tablee=SERVICES.objects.all()
    return render(request,'servtable.html',{'tablee':tablee})
def servstore(request):
    if request.method=='POST':
        Serv=request.POST['serv']
        Salon=request.POST['saloon']
        Price=request.POST['price']
        Description=request.POST['description']
        IImage=request.FILES['iimage']
        serstore=SERVICES(Serv=Serv,Salon=Salon,Price=Price,Description=Description,IImage=IImage)
        serstore.save()
    return redirect('servtable')
def servedit(request,id):
    seredit=SERVICES.objects.filter(id=id)
    saloonedit=SALOON.objects.all()
    return render(request,'servedit.html',{'seredit':seredit,'saloonedit':saloonedit})
def serupdate(request,id):
    if request.method=='POST':
        Serv=request.POST['serv']
        Salon=request.POST['saloon']
        Price=request.POST['price']
        Description=request.POST['description']
        try:
            img_c = request.FILES['iimage']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = SERVICES.objects.get(id=id).IImage

        SERVICES.objects.filter(id=id).update(Serv=Serv,Salon=Salon,Price=Price,Description=Description,IImage=file)
    return redirect('servtable')
def servdelete(request,id):
    SERVICES.objects.filter(id=id).delete()
    return redirect('servtable')
def viewreg(request):
    regs=Reg.objects.all()
    return render(request,'viewreg.html',{'regs':regs})
def viewcont(request):
    co=CONT.objects.all()
    return render(request,'viewcont.html',{'co':co})
def viewbook(request):
    buk=BOOK.objects.all()
    return render(request,'viewbooking.html',{'buk':buk})
def approvebooking(request,id):
    BOOK.objects.filter(id=id).update(status='approved')
    return redirect('viewbook')
    
def decline(request,id):
    BOOK.objects.filter(id=id).update(status='declined')
    return redirect('viewbook')
   

        