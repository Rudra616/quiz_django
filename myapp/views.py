# from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse

# # Create your views here.
# from .models import *

# import random
# def get_quiz(request):
#     try:
#         question_objs = list(Question.objects.all())
#         data = []
#         random.shuffle((question_objs))
       
#         for question_obj in question_objs:
#             print(question_obj.get_answers())
#             data.append({
#                 "category" : question_obj.category.category_name,
#                 "question" : question_obj.question,
#                 "marks" : question_obj.marks,
#                 "answer" : question_obj.get_answers()
#             })

#         # payload = {'data':data}
#         payload = { 'status' : True , 'data' : data }
#         return JsonResponse(payload)

#     except Exception as e:
#         print(e)
#     return HttpResponse("something was wrong")
from django.shortcuts import render, redirect
from .models import Question, Ans, Category
import random

def home(request):
    context = {'category': Category.objects.all()}  # Provide categories to the home page
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")  # Redirect to quiz page with selected category
    return render(request, 'home.html', context)



from django.shortcuts import render, redirect
from .models import Question, Ans, Category

def quiz(request):
    if request.method == "POST":
        questions = Question.objects.filter(category__category_name=request.GET.get('category'))
        total_questions = questions.count()
        correct_answers = 0
        results = []

        for question in questions:
            user_answer = request.POST.get(f"question_{question.uid}")  # Get user's answer
            if user_answer:  # Check if an answer was provided
                correct_ans = Ans.objects.filter(question=question, iscorrect=True).first()
                user_answer_obj = Ans.objects.filter(uid=user_answer).first()

                # Check if both correct_ans and user_answer_obj exist
                if correct_ans and user_answer_obj:
                    is_correct = correct_ans.uid == user_answer_obj.uid
                    if is_correct:
                        correct_answers += 1
                    results.append({
                        "question": question.question,
                        "correct_answer": correct_ans.ans,
                        "user_answer": user_answer_obj.ans,
                        "is_correct": is_correct,
                    })
                else:
                    # Handle cases where the correct answer or user answer is missing
                    results.append({
                        "question": question.question,
                        "correct_answer": correct_ans.ans if correct_ans else "N/A",
                        "user_answer": "No Answer",
                        "is_correct": False,
                    })

        marks = correct_answers  # 1 mark per correct answer

        context = {
            "total_questions": total_questions,
            "correct_answers": correct_answers,
            "marks": marks,
            "results": results,
        }
        return render(request, "result.html", context)

    questions = Question.objects.filter(category__category_name=request.GET.get('category'))
    context = {"questions": questions}
    return render(request, "quiz.html", context)
