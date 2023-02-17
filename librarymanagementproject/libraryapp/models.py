from django.db import models

# Create your models here.
class Course(models.Model):
    Course_name=models.CharField(max_length=60)
    def __str__(self):
       return f"{self.Course_name}"
class Book(models.Model):
    Book_name=models.CharField(max_length=60)
    Author_name=models.CharField(max_length=60)
    Course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.Book_name}"
class Student(models.Model):
    Student_name=models.CharField(max_length=60)
    Student_phone=models.BigIntegerField()
    Student_sem=models.IntegerField()
    Student_pswd=models.CharField(max_length=60)
    Student_Course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.Student_name}"
class Issue_Book(models.Model):
    S_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    S_Book_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    Start_date=models.DateField()
    Start_end=models.DateField()
