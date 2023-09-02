from django.shortcuts import render, redirect
from .forms import CustomStudentForm, CustomResultsForm
from .models import Student


def check_duplicate_student(request, name, class_choice, place, school):
    try:
        existing_student = Student.objects.get(name=name, class_choice=class_choice, place=place, school=school)
        return True  # Student with the same details exists
    except Student.DoesNotExist:
        return False


global typeof


def class_view(request):
    if request.method == 'POST':
        button_value = request.POST.get('button_value', '')
        if button_value == 'basic':
            return redirect('details_page', class_type='basic')
        elif button_value == 'inter':
            return redirect('details_page', class_type='inter')
    else:
        return render(request, "class.html")


def student_details(request, class_type):
    if request.method == 'POST':
        form = CustomStudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            class_choice = form.cleaned_data['class_choice']
            place = form.cleaned_data['place']
            school = form.cleaned_data['school']
            if check_duplicate_student(request, name, class_choice, place, school):
                error_message = f"A student with the same details already exists."
                return render(request, 'details.html', {'form': form, 'error_message': error_message})
            else:
                # Redirect to the typing test page, passing the student details as parameters
                name = form.cleaned_data['name']
                class_choice = form.cleaned_data['class_choice']
                place = form.cleaned_data['place']
                school = form.cleaned_data['school']
                return redirect('test_page', name=name, class_choice=class_choice, place=place, school=school)
    else:
        form = CustomStudentForm()
        if class_type == 'basic':
            # Render the student details form page with basic class options
            class_options = range(6, 11)  # Basic class options: 6 to 10
        elif class_type == 'inter':
            # Render the student details form page with intermediate class options
            class_options = [11, 12]  # Intermediate class options: 11 and 12

        return render(request, 'details.html', {'form': form, 'class_options': class_options,'class_choice': class_type})


def test(request):
    name = request.GET.get('name')
    class_choice = request.GET.get('class_choice')
    place = request.GET.get('place')
    school = request.GET.get('school')
    if request.method == 'POST':
        try:
            form = CustomResultsForm(request.POST)
            if form.is_valid():
                data = Student(
                    name=name,
                    class_choice=class_choice,
                    place=place,
                    school=school,
                    accuracy=form.cleaned_data['accuracy'],
                    wpm=form.cleaned_data['wpm'],
                    cpm=form.cleaned_data['cpm'],
                )
                data.save()

                return redirect('results_page')
        except (BrokenPipeError, IOError) :
            print("error occurred here")
    else:
        try:
            form = CustomResultsForm()
            return render(request, 'test.html', {'form': form})
        except (BrokenPipeError, IOError):
            print("here error")


def results(request):
    if request.method == 'POST':
        return redirect('class_page')
    else:
        try:

            return render(request, 'results.html')
        except BrokenPipeError as e:
            print("error occurred here :")


def dashboard(request):
    filter_value = request.GET.get('filter')

    type_results = Student.objects.order_by('-cpm', '-accuracy', '-wpm')
    if filter_value == 'basic':
        type_results = type_results.filter(class_choice__range=(6, 10))
    elif filter_value == 'intermediate':
        type_results = type_results.filter(class_choice__in=[11, 12])

    context = {
        'results': type_results
    }

    return render(request, 'dashboard.html', context)
