from main.models import Photo
from api.serializers import PhotoSerializer
from rest_framework import generics
from django.http import JsonResponse


class PhotoList(generics.ListCreateAPIView):
    """ Return Photo List or if request POST return same Photo or rotated Photo """

    def get_queryset(self):
        return Photo.objects.all()

    serializer_class = PhotoSerializer


def delete_all(request):
    """ Delete all photo from DB and clean photo list, return simple JSON response """

    Photo.objects.all().delete()

    return JsonResponse({'Delete_all': 'Confirmed'})
