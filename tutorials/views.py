from rest_framework.response import Response
from tutorials.models import Tutorial
from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def apitest(request):
    return Response("Only API test")

@api_view(['GET'])
def listTutorial(request):
    tutorials = Tutorial.objects.all()
    serializer = TutorialSerializer(tutorials, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detailTutorial(request, pk):
    tutorials = Tutorial.objects.get(id=pk)
    serializer = TutorialSerializer(tutorials, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTutorial(request):
    serializer = TutorialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTutorial(request, pk):
    tutorials = Tutorial.objects.get(id=pk)
    serializer = TutorialSerializer(instance=tutorials, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTutorial(request, pk):
    tutorials = Tutorial.objects.get(id=pk)
    tutorials.delete()
    return Response("Tutorial deleted", status=204)




# Create your views here.
