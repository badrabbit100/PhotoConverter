from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Photo
from .services import validate_photo_extension, rotate_image_handler


def index(request):
    """ 1. This function render main PAGE
        2. Handle rotate action with photo
        3. Delete all photos by GET request ('delete_all')
    """

    session = request.session.session_key
    photos = Photo.objects.all().filter(session=session)

    if request.method == 'POST':
        if request.POST.get('turn_left_90') == 'True':
            rotate_image_handler(photos, angle=90)
        elif request.POST.get('turn_right_90') == 'True':
            rotate_image_handler(photos, angle=-90)
        elif request.POST.get('delete_all') == 'True':
            photos.delete()

    context = {'photos': photos}

    return render(request, 'main/index.html', context=context)


def photo_upload(request):
    """ Upload file function, validate photo format, create new object """

    if request.method == 'POST':
        my_file = request.FILES.get('file')
        if my_file is not None:
            validate_photo_extension(my_file)
            Photo.objects.create(photo_input=my_file, session=request.session.session_key)

        return HttpResponse('')

    return JsonResponse({'post': 'false'})


def photo_delete(request, pk):
    """ Function delete 1 selected photo """

    if request.method == 'GET':
        Photo.objects.get(id=pk).delete()
    return redirect('index')
