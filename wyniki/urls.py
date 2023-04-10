from django.urls import path
from wyniki import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("wyniki/<name>/add", views.add_results, name="add_results"),
    path("wyniki/<name>/create_study", views.create_study, name="create_study"),
    path("wyniki/<name>/edit/<result_id>", views.edit_results, name="edit_results"),
    path("wyniki/<name>/see/<result_id>", views.see_results, name="see_results"),
    path("wyniki/<name>/history", views.history, name="history"),
    path("register_patient/", views.register_patient, name="register_patient"),
    path("register_doctor/", views.register_doctor, name="register_doctor"),
    path("register_patient/create_patient", views.create_patient, name="create_patient"),
    path("register_doctor/create_doctor", views.create_doctor, name="create_doctor"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)