# wikipedia_BERTbot
Q&A BERT Django app which searches a Wikipedia page for answers

## Introduction
This is a simple Django webapp which searches for an answer from a question and Wikipedia page query. This app is powered by the BERT Q&A model provided by <a href='https://huggingface.co/docs/transformers/index'>Hugging Face</a> and the <a href='https://pypi.org/project/Wikipedia-API/'>Wikipedia API</a>.

<img src="https://github.com/ArnoldYSYeung/wikipedia_BERTbot/blob/main/images/interface.PNG" width="600"/>

The webapp also shows past queries through `/history`.

<img src="https://github.com/ArnoldYSYeung/wikipedia_BERTbot/blob/main/images/history.png" width="600"/>

## Requirements
You need the following libraries to run this webapp:
- <a href='https://www.djangoproject.com/download/'>Django 3.2.9</a>
- <a href='https://huggingface.co/docs/transformers/installation'>Transformers</a>
- <a href='https://pypi.org/project/Wikipedia-API/'>Wikipedia API</a>

## Initialization
Go to `wikipedia_BERTbot/bertbot` and run the following: `python3 manage.py runserver`.

