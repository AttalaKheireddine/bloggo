from django.conf.urls import url
from django.urls import path,include
from blog import views

urlpatterns =[
    url(r'^about/$',views.AboutView.as_view(),name = "about"),
    url(r'^$',views.PostListView.as_view(), name ="post_list"),
    url(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(),name = "post_detail"),
    url(r'^posts/create/$',views.CreatePostView.as_view(), name = "create_post"),
    url(r'^posts/(?P<pk>\d+)/update$',views.PostUpdateView.as_view(), name = "post_edit"),
    url(r"^posts/(?P<pk>\d+)/remove$",views.PostDeleteView.as_view(), name="post_remove"),
    url(r"^posts/drafts$",views.DraftListView.as_view(),name='post_draft_list'),
    url(r"^post/comment/(?P<pk>\d+)$",views.add_comment_to_post,name = "add_comment_to_post"),
    url(r"^post/comment/(?P<pk>\d+)/approve$",views.comment_approve,name = "comment_approve"),
    url(r"^post/comment/(?P<pk>\d+)/delete$",views.remove_comment, name = "remove_comment"),
    url(r"^posts/(?P<pk>\d+)/publish$",views.publish_post,name = "publish_post")
]