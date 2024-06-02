from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json
import os

@csrf_exempt
def healthcheck(request):
    return HttpResponse("OK", status=200)

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            age = data['age']
            student = Student(name=name, age=age)
            student.save()

            # Створення папки, якщо вона не існує
            if not os.path.exists('./class'):
                os.makedirs('./class')

            # Збереження інформації про студента у файл
            with open(f'./class/student_{student.student_id}.json', 'w') as f:
                json.dump({'name': name, 'age': age, 'student_id': student.student_id}, f)

            return JsonResponse({'id': student.student_id}, status=201)
        except KeyError:
            return HttpResponseBadRequest("Invalid data")
    else:
        return HttpResponseBadRequest("Invalid request method")

def get_students(request):
    if request.method == 'GET':
        students = Student.objects.all().values()
        return JsonResponse(list(students), safe=False)
    else:
        return HttpResponseBadRequest("Invalid request method")

def get_student(request, student_id):
    if request.method == 'GET':
        try:
            student = Student.objects.get(student_id=student_id)
            student_data = {
                'name': student.name,
                'age': student.age,
                'student_id': student.student_id,
            }
            return JsonResponse(student_data)
        except Student.DoesNotExist:
            return HttpResponse("Student not found", status=404)
    else:
        return HttpResponseBadRequest("Invalid request method")