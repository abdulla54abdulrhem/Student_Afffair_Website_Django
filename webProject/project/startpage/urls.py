from django.urls import path
from .import views

urlpatterns=[
    path('',views.WelcomePage,name="welcome"),
    path('AddStu',views.AddNewStudent,name="add"),
    path('All/<sname>',views.AllStudents,name='allSearch'),
    path('All',views.AllStudentss,name="all"),
    path('Edit/<int:theid>',views.EditStudent,name='edit'),
    path('Select/<int:theid>',views.SelectDepartment,name='select'),
    path('Search',views.Search,name="search"),
    path('Comp',views.InqComPage,name='CompInq'),
    path('CompList',views.AllComp,name='CompList')
]