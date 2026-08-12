from django.shortcuts import render
from .models.course import Course
# Create your views here.


def course_list(request):  # courses
    courses = Course.objects.all()
    return render(request, "courses/courses.html", {"courses": courses})


def course_detail(request):
    courses = [
        {
            "course_title": "Django Aplicaciones",
            "course_link": "",
            "course_info": {
                "lessons": 79,
                "duration": 8,
                "instructor": "Ricardo Cuéllar",
            },
            "course_content": {
                "id": 1,
                "name": "Introducción al curso",
                "lessons": [
                    {
                        "name": "¿Qué aprenderás en este curso?",
                        "type": "video",
                    },
                    {
                        "name": "¿Cómo usar la plataforma?",
                        "type": "file",
                    },
                ],
            },
        },
        {
            "course_title": "",
            "course_link": "",
            "course_info": {
                "lessons": 40,
                "duration": 4,
                "instructor": "Ricardo Cuéllar",
            },
            "course_content": {
                "id": 2,
                "name": "Fundamentos necesarios de Python",
                "lessons": [
                    {
                        "name": "Variables y tipos de datos",
                        "type": "video",
                    },
                    {
                        "name": "Condicionales y bucles",
                        "type": "file",
                    },
                    {
                        "name": "Funciones básicas",
                        "type": "file",
                    },
                ],
            },
        },
        {
            "course_title": "",
            "course_link": "",
            "course_info": {
                "lessons": 50,
                "duration": 4,
                "instructor": "Ricardo Cuéllar",
            },
            "course_content": {
                "id": 3,
                "name": "Introducción a Django",
                "lessons": [
                    {
                        "name": "¿Qué es Django?",
                        "type": "video",
                    },
                    {
                        "name": "Primer proyecto con Django",
                        "type": "file",
                    },
                ],
            },
        },
    ]
    course_urls = {"course_link": "course_lessons", "course_image": "img/curso_2.jpg"}

    return render(
        request,
        "courses/course_detail.html",
        {"courses": courses, "course_urls": course_urls},
    )


def course_lessons(request):
    lesson = {
        "course_title": "Django: Crea aplicaciones web robustas con Python",
        "course_progress": 70,
        "course_content": [
            {
                "id": 1,
                "name": "Introducción al curso",
                "total_lessons": 6,
                "complete_lessons": 3,
                "lessons": [
                    {
                        "name": "¿Qué aprenderás en este curso?",
                        "type": "video",
                    },
                    {
                        "name": "¿Cómo usar la plataforma?",
                        "type": "file",
                    },
                ],
            },
            {
                "id": 2,
                "name": "Fundamentos necesarios de Python",
                "total_lessons": 27,
                "complete_lessons": 12,
                "lessons": [
                    {
                        "name": "Variables",
                        "type": "video",
                    },
                    {
                        "name": "Condicionales",
                        "type": "file",
                    },
                ],
            },
        ],
    }

    return render(request, "courses/course_lessons.html", {"lesson": lesson})
