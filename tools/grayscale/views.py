import numpy as np
import cv2
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,HttpResponse,redirect
import os
def takePhoto(request):
    if request.method=="POST":
        image=request.FILES.get("userimage")
        #filesystestorage ka object banaya
        fs=FileSystemStorage()
        #file ko save karwaya
        filename=fs.save(image.name,image)
        #jaha file save hui uska address nikala
        filepath=fs.path(filename)
        #address file ko cv2 mein read karwaaya
        data=cv2.imread(filepath)

        #grayscale mein 
        # convert kiya
        data2=cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
        #naya address banaya taki grayscale photo ko save kiya ja sake
        path=os.path.join(fs.location,"../../static/gray")
        #naya filename banaya with extension explicitly
        newfilename=f"gray_{filename}.jpg"

        #new address or filename ko join kiya
        completePath=os.path.join(path,newfilename)

        #grayscale matrix(2d) array ko image mein convert kiya
        cv2.imwrite(completePath,data2)
    
        return render(request,'black.html',{'lelo':newfilename})
    else:
        return render(request,"user.html")

   #compress Image

def compressing(request):
        if request.method=='POST':
            image=request.FILES.get("compressimg")
            fs=FileSystemStorage()
            filename=fs.save(image.name,image)
            filepath=fs.path(filename)
            data=cv2.imread(filepath)
            
            #compress image function
            data2=data.astype("uint8")
            path=os.path.join(fs.location,"../../static/compress")
            newfilename=f"comp_{filename}.jpg"
            completePath=os.path.join(path,newfilename)
            cv2.imwrite(completePath,data2)
            print(data2)
            return render(request,'comp.html',{'lelo':newfilename})
        else:
            return render(request,"comp.html")
        
def resizing(request):

    if request.method=='POST':
            image=request.FILES.get("resizing")
            size=float(request.POST.get("size"))
            fs=FileSystemStorage()
            filename=fs.save(image.name,image)
            filepath=fs.path(filename)
            data=cv2.imread(filepath)
            print(size)
            #resizeing image function
            data2=cv2.resize(data,None,fx=size,fy=size)           
            path=os.path.join(fs.location,"../../static/resize")
            newfilename=f"resize_{filename}.jpg"
            completePath=os.path.join(path,newfilename)
            cv2.imwrite(completePath,data2)
            print(data2)
            return render(request,'resize.html',{'lelo':newfilename})
    else:
            return render(request,"resize.html")
        
          
def rotate(request):
      if request.method=='POST':
           image=request.FILES.get("rotating")
           degree=int(request.POST.get("degree"))
           fs=FileSystemStorage()
           filename=fs.save(image.name,image)
           filepath=fs.path(filename)
           data=cv2.imread(filepath)
           print(degree)

           #function rotate
           if degree==0:
                rotate=data
           elif degree==90:
                rotate=cv2.rotate(data,cv2.ROTATE_90_CLOCKWISE)
           elif degree==180:
                rotate=cv2.rotate(data,cv2.ROTATE_180)
           elif degree==270:
                rotate=cv2.rotate(data,cv2.ROTATE_90_COUNTERCLOCKWISE)

           data2=rotate
           path=os.path.join(fs.location,"../../static/rotate")
           newfilename=f"rotate_{filename}.jpg"
           completePath=os.path.join(path,newfilename)
           cv2.imwrite(completePath,data2)
           print(data2)
           return render(request,'rotate.html',{'lelo':newfilename})
      else:
           return render(request,"rotate.html")

def signup(request):
     return render(request,'signin.html')