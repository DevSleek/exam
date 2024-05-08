from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class District(BaseModel):
    title = models.CharField(max_length=256)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )

    def __str__(self):
        return self.title


class School(BaseModel):
    title = models.CharField(max_length=256)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="schools"
    )

    def __str__(self):
        return self.title


class Student(BaseModel):
    name = models.CharField(max_length=256)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return self.name


class Test(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="tests")
    percentage = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.percentage)