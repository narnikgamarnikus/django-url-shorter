from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from .models import URL
from django.shortcuts import redirect


class URLListView(LoginRequiredMixin, ListView):

    model = URL

    def get_queryset(self):
        queryset = super(URLListView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class URLCreateView(LoginRequiredMixin, CreateView):

    model = URL
    fields = ['long_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(URLCreateView, self).form_valid(form)


class URLDetailView(LoginRequiredMixin, DetailView):

    model = URL
    pk_url_kwarg = 'short_url'
    slug_field = 'short_url'
    slug_url_kwarg = 'short_url'


class URLRedirectView(DetailView):

    model = URL
    pk_url_kwarg = 'short_url'
    slug_field = 'short_url'
    slug_url_kwarg = 'short_url'

    def get(self, *args, **kwargs):
        obj = self.get_object()
        return redirect(obj.long_url)

'''
class UserURLListView(LoginRequiredMixin, ListView):

    model = UserURL

    def get_queryset(self):
        queryset = super(UserURLListView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class UserURLCreateView(LoginRequiredMixin, CreateView):

    model = UserURL
    fields = ['long_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserURLCreateView, self).form_valid(form)


class UserURLDetailView(LoginRequiredMixin, DetailView):

    model = UserURL
    pk_url_kwarg = 'short_url'
    slug_field = 'short_url'
    slug_url_kwarg = 'short_url'


class UserURLRedirectView(LoginRequiredMixin, DetailView):

    model = UserURL
    pk_url_kwarg = 'short_url'
    slug_field = 'short_url'
    slug_url_kwarg = 'short_url'

    def get(self, *args, **kwargs):
        obj = self.get_object()
        return redirect(obj.long_url)
'''
