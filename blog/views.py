from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.


class GreetingView(View):
    message = 'good day'

    def get(self, *args, **kwargs):
        return HttpResponse(self.message)

greeting = GreetingView.as_view()


class MorgingGreetingView(GreetingView):
    # 클래스 변수 재정의
    message = 'good morning'


greeting2 = MorgingGreetingView.as_view()
greeting3 = GreetingView.as_view(message='good night')
