from rest_framework import generics, status
from rest_framework.response import Response

from api.serializers import PlateNumberSerializer

class PlatNumberDataView(generics.GenericAPIView):
    serializer_class = PlateNumberSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
