from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class WishView(View):

    def get(self, request):

        context = {
            "page": "wish"
        }
        return render(request, 'wish.html', context)