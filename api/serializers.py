from rest_framework import serializers
from main.models import Photo
from .services import action_handler


class PhotoSerializer(serializers.ModelSerializer):
    """ Serialize photo model data """

    class Meta:
        model = Photo
        fields = ['photo_input', 'action']
        read_only_fields = ('id', )

    def create(self, request, *args, **kwargs):
        """ This function create Photo object and call action_handler function, return Photo-object """

        photo = Photo.objects.create(photo_input=self.validated_data['photo_input'])
        action_handler(photo, action=self.validated_data['action'])

        return photo
