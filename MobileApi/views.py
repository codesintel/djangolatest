from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import RecommendedItems
from rest_framework.views import APIView
from .serializers import RecommendedItemsSerializer
#from mysite import settings as stcd
import smtplib
import turicreate as tc
import settings as setting
# Create your views here.


class ItemsUserApi(APIView):
    def get(self,request):
        x=RecommendedItems()
        x.ItemID="111"
        x.ItemName="222"
        x.TimeStamp="222"
        model=tc.load_model("my_model.model")
        model
        serializer=RecommendedItemsSerializer(x)
        return Response(serializer.data)
    def post(self):
        pass





