from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from students.models import Student, MyModel

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, View
from django.urls import reverse_lazy

from students.forms import StudentForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden # нет доступа

# Create your views here.

from django.core.cache import cache

def my_view(request):
    data = cache.get('my_key')

    if not data:
        data = 'some expensive computation'
        cache.set('my_key', data, 60*15) # крайнее значение - время жизни

    return HttpResponse(data)




class PromoteStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        if not request.user.has_perm('student.can_promote_student'):
            return HttpResponseForbidden('У вас нет прав для перевода студента.')

        student.year = next_year(student.year)
        student.save()

        return redirect('students:student_list')


class ExpelStudentView(LoginRequiredMixin, View):
    def post(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        if not request.user.has_perm('student.can_expel_student'):
            return HttpResponseForbidden('У вас нет прав для исключения студента.')

        student.delete()

        return redirect('students:student_list')


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        if not self.request.user.has_perm('students.view_student'):
             return Student.objects.none()

        return Student.objects.all()



class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')


#Параметр
# request является экземпляром класса HttpRequest, который представляет запрос клиента.
# Он содержит всю информацию о запросе, такую как метод запроса (GET, POST и т. д.), данные, заголовки и прочее.

# def example_view(request):
#     """ Контроллер - пример реализации """
#     return render(request, 'app/example.html')
#
# def show_data(request):
#     """ Контроллер """
#     if request.method == 'GET':
#         return render(request, 'app/show_data.html')
#
#
# def submit_data(request):
#     """ Контроллер """
#     if request.method == 'POST':
#         return HttpResponse('Данные отправлены')
#
#
# def show_item(request, item_id):
#     """ Контроллер с параметром из маршрута """
#     return render(
#         request,
#         'app/item.html',
#         {'item_id' : item_id}
#         )

def about(request):
    """ Контроллер для about.html """
    return render(request, 'students/about.html')


def contact(request):
    """ Контроллер """
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}. Сообщение получено!')

    return render(request, 'students/contact.html')

# шаблоны

def example(request):
    """"""
    return render(request, 'students/example.html')

def index(request):
    """ Функциональный контроллер отображения информации о студенте """
    student = Student.objects.get(id=1)
    context = {
        'student_name': f'{student.first_name} {student.last_name}',
        'student_year': student.get_year_display(),
    }

    return render(request, 'students/index.html', context=context)


def student_detail(request, student_id):
    """ Функциональный контроллер отображения информации о студенте """
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }

    return render(request, 'students/detail.html', context=context)


def student_list(request):
    """"""
    students = Student.objects.all()
    context = {
        "students": students,
    }

    return render(request, 'students/student_list.html', context=context)


class MyModelCreateView(CreateView):
    """"""
    model = MyModel
    fields = ['name', 'description']
    template_name =  'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')

    def form_valid(self, form):
        """"""
        form.instance.created_by = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        """"""
        response = super().form_invalid(form)
        response.context_data['error_message'] = 'Please correct the errors'

        return response


class MyModelListView(ListView):
    """"""
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'

    def get_queryset(self):
        """"""
        # queryset = super().get_queryset().filter(is_active=True)
        # return queryset
        # Если бы у нас было поле is_active мы бы отфильтровали по значению True
        return MyModel.objects.filter(is_active=True)


class MyModelDetailView(DetailView):
    """"""
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'

    def get_additional_data(self):
        """ Метод получения дополнительных данных """
        return 'Это дополнительная информация'

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['additional_data',] = self.get_additional_data()

        return context

    def get_object(self, queryset=None):
        """ Переопределение метод"""
        obj = super().get_object(queryset)

        if not obj.is_active:
            raise Http404("Object not foud error")

        return obj

class MyModelUpdateView(UpdateView):
    """"""
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDeleteView(DeleteView):
    """"""
    model = MyModel
    template_name = 'students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('students:mymodel_list')

