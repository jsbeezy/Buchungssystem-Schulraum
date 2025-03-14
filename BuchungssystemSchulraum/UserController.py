from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserListView(View):
    def get(self, request):
        users = User.objects.all()

        # todo: hier template einfügen oder so? oder vlt lieber getAll und getById/getByName als Routen, die nur eine jsonResponse geben fürs FE
        return render(request, 'users.html', {"users": users})

class AddUserView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        hashed_password = make_password(password)
        user = User.objects.create(username=username, password=hashed_password)

        return JsonResponse({"message": "User added", "id": user.id})

class EditUserView(View):
    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        username = request.POST.get('username', user.username)
        password = request.POST.get('password')

        if password:
            user.password = make_password(password)

        user.username = username
        user.save()

        return JsonResponse({"message": "User updated", "id": user.id})

class DeleteUserView(View):
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)
        user.delete()

        return JsonResponse({"message": "User deleted"})