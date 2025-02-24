from django.urls import include, path

from classes.views import class_assessment_views, classes_views, class_students_views, views

urlpatterns = [
    # CLASS ROUTES
    path("classes/", views.list_classes, name="class-list"),
    path("classes/new/", views.new_class, name="class-new"),

    path("classes/<str:class_pk>/", views.show_class, name="class-show"),
    path("classes/<str:class_pk>/edit/", views.update_class, name="class-edit"),
    path("classes/<str:class_pk>/delete/", views.delete_class, name="class-delete")
]
