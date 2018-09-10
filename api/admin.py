from django.contrib import admin
from api.models import User, Lesson, StudentLesson, Student, Subject, Teacher, TeacherStudent, Document, LessonDocument

# Register your models here.
admin.site.register(User)
admin.site.register(Lesson)
admin.site.register(StudentLesson)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(TeacherStudent)
admin.site.register(Document)
admin.site.register(LessonDocument)