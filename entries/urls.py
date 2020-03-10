from django.urls import path, include
from django.conf.urls import (handler400, handler403, handler404, handler500)
from .views import HomeView, EntryView, CreateEntryView, TemplatePageNotFound


# handler400 = 'views.bad_request'
# handler403 = 'entries.views.permission_denied'
handler404 = TemplatePageNotFound.as_view()
# handler500 = 'entries.views.server_error'


urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry-detail'),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name='create-entry'),
    # path('entry/<int:pk>/', CreateCommentView.as_view(success_url='/'), name='comment-entry'),
]