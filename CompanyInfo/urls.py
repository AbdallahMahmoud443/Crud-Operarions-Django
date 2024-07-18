from django.urls import path # type: ignore
from . import views

urlpatterns = [
   path('bulkinsert',views.BulkInsertEmployess,name="bulkInsertPage"),
   path('bulkinsertnew',views.BulkInsertEmployessNew,name="bulkInsertNewPage"),
   path('bulkupdate',views.BulkUpdateEmployee,name="bulkUpdatePage")
]
