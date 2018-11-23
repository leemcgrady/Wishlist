from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class GroupView(View):

    def get(self, request):

        context = {
            "page": "group"
        }
        return render(request, 'group.html', context)


class GroupUserView(View):

    def get(self, request):

        context = {
            "page": "group"
        }
        return render(request, 'group_user.html', context)


