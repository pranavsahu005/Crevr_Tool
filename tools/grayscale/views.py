import numpy as np
import cv2
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponse
import os

def home(request):
    """Renders the main user interface page."""
    return render(request, "user.html")

def process_image(request):
    if request.method != 'POST':
        return render(request, "user.html")

    # Determine which tool is being used from the URL
    url_path = request.path
    tool_type = url_path.strip('/').split('/')[-1] # e.g., 'grayscale', 'compress'

    # Determine the correct input name based on the tool
    input_name_map = {
        'grayscale': 'userimage',
        'compress': 'compressimg',
        'resize': 'resizing',
        'rotate': 'rotating',
        'crop': 'cropimg'
    }
    input_name = input_name_map.get(tool_type)

    image = request.FILES.get(input_name)
    if not image:
        # Handle case where no image is uploaded, though 'required' in HTML should prevent this.
        return render(request, "user.html", {'error': 'No image file found.'})

    # filesystestorage ka object banaya
    fs = FileSystemStorage()
    # file ko save karwaya
    filename = fs.save(image.name, image)
    # jaha file save hui uska address nikala
    filepath = fs.path(filename)
    # address file ko cv2 mein read karwaaya
    data = cv2.imread(filepath)

    processed_image = None
    prefix = "processed"

    if tool_type == 'grayscale':
        # grayscale mein convert kiya
        processed_image = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        prefix = "gray"
    elif tool_type == 'compress':
        # compress image function
        processed_image = data.astype("uint8")
        prefix = "comp"
    elif tool_type == 'resize':
        size = float(request.POST.get("size", 1.0))
        # resizeing image function
        processed_image = cv2.resize(data, None, fx=size, fy=size)
        prefix = "resize"
    elif tool_type == 'rotate':
        degree = int(request.POST.get("degree", 0))
        # function rotate
        if degree == 90:
            processed_image = cv2.rotate(data, cv2.ROTATE_90_CLOCKWISE)
        elif degree == 180:
            processed_image = cv2.rotate(data, cv2.ROTATE_180)
        elif degree == 270:
            processed_image = cv2.rotate(data, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            processed_image = data
        prefix = "rotate"

    # naya address banaya taki processed photo ko save kiya ja sake
    output_path = os.path.join(fs.location, f"../../static/{tool_type}")
    new_filename = f"{prefix}_{filename}.jpg"
    complete_path = os.path.join(output_path, new_filename)

    # processed matrix array ko image mein convert kiya
    cv2.imwrite(complete_path, processed_image)

    context = {'lelo': new_filename, 'tool_type': tool_type}
    return render(request, 'user.html', context)

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
          return render (request,"crop.html")

def signup(request):
     return render(request,'signin.html')