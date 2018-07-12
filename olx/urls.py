from django.conf.urls import url
from django.urls import path

from olx.Views import *
from olx.views import *
app_name = 'olx'
urlpatterns =[
    url('index/', CategoryListView.as_view(), name='index'),
    url(r'^signup/$',SignUpController.as_view(),name = 'signup'),
    path('register/', SignUpController.as_view(), name='signup'),
    path('login/',LoginController.as_view(),name='login'),
    path('logout/',logout_user,name = 'logout'),
    path('test/',test,name='test'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/$', show_category, name='show_category'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/sort/$', show_category_price_dec, name='show_category_price_dec'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/add_product/$', CreateProductView.as_view(),name='add_product'),
    path('product/<int:pk>/edit/',UpdateProductView.as_view(),name='edit_product'),
    path('product/<int:pk>/delete/',DeleteProductView.as_view(),name='delete_product'),

    path('cart/',ShowCartView.as_view(),name = 'cart'),
    url(r'my-orders/',myOrders,name = 'myOrders'),
    url(r'my-posts/',my_posts,name = 'myPosts'),
    path('add_to_cart/<int:pk>/',add_toCart,name='addtoCart'),
    path('product_Info/<int:pk>/',product_info,name='productInfo'),
    path('remove_from_cart/<int:pk>/',remove_from_cart,name='removeFromCart'),
    path('return_product/<int:pk>/',return_product,name = 'returnProduct'),
    path('buy/<int:pk>/',buy,name='buy'),
    url(r'^suggest/$',suggest_product,name='suggest_product'),
    path('profile/view/<str:value>/',ProfileView.as_view(),name = "profile"),
    path('profile/add/',CreateProfileView.as_view(),name = 'profile_details_add'),
    path('profile/<int:pk>/edit/',UpdateProfileView.as_view(),name = 'profile_edit'),
    path('comment/<int:pk>/add',CreateCommentView.as_view(),name = "add_comment"),
    path('buy_confirm/<str:value>/<int:pk>/',buy_view.as_view(),name='buy_conf')

]