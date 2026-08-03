from django.shortcuts import render

# Create your views here.


def course_list(request):  # courses
    courses = [
        {
            "id": 1,
            "level": "Principiante",
            "rating": 4.8,
            "course_title": "Python: fundamentos hasta los detalles",
            "instructor": "Alison Walsh",
            "course_image": "img/curso_1.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/68.jpg",
        },
        {
            "id": 2,
            "level": "Principiante",
            "rating": 5.0,
            "course_title": "Django: crea aplicaciones robustas",
            "instructor": "Patty Kutch",
            "course_image": "img/curso_2.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/20.jpg",
        },
        {
            "id": 3,
            "level": "Avanzado",
            "rating": 5.0,
            "course_title": "Django: Avanzado",
            "instructor": "Alonzo Murray",
            "course_image": "img/curso_3.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/men/32.jpg",
        },
        {
            "id": 4,
            "level": "Avanzado",
            "rating": 4.8,
            "course_title": "FastAPI: Avanzado",
            "instructor": "Gregory Harris",
            "course_image": "img/curso_4.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/men/45.jpg",
        },
    ]
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
    course_urls = {
        'course_link': 'course_lessons',
        'course_image': 'img/curso_2.jpg'
    }

    return render(request, "courses/course_detail.html", {
            "courses": courses,
            "course_urls": course_urls
        }
    )


def course_lessons(request):
    return render(request, 'courses/course_lessons.html')
