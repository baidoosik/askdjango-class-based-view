from django.shortcuts import render, HttpResponse, \
    get_object_or_404, redirect, Http404
from django.views import View
from .forms import PostForm
from .models import Post
from django.views.generic import (
    ListView, DetailView, CreateView,
TodayArchiveView
)
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


'''
# CBV.as_view(**init_kwargs)의 동작방식
class View(object):
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self, key, value)


    @classmethod
    def as_view(cls, **initkwargs):
        def view(request, *args, **kwargs):
            self = cls(**kwargs)
            return self.dispatch(request, *args, **kwargs)
        return view
'''

# 재사용이 가능하도록 ,cbv 패텅으로 재구현


class EditFormView(View):
    model = None
    success_url = None
    template_name = None

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.model, id=pk)

    def get_success_url(self):
        return self.success_url

    def get_template_name(self):
        return self.template_name

    def get_form(self):
        form_kwargs = {
            'instance': self.get_object()
        }
        if self.request.method == 'POST':
            form_kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILSE
            })
        return PostForm(**form_kwargs)

    def get_context_data(self, **kwargs):
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return kwargs

    def get(self, *args, **kwargs):
        return render(self.request, self.get_template_name(), self.get_context_data())

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        return render(self.request, self.get_template_name(), self.get_context_data(form=form))


post_edit = EditFormView.as_view(
    model=Post,
    success_url='/greeting',
    template_name='blog/post_form.html'
)


class PostListView(ListView):
    model = Post
    ordering = '-created_at'
    paginate_by = 10

    def head(self, *args, **kwargs):
        try:
            post = Post.objects.last()
        except Post.DoesNotExist:
            raise Http404

        response = HttpResponse()
        response['Last-Modified'] = post.created_at.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

    def delete(self, *args, **kwargs):
        raise NotImplementedError

post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

post_new = PostCreateView.as_view()


class PostTodayArchiveView(TodayArchiveView):
    model = Post
    date_field = 'created_at'
    paginate_by = 10

post_today_archive = PostTodayArchiveView.as_view()