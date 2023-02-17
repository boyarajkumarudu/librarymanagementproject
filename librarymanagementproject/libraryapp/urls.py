from django.urls import path

from libraryapp import views

urlpatterns = [
    path('',views.login_fun,name='log'),
    path('logdata',views.logindata_fun),

    path('admi',views.admin_fun,name='admi'),
    path('admindata',views.admindata_fun),

    path('student',views.student_fun,name='stu'),
    path('studentdata',views.studentdata_fun),

    path('shome',views.shome_fun,name='shome'),

    path('ahome',views.adminhome_fun, name='ahome'),

    path('addbook',views.addbook_fun,name='add'),
    path('adddata',views.addbookdata_fun),

    path('displaybook',views.display_fun,name='display'),

    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>', views.del_fun, name='del'),

    path('logout',views.logout_fun,name='logo'),
    path('assign',views.assign_fun,name='ass'),
    path('assingdata',views.assingdata_fun),
    path('assreaddata', views.assreaddata_fun,name='assread'),

    path('issued', views.issueddisplay_fun,name='issu'),



    path('updt/<int:id>',views.assingdate_fun,name='updt'),
    path('dele/<int:id>',views.assingdelet_fun,name='dele'),

    path('studentreaddata',views.studentprofile_fun,name='stpro'),
    path('updateprof/<int:id>',views.updateprof_fun,name='updateprof'),

    path('sissue',views.studentissue_fun,name='sissue'),
    path('slog_out',views.slogout_fun_fun,name='slog_out')








]