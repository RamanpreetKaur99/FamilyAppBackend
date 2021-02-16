from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GroceriesSerializer, ToDoSerializer, EventSerializer, BillsSerializer
from .models import Groceries, ToDo, Event, Bills
from core.models import MyUser
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import AllowAny


# MANAGE GROCERIES
class AllGroceryItems(APIView):
    def get(self,request,username):
        try:
            user = MyUser.objects.get(username = username)
            family = user.family
            g = Groceries.objects.all()
            groceries = Groceries.objects.filter(family = family)
            serializer= GroceriesSerializer(groceries, many=True)
            return Response(serializer.data) 
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)
    
class ViewGroceryItem(APIView):
    def post(self,request,id):
        user = MyUser.objects.get(username = id)
        family = user.family
        newdata = request.data 
        newdata['family'] = family.id 
        serializer = GroceriesSerializer(data=newdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = Groceries.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

    def put(self, request, id):
        item = Groceries.objects.get(id = id)
        item.purchased = not item.purchased 
        item.save()
        return Response(status = status.HTTP_200_OK)



# MANAGE TODOs
class AllToDoItems(APIView):
    def get(self,request,username):
        try:
            user = MyUser.objects.get(username = username)
            family = user.family
            g = ToDo.objects.all()
            todo = ToDo.objects.filter(family = family)
            serializer= ToDoSerializer(todo, many=True)
            return Response(serializer.data) 
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)
    
    
class ViewToDoItem(APIView):
    def post(self,request,id):
        user = MyUser.objects.get(username = id)
        family = user.family
        newdata = request.data 
        newdata['family'] = family.id 
        serializer = ToDoSerializer(data=newdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = ToDo.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

   
    def put(self, request, id):
        item = ToDo.objects.get(id = id)
        item.completed = not item.completed 
        item.save()
        return Response(status = status.HTTP_200_OK)


#MANAGE EVENTS
class AllEvents(APIView):
    def get(self,request,username):
        try:
            user = MyUser.objects.get(username = username)
            family = user.family
            events = Event.objects.filter(family = family)
            serializer= EventSerializer(events, many=True)
            templist = []
            for i in serializer.data:
                temp = {}
                temp['title'] = i['title']
                temp['startDate'] = i['startDate']
                temp['endDate'] = i['endDate']
                temp['allDay'] = i['allDay']
                templist.append(temp) 
            return Response(templist) 
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)

class ViewEvent(APIView):
    def post(self,request, id):
        user = MyUser.objects.get(username = id)
        family = user.family
        newdata = request.data 
        newdata['family'] = family.id 
        serializer = EventSerializer(data=newdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# MANAGE BILLS
class AllBills(APIView):
    def get(self,request,username):
        try:
            user = MyUser.objects.get(username = username)
            family = user.family
            try:
                bills = Bills.objects.get(family = family)
            except:
                bills = None
            if bills==None:
                newbill = {}
                newbill['family'] = family.id 
                serializer = BillsSerializer(data=newbill)
                if serializer.is_valid():
                    serializer.save()
            print('bills',bills)
            serializer= BillsSerializer(bills)
            tempdict = {}
            for i in serializer.data:
                if i != 'id' and i != 'family':
                    tempdict[str(i)] = map(int,serializer.data[str(i)].split(' '))
            print(tempdict)
            return Response(tempdict)  
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)

class ViewBills(APIView):
    def put(self,request,id):
        newdata = {}
        print(request.data)
        for i in request.data:
            if i != 'family':
                newdata[str(i)] = ' '.join(map(str,request.data[i]))
        print(newdata)
        user = MyUser.objects.get(username = id)
        print(user)
        family = user.family
        print(family)
        temp = Bills.objects.get(family=family)
        print('jh',temp)
        temp.electricity = newdata['electricity']
        temp.maid = newdata['maid']
        temp.water = newdata['water']
        temp.gascylinder = newdata['gascylinder']
        temp.save()
        return Response(status = status.HTTP_200_OK)

        