# # our local import
# from entries.models import Entry
# from entries.serializers import EntrySerializer

# # the serializer import  and all that mumbo jumbo
# from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# # Create your views here.

# # class EntryViewSet(viewsets.ModelViewSet):
# #     serializer_class = EntrySerializer
# #     queryset = Entry.objects.all()


# @api_view(['GET', 'POST'])
# def api_entries_view_list(request, year, month):
#     if request.method == 'GET':
#         data = Entry.objects.all()

#         serializer = EntrySerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = EntrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'POST'])
# def request_all_entries(request):
#     if request.method == 'GET':
#         data = Entry.objects.all()

#         serializer = EntrySerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = EntrySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['PUT', 'DELETE'])
# def students_detail(request, pk):
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)