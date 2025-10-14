import cv2
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import os
from django.views.decorators.http import require_http_methods
from django.conf import settings
@require_http_methods(["GET"])
def home(request):
    """
    This view handles GET requests and renders the main user interface page.
    """
    return render(request, "user.html")


@require_http_methods(["POST"])
def process_image(request):
    """
    This view handles POST requests from the tool form to process an uploaded image.
    It determines the tool used based on the submission URL.
    """
    # Determine the tool from the path, e.g., '/compress/' -> 'compress'
    path = request.path.strip('/')
    tool_type = path

    # The name of the file input field changes based on the tool
    input_name_map = {
        'grayscale': 'userimage',
        'compress': 'compressimg',
        'resize': 'resizing',
        'rotate': 'rotating',
        'crop': 'cropimg'
    }
    input_name = input_name_map.get(tool_type)
    image_file = request.FILES.get(input_name)

    if not image_file:
        return render(request, "user.html", {'error': 'No image file was submitted.'})

    fs = FileSystemStorage()
    filename = fs.save(image_file.name, image_file)
    filepath = fs.path(filename)
    original_image = cv2.imread(filepath)
    processed_image = None
    new_filename_prefix = tool_type

    # --- Apply processing based on the tool ---
    if tool_type == 'grayscale':
        processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    elif tool_type == 'compress':
        # For compression, we just re-save the image. The quality is handled by imwrite.
        # The user's old code just saved it as is, which we will replicate.
        processed_image = original_image

    elif tool_type == 'crop':
        # Placeholder for crop functionality.
        # For now, it returns the original image. The user will add logic later.
        processed_image = original_image

    elif tool_type == 'resize':
        size = float(request.POST.get("size", 1.0))
        processed_image = cv2.resize(original_image, None, fx=size, fy=size)

    elif tool_type == 'rotate':
        degree = int(request.POST.get("degree", 0))
        rotation_map = {90: cv2.ROTATE_90_CLOCKWISE, 180: cv2.ROTATE_180, 270: cv2.ROTATE_90_COUNTERCLOCKWISE}
        rotation_code = rotation_map.get(degree)
        processed_image = cv2.rotate(original_image, rotation_code) if rotation_code is not None else original_image

    if processed_image is None:
        return render(request, "user.html", {'error': 'Invalid tool specified.'})

    # --- Save the processed image ---
    output_dir = os.path.join(settings.BASE_DIR, "static", new_filename_prefix)
    os.makedirs(output_dir, exist_ok=True)
    # Ensure the new filename has a common extension like .jpg for consistency
    new_filename = f"{new_filename_prefix}_{os.path.splitext(filename)[0]}.jpg"
    complete_path = os.path.join(output_dir, new_filename)
    cv2.imwrite(complete_path, processed_image)

    return render(request, 'user.html', {'lelo': new_filename, 'tool_type': new_filename_prefix})

def signup(request):
    return render(request, 'signin.html')