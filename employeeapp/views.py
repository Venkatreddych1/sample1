from django.shortcuts import render
from .models import Employee
from .Serializers import EmployeeSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


def home(request):
    return render(request,'employee1.html')

def insert(request):
    if request.method == "GET":
       empid1=int(request.GET['x1'])
       name1= request.GET['x2']
       emp_num1=int(request.GET['x3'])
       depart1=request.GET['x4']
       E=Employee(empid=empid1,name=name1,emp_num=emp_num1,depart=depart1)
       E.save()
       return render(request,'link.html')
    else:
        return request(request,'employee1.html')

def deleteitem(request,pk):
    de=Employee.objects.filter(pk=pk)
    de.delete()
    return HttpResponse("deleted successfully")





def display(request):
    dis=Employee.objects.all()
    return render(request,'display.html',{'records':dis})


class EmployeeList(APIView):
      def get(self,request,pk,format=None):
          Employees=Employee.objects.filter(pk=pk)
          Serializers= EmployeeSerializer(Employees,many=True)
          return Response({"Employees":Serializers.data})

      def post(self, request, pk,format=None):
          emp_1 = Employee.objects.create(pk=pk)
          serializer = EmployeeSerializer(emp_1, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self,request,pk):
          event1=Employee.objects.filter(pk=pk)
          event1.delete()
          return Response({"msg":"deleted all records successfully"})


