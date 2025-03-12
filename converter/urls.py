from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('convert/', views.convert_file, name='convert_file'),
    path('split/', views.split, name="split"),
    path('conversion', views.conversion, name='conversion'), 
    path('convert/', views.convert_file, name='convert_file'),

    path('sdf-to-smi/', views.sdf_to_smi, name='sdf_to_smi'),
    path('sdf-smi/', views.sdf_smi, name='sdf_smi'), 

    path('smi-pdb/',views.smi_pdb, name='smi_pdb'),

    path('pdb-to-smi/',views.pdb_to_smi, name='pdb_to_smi'),
    path('pdb-smi/',views.pdb_smi, name='pdb_smi'),

    path('sdf-to-pdb/',views.sdf_to_pdb, name='sdf_to_pdb'),
    path('sdf-pdb/',views.sdf_pdb, name='sdf_pdb'),

    path('pdb-to-sdf/',views.pdb_to_sdf, name='pdb_to_sdf'),
    path('pdb-sdf/',views.pdb_sdf, name='pdb_sdf'),

    path('smi-to-mol2/',views.smi_to_mol2, name='smi_to_mol2'),
    path('smi-mol2/',views.smi_mol2, name='smi_mol2'),

    path('mol2-to-smi/',views.mol2_to_smi, name='mol2_to_smi'),
    path('mol2-smi/',views.mol2_smi, name='mol2_smi'),

    path('sdf-to-mol2/',views.sdf_to_mol2, name='sdf_to_mol2'),
    path('sdf-mol2/',views.sdf_mol2, name='sdf_mol2'),

    path('mol2-to-sdf/',views.mol2_to_sdf, name='mol2_to_sdf'),
    path('mol2-sdf/',views.mol2_sdf, name='mol2_sdf'),

    path('pdb-to-mol2/',views.pdb_to_mol2, name='pdb_to_mol2'),
    path('pdb-mol2/',views.pdb_mol2, name='pdb_mol2'),

    path('mol2_pdb/', views.mol2_pdb, name='mol2_pdb'),

    path('mol2-to-pdb/',views.mol2_to_pdb, name='mol2_to_pdb'),
  





]
