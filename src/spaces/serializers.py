from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication  
from rest_framework import permissions, routers, serializers, viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Rating, Space


class RatingSerializer(serializers.HyperlinkedModelSerializer):

    user  = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    space = serializers.PrimaryKeyRelatedField(queryset=Space.objects.all())

    class Meta:
        model  = Rating
        fields = [
            'id',
            'user',
            'space',
            'star',
            'content',
            'timestamp',
        ]


class RatingViewSet(viewsets.ModelViewSet):

    authentication_classes = [SessionAuthentication,
                              BasicAuthentication,
                              JSONWebTokenAuthentication]
    queryset               = Rating.objects.all()
    serializer_class       = RatingSerializer


class SpaceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model  = Space
        fields = [
            'id',
            'name',
            'capacity',
            'description',
            'zipcode',
            'country',
            'state',
            'city',
            'address',
            'date_added',
            'is_featured',
            'is_ours',
            'rating_set',
        ]


class SpaceViewSet(viewsets.ModelViewSet):

    authentication_classes = [SessionAuthentication,
                              BasicAuthentication,
                              JSONWebTokenAuthentication]
    permission_classes     = [permissions.IsAuthenticated, ]
    queryset               = Space.objects.all()
    serializer_class       = SpaceSerializer
