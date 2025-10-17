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
    
        return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'takephoto'})
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
            return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'compress'})
        else:
            return render(request,"user.html")
        
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
            return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'resizing'})
    else:
            return render(request,"user.html")
        
          
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
           return render(request,'user.html',{'lelo':newfilename, 'tool_name': 'rotatephoto'})
      else:
           return render(request,"user.html")

def signin(request):
     return render(request,'signin.html')

def myclick(event,x,y,flag,param):
     ptr1=[]
     count=0
     height=250
     width=350
     data=cv2.imread(filepath)
     if(event==cv2.EVENT_LBUTTONDOWN):
        count+=1
        if(count==5):
            count=1
            data=cv2.imread(filepath)
            ptr1=[]
        cv2.circle(center=(x,y),color=(0,255,0),img=data,thickness=2,radius=2)
        ptr1.append((x,y))
        if(count==4):
            cv2.line(data,ptr1[0],ptr1[1],(0,255,0),2)
            cv2.line(data,ptr1[1],ptr1[2],(0,255,0),2)
            cv2.line(data,ptr1[2],ptr1[3],(0,255,0),2)
            cv2.line(data,ptr1[3],ptr1[0],(0,255,0),2)

            ptr2=[
                [0,0],[0,height],[width,height],[width,0]
            ]
            matrix=cv2.getPerspectiveTransform(src=np.float32(ptr1),dst=np.float32(ptr2))
            cropped=cv2.warpPerspective(src=data,M=matrix,dsize=[width,height])
            cv2.imshow("Cropper",cropped)
            fs=FileSystemStorage()
            path=os.path.join(fs.location,"../../static/wrap")
            newfilename=f"crop_{filename}.jpg"
            completePath=os.path.join(path,newfilename)
            cv2.imwrite(completePath,cropped)
            cv2.imshow("dekho",cropped)
            print("done")
          #   return render(request,'crop.html',{'lelo':newfilename})
def Crop(request):
     global filename,filepath,data

     if request.method=='POST':
          image=request.FILES.get("crop")
          fs=FileSystemStorage()
          filename=fs.save(image.name,image)
          filepath=fs.path(filename)
          data=cv2.imread(filepath)
          cv2.namedWindow("rummy")
          cv2.setMouseCallback("rummy",myclick)
          while(True):
               cv2.imshow("rummy",data)
               if(cv2.waitKey(20)==ord('a')):
                    break
          cv2.destroyAllWindows()
          return HttpResponse("done")
     else:
          return render (request,"user.html")