from django.shortcuts import render
from django.conf import settings
from .models import Question
from .forms import QuestionForm

import wikipediaapi

# Create your views here.
def index(request):
    if request.method == 'POST':

        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                #   get question and wiki_term
                question = form.cleaned_data['question']
                wiki_terms = form.cleaned_data['wiki_terms']

                print("Question: "+question)
                print("Wiki Terms: "+wiki_terms)

                #   get wikipedia text
                wiki = wikipediaapi.Wikipedia('en')
                wiki_text = wiki.page(wiki_terms).summary

                print("Wiki Text: "+wiki_text)

                #   BERT_PIPELINE is loaded during initialization in settings
                result = settings.BERT_PIPELINE(question=question, context=wiki_text)
                print("BERT PIPELINE ran.")
                print(result)
                print(type(result))
                answer = result['answer']
                prediction_score = str(result['score'])
                
                print('Answer: '+answer)
                print("Prediction score: ")
                print(type(prediction_score))
                print('Score: '+prediction_score)

                #   save to Question model
                q = Question()
                q.wiki_terms = wiki_terms
                q.wiki_text = wiki_text
                q.question = question
                q.answer = answer
                q.prediction_score = prediction_score
                q.save()

            except:
                answer = 'There is an error.'
                prediction_score = 0
        #   render to html
        return render(request, 'main/index.html', {'form': form, 'answer': answer, 'score': prediction_score})
    
    else:
        #   e.g., with GET -> fresh form
        form = QuestionForm()
        return render(request, 'main/index.html', {'form': form})

def history(request):
    #   get all questions in database
    q=Question.objects.all()
    return render(request, 'main/history.html', {'questions': q})