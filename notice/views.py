from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import views
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from .permissions import IsTFOrReadOnly


class NoticeListView(views.APIView):
    serializer_class = NoticeSerializer
    permission_classes = [IsTFOrReadOnly]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message': 'TF 공지 작성 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return Response({'message': 'TF 공지 작성 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        notices = Notice.objects.all().order_by('-created_at')
        serializer = self.serializer_class(notices, many=True)
        
        return Response({'message': 'TF 공지 목록 조회 성공', 'data': serializer.data})
