from django.db import models

# Create your models here.

class Case(models.Model):
    patient_name = models.ForeignKey(
        "user.User", on_delete=models.SET_NULL, null=True, blank=True
    )
    # desease_name = models.ForeignKey(
    #     "desease.Desease", on_delete=models.SET_NULL, null=True, blank=True
    # )
    desease_name = models.CharField(max_length=255, blank=True)


class CaseSymptoms(models.Model):
    case = models.ForeignKey(
        "case.Case", on_delete=models.SET_NULL, null=True, blank=True
    )
    symptom_name = models.ForeignKey(
        "symptoms.Symptom", on_delete=models.SET_NULL, null=True, blank=True
    )