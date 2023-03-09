from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Test, Answer
from .utils import *

def index(request):
    return render(request, 'home/index.html')

@login_required
def mbti_test(request):
    questions = Test.objects.all()
    context = {'questions': questions}
    return render(request, 'home/mbti_test.html', context)

@login_required
def results(request):
    if request.method == 'POST':
        user = request.user
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                test = Test.objects.get(id=question_id)
                response = {'answer': value}
                answer = Answer(test=test, user=user, response=response)
                answer.save()
        # Calculate MBTI result
        mbti_result = calculate_mbti_result(user)
        return render(request, 'home/results.html', {'mbti_result': mbti_result})
    else:
        return render(request, 'home/mbti_test.html')