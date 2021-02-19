from rest_framework.viewsets import ModelViewSet, GenericViewSet

from ..models.users import MyUser
from ..serializers.users import MyUserSerializer


class MyUserViewSet (ModelViewSet):
    # queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_queryset(self):
        if (self.kwargs.get('username')):
            return MyUser.objects.filter(username=self.kwargs.get('username'))
        return MyUser.objects.all()
