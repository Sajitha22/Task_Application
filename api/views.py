from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import TaskSerializer,UserSerializer
from django.contrib.auth.models import User
from api.models import Task


from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action
# Create your views here.
class TaskView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)    

class TaskDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Task.objects.get(id=id)
        serializer=TaskSerializer(qs,many=False)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Task.objects.get(id=id).delete()
        return Response(data="deleted")    


    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Task.objects.get(id=id)
        serializer=TaskSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)        



# Viewset-------------------------

class TaskViewsetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)

    
    
    def create(self,request,*args,**kwargs):
        serializer=TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 

    
    
    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializer=TaskSerializer(qs)
        return Response(data=serializer.data)


    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Task.objects.get(id=id)
        serializer=TaskSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)   



    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.get(id=id).delete()
        return Response(data="deleted")  



        # modelviewset......................................................................



class TaskModelViewsetView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    # .................
    serializer_class=TaskSerializer
    queryset=Task.objects.all()
    # ...................

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 


    def list(self, request, *args, **kwargs):
        qs=Task.objects.filter(user=request.user)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
     # override create method

    # def create(self, request, *args, **kwargs):
    #     serializer=TaskSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)





    # def list(self, request, *args, **kwargs):
    #     qs=Task.objects.all()
    #     serializer=TaskSerializer(qs,many=True)
    #     print(request.user)
    #     return Response(data=serializer.data)

       




# custom methods implementation................

    @action(methods=["GET"],detail=False)
    def finished_task(self,request,*args,**kwargs):
        qs=Task.objects.filter(status=True)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)


    @action(methods=["GET"],detail=False)
    def pending_task(self,request,*args,**kwargs):
        qs=Task.objects.filter(status=False)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)


    @action(methods=["POST"],detail=True)
    def mark_as_done(self,*args,**kwargs):
        id=kwargs.get("pk")
        Task.objects.filter(id=id).update(status=True)
        return Response(data="status deleted")    



# usermodelviewset..............................

class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all() 


        #    ..............................................pwd encription....

    # def create(self, request, *args, **kwargs):
    #    serializer=UserSerializer(data=request.data)
    #    if serializer.is_valid():
        # usr=User.objects.create_user(**serializer.validated_data)
        # sz=UserSerializer(usr,many=False)
        # return Response(sz.data)


    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
         usr=User.objects.create_user(**serializer.validated_data)
         serializerz=UserSerializer(usr,many=False)
         return Response(data=serializer.data)
        else:
             return Response(data=serializer.errors)