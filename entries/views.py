from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry, Comment
from .forms import PostCommentForm
from django.template import RequestContext


class HomeView(ListView):
    model = Entry
    template_name = 'entries/base.html'
    context_object_name = 'blog_entries'
    ordering = ['-entry_date']
    paginate_by = 2


class EntryView(TemplateView):
    template_name = 'entries/entry_detail.html'

    def post(self, request, **kwargs):
        form = PostCommentForm(request.POST)
        if form.is_valid():
            post = Entry.objects.prefetch_related('comment').get(pk=kwargs['pk'])
            post.comment.create(text=form.cleaned_data['text'], entry=post, author=self.request.user)
            post.save()
            context = super(EntryView, self).get_context_data(**kwargs)
            context['entry'] = post
            context['form'] = PostCommentForm()
            return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        context['entry'] = get_object_or_404(Entry.objects.prefetch_related('comment'), pk=kwargs['pk'])
        context['form'] = PostCommentForm()
        return context


class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)


class CreateCommentView(LoginRequiredMixin, DetailView, CreateView):
    model = Comment
    template_name = 'entries/entry_detail.html'
    fields = ['comment_text']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)


# HTTP Error 404
class TemplatePageNotFound(TemplateView):
    template_name = 'entries/error_page.html'
