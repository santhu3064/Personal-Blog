from django.conf.urls import url
from rvl_blog import views


urlpatterns=[url(r'^about/$',views.AboutView.as_view(),name='about'),
             url(r'^$',views.PostListView.as_view(),name='post_list'),
             url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
             url(r'^post/new/$',views.PostCreateView.as_view(),name='post_create'),
             url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_update'),
             url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='post_delete'),
             url(r'^drafts/$',views.PostDraftView.as_view(),name='post_draft_list'),
             url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comments_to_post'),
             url(r'^comment/(?P<pk>\d+)/approve/$',views.comments_approve,name='approve_comment'),
             url(r'^comment/(?P<pk>\d+)/delete/$',views.comments_remove,name='remove_comment'),
             url(r'^post/(?P<pk>\d+)/publish/$',views.publish_post,name='post_publish'),]