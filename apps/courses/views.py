from django.shortcuts import render, get_object_or_404
from .models.course import Course
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def course_list(request):  # courses
    courses = Course.objects.all()
    
    query = request.GET.get('q')
    
    if query:
        courses = courses.filter(
            Q(title__icontains=query) | Q(owner__first_name__icontains=query)
        )
    
    paginator = Paginator(courses, 8)
    page_number = request.GET.get('page')
    courses_obj = paginator.get_page(page_number)
    
    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')
    query_string = query_params.urlencode()
    
    return render(request, "courses/courses.html", {"courses_obj": courses_obj, "query": query, "query_string": query_string})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    modules = course.modules.prefetch_related('contents')
    return render(
        request,
        "courses/course_detail.html",{
            "course": course,
            "modules":modules,
        },
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
