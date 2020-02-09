
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def addUser(self, username, email, password, name, surname):
        new_user = User.objects.create_user(username=username,email=email,password=password,first_name=name,last_name=surname)
        if new_user:
            print("KAYIT İÇİN GEREKLİ İŞMLEMLER YAPILIYOR")
            new_user.first_name = name
            new_user.last_name = surname
            new_user.save()
            return "OK"
        else:
            return "ERROR"

    def getNameandSurname(self,username):
        UserModel = get_user_model()
        user = UserModel.objects.get(username=username)
        return user.first_name+" "+user.last_name

    def getEmail(self, username):
        UserModel = get_user_model()
        user = UserModel.objects.get(username=username)
        return user.email


    def updateUserInfo(self,username,name,surname, address , email, password, phone):
        UserModel = get_user_model()
        user = 0
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None
        user.first_name = name
        user.last_name = surname
        user.email = email
        user.password = password
        user.address = address
        user.phone = phone
        user.save()
        return "OK"
