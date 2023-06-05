from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from reader.models import Post
from student.models import Student
from .serializers import ItemSerializer, PostSerializer, StudentSerializer

# ITEMS VIEWS (FROM TUTORIAL)
@api_view(['GET'])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()

    return Response("Item deleted successfully!")


# POST VIEWS
@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return Response('Post deleted successfully!')

# STUDENT VIEWS
# GET ALL STUDENTS
@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

# GET STUDENT BY ID
@api_view(['GET'])
def getStudentById(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)

    return Response(serializer.data)


# CREATE NEW STUDENT
@api_view(['POST'])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# UPDATE STUDENT
@api_view(['POST'])
def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# DELETE STUDENT
@api_view(['DELETE'])
def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response('Item successfully deleted!')

