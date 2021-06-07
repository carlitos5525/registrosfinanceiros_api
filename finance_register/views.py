from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from finance_register.models import Ammount, Register
from finance_register.serializers import RegisterSerializer, AmmountSerializer
from rest_framework.decorators import action
from django.http import HttpResponse, Http404, response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegisterViewSet(ModelViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        query = Register.objects.all()
        return query

    @action(methods=['put'], detail=True)
    def update_ammount(self, request, pk):
        ammount_data = request.data['ammount']
        register = Register.objects.get(id=pk)
        register_ammounts = register.ammounts.all()
        ammount_id = ammount_data['id']
        ammount = get_object_or_404(Ammount, id=ammount_id)
        if ammount in register_ammounts:
            for attr, value in ammount_data.items():
                setattr(ammount, attr, value)
            ammount.save()
            register_serialized = RegisterSerializer(register)
            json = JSONRenderer().render(register_serialized.data)
            return HttpResponse(json)
        else:
            response = HttpResponse('The ammount is not related to the finance register')
            response.status_code = 404
            return response

    @action(methods=['post'], detail=True)
    def create_ammount(self, request, pk):
        ammount_data = request.data
        register = Register.objects.get(id=pk)
        ammount_data['company_id'] = register.company_id
        ammount = Ammount.objects.create(**ammount_data)
        register.ammounts.add(ammount)
        register_serialized = RegisterSerializer(register)
        json = JSONRenderer().render(register_serialized.data)
        return HttpResponse(json)

    @action(methods=['delete'], detail=True)
    def delete_ammount(self, request, pk):
        ammount_id = request.data['id']
        register = Register.objects.get(id=pk)
        register_ammounts = register.ammounts.all()
        ammount = get_object_or_404(Ammount, id=ammount_id)
        if ammount in register_ammounts:
            ammount.delete()
            register_serialized = RegisterSerializer(register)
            json = JSONRenderer().render(register_serialized.data)
            return HttpResponse(json)
        else:
            response = HttpResponse('The ammount is not related to the finance register')
            response.status_code = 404
            return response
