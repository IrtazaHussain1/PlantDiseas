from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import status
from .models import PlantDisease
# from .serializers import PridictDiseaseModelSerializer

# model import
from tensorflow.keras.models import load_model
from .CNNModel import load_image, class_name

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.


class PredictDiseaseModelView(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def get(self,request):
        return Response({"data":str(request.GET)})

    def post(self, request, *args, **kwargs):
        print(request.FILES.get("ImageFile"))

        # PlantDisease.objects.create(ImageFile=request.POST.get("ImageFile"))
        # getPath = PlantDisease.objects.latest('pk')
        # load model
        print(os.path.join(BASE_DIR,'static','model.h5'))
        model = load_model(os.path.join(BASE_DIR,'static','model.h5'))
        new_image = load_image(request.FILES['ImageFile'], True)
        ourpred = model.predict(new_image)
        
        return Response({'className',class_name(ourpred)[0]},status=200)

