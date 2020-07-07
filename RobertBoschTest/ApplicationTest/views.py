from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from ApplicationTest.models import *


def login_authentication(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        if email != "" and password != "":
            try:
                is_exist = User.objects.get(email=email)
            except:
                return render(request, 'login.html', {'error': 'User Doest Not exist.'})

            is_authenticated = authenticate(username=email, password=password)
            print(is_authenticated, ">>>>>>>>>>>>>>>>>")
            if is_authenticated:
                login(request, is_authenticated)
                return HttpResponseRedirect('/quiz/')
            else:
                error = "Email or Password is incorrect."
                return render(request, 'login.html', {'error': error})

        else:
            error = "Email and Password are required."
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')


def quiz(request):
    if request.POST:
        try:
            question = Question.objects.filter(is_active=True)
            total_questions = len(question)
            correct_answer = 0
            data = {}
            for no in range(1, total_questions + 1):
                que = "question{0}".format(no)
                answ = request.POST["answer{0}".format(no)]
                question = Question.objects.get(question=request.POST[que])
                answer = Answer.objects.filter(question=question)
                for ans in answer:
                    data[ans.question] = [answ]
                    if ans.answer == answ and ans.is_true:
                        correct_answer += 1
                        data[ans.question] = data[ans.question].append(ans.answer)
                    elif ans.is_true:
                        data[ans.question] = data[ans.question].append(ans.answer)

            result = "{} Out of {} are correct answer.".format(correct_answer, total_questions)
            return render(request, 'quiz.html', {"result": result, 'data': data})
        except Exception as e:
            return render(request, 'quiz.html', {"result": str(e)})
    else:
        try:
            question = Question.objects.filter(is_active=True)
            answer = Answer.objects.all()
            return render(request, 'quiz.html', {'questions': question, 'answer': answer})
        except Exception as e:
            return render(request, 'quiz.html', {'result': str(e)})
