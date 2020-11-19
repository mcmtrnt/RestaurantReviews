# Author: Trent McMillan
# Description: Aspect-Based Sentiment Analysis for Restaurant Reviews.

from django.conf import settings
from django_mako_plus import view_function, jscontext
import requests
import re
import collections
import time
import nltk
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sklearn
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import stanza
from django.http import HttpResponse
from homepage import models as hmod
from collections import Counter
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.text import Text

wnl = WordNetLemmatizer()


def is_food(word):
    syns = wordnet.synsets(word, pos=wordnet.NOUN)
    for syn in syns:
        if 'food' in syn.lexname():
            return 1
    return 0

# Words that indicate the review is about customer service.
custServ = ["service", "worker", "workers", "employee", "employees",
            "manager", "managers", "staff", "cashier", "server",
            "serve", "served", "he", "she", "friendly", "quickly",
            "people", "person", "polite", "efficient",
            "customer", "quick", "personable", "helpful", "courteous",
            "greeting", "respect", "respectful", "apologetic",
            "prompt", "greet", "attentive", "competent", "smile",
            "smiles", "rude", "obnoxious", "rudely", "curt",
            "attitude", "unprofessional", "racist", "indifferent",
            "incompetent", "incompetency", "clueless", "uncaring",
            "nobody", "ignored", "disrespect", "disrespectful",
            "inconsiderate", "rush", "rushed", "rushing", "impatient",
            "audacity", "forgot", "forget", "lie", "lied", "liar",
            "argue", "argued", "waiter", "waitress"]

# Words that indicate positive sentiment towards customer service.
posCustServ = ["friendly", "polite", "efficient", "satisfied",
               "nice", "nicest", "nicer", "professional", "personable",
               "kind", "kindly", "helpful", "organized",
               "quick", "quickly", "extra", "help", "helping", "fast",
               "faster", "fastest", "clean", "greet", "greeting",
               "courteous", "genuine",
               "respect", "respectful", "bright", "consistent",
               "consistently", "apologetic", "apologize", "apologized",
               "prompt", "precise", "5", "fab", "fabulous", "safe",
               "impeccable", "delightful", "delight", "delighted",
               "promptly", "pleasant", "pleasantly", "comfortable",
               "attentive", "sweet", "recommendations", "patient",
               "superstar", "competent", "smile", "smiles", "smiled",
               "kindness", "pleasure", "beautiful", "bravo", "happy",
               "incredible", "great", "good", "chill", "cared"]

# Words that indicate negative sentiment towards customer service.
negCustServ = ["rude", "rudely", "wait", "waiting", "waited",
               "dissatisfaction", "dissatisfied", "forgot", "forget",
               "missing", "trouble", "busy", "obnoxious", "poor",
               "poorly", "dissapointed", "waste", "messed",
               "forever", "awful", "terrible", "curt", "excuse",
               "complain", "complained", "complaining", "joke",
               "joking", "joked", "uptight", "loud", "loudly",
               "dissapointment", "unfriendly", "bothered", "yell",
               "yelled", "wrong", "bad", "pissed", "angry", "impolite",
               "unpleasant", "disagreeable", "offensive", "crude",
               "filthy", "regret", "attitude", "short", "unprofessional",
               "swear", "care", "worst", "yanked", "racist",
               "hate", "indifferent", "incompetent", "incompetency",
               "displeasure", "clueless", "screwed", "uncaring",
               "paralyzed", "anxiety", "error", "sad", "saddened",
               "saddens", "sadly", "frustrating", "frustrated",
               "overwhelming", "overwhelmed", "nobody", "ignored",
               "negative", "disrespectful", "piss", "inconsiderate",
               "shit", "shitty", "train", "trained", "training",
               "rush", "rushed", "rushing", "impatient", "mental",
               "hell", "screw", "fail", "failed", "confused", "cry",
               "crying", "unfortunate", "minute", "minutes", "slow",
               "concerned", "laughing", "audacity", "baffled",
               "unfortunately", "embarrass", "embarrassed", "condescending",
               "reprimanded", "reprimand", "stupid",
               "suck", "sucks", "lazy", "liar", "lie", "lied", "argue",
               "argued", "spit", "ridiculous"]

# Words that indicate the review is about covid safety
covid = ["covid", "covid19", "covid-19", "corona", "coronavirus", "virus",
         "rona", "mask", "masks", "sanitizer", "distancing", "cover",
         "mouth", "mouths", "nose", "noses", "cough", "coughed", "coughing",
         "coughs"]


@view_function
def process_request(request):

    sid = SentimentIntensityAnalyzer()
    ChickfilAReviews = hmod.Reviews.objects.filter(restaurant='Chick-fil-A')

    # The general sentiment score with VADER
    genSent = []
    for r in ChickfilAReviews:
        sent_text = nltk.sent_tokenize(r.review)
        for sent in sent_text:
            ss = sid.polarity_scores(sent)
            genSent.append(ss['compound'])
    genSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)
    print(genSentVader)

    # Identify which sentences belong in each category
    foodWords = Counter()
    foodQualSent = set()
    custServSent = set()
    covidSent = set()
    words = []
    text = ''

    for r in ChickfilAReviews:
        text += r.review
        sent_text = nltk.sent_tokenize(r.review)
        for sent in sent_text:
            tWords = nltk.word_tokenize(sent)
            for t in tWords:
                words.append(t)
                if(t in custServ):
                    custServSent.add(sent)
                if(t in covid):
                    covidSent.add(sent)
                if(is_food(t)):
                    foodWords[str(wnl.lemmatize(t.lower()))] += 1
                    foodQualSent.add(sent)

    # Find the most common bigrams
    col = Text(words).collocation_list()
    col2 = []
    for c in col:
        mybool = False
        tWords = nltk.word_tokenize(c)
        for t in tWords:
            if(is_food(t)):
                mybool = True
        if mybool:
            col2.append(c)

    foodBigrams = Counter()
    bigramFoodDict = {}
    # Find which sentences have the most common bigrams
    sent_text = nltk.sent_tokenize(text)
    for c in col2:
        foodBigramSentences = set()
        for sent in sent_text:

            if c.lower() in sent.lower():
                foodBigramSentences.add(sent.lower())
                foodBigrams[str(c.lower())] += 1
        bigramFoodDict[c.lower()] = foodBigramSentences

    # Only include bigrams that occur at least 3 times
    col3 = []
    for w, i in foodBigrams.most_common(10):
        if(i > 2):
            col3.append(w)

    # Find the sentiment scores for each bigram
    bigramSentiment = {}
    for f in col3:
        foodSent = []
        for s in bigramFoodDict[f.lower()]:
            ss = sid.polarity_scores(s)
            foodSent.append(ss['compound'])
        if(len(foodSent) > 0):
            calc = round((1 + (sum(foodSent) / len(foodSent))) / 2, 3)
            bigramSentiment[f.lower()] = calc

    # Find the most common food mentions
    commonFoods = []
    for f, i in foodWords.most_common(10):
        commonFoods.append(f)

    # Remove duplicate words
    removeThese = []
    for c in col3:
        for f in commonFoods:
            if(f in c):
                removeThese.append(f)
    l3 = [x for x in commonFoods if x not in removeThese]

    # Gather all of the sentences for the most common food mentions
    commonFoodDict = {}
    for f in l3:
        fsentences = set()
        for r in ChickfilAReviews:
            sent_text = nltk.sent_tokenize(r.review)
            for sent in sent_text:
                tWords = nltk.word_tokenize(sent)
                for t in tWords:
                    if(wnl.lemmatize(t.lower()) == f):
                        fsentences.add(sent)
        commonFoodDict[f] = fsentences

    # Find sentiment scores for each of the most common foods
    commonSentiment = {}
    for f in l3:
        foodSent = []
        for s in commonFoodDict[f]:
            ss = sid.polarity_scores(s)
            foodSent.append(ss['compound'])
        calc = round((1 + (sum(foodSent) / len(foodSent))) / 2, 3)
        commonSentiment[f] = calc

    # Merge the two dictionaries
    commonSentiment.update(bigramSentiment)
    cf1 = sorted(commonSentiment.items(), key=lambda x: x[1], reverse=True)

    # VADER sentiment analysis for sentences relating to customer service
    genSent = []
    for s in custServSent:
        ss = sid.polarity_scores(s)
        genSent.append(ss['compound'])
    custServSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)

    # VADER sentiment analysis for sentences relating to food quality
    genSent = []
    for s in foodQualSent:
        ss = sid.polarity_scores(s)
        genSent.append(ss['compound'])
    foodQualSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)

    # VADER sentiment analysis for sentences relating to covid
    genSent = []
    for s in covidSent:
        ss = sid.polarity_scores(s)
        genSent.append(ss['compound'])
    covidSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)

    context = {
        'genSentVader': genSentVader,
        'custServSentVader': custServSentVader,
        'foodQualSentVader': foodQualSentVader,
        'covidSentVader': covidSentVader,
        'commonFoods': cf1,
    }
    return request.dmp.render('index.html', context)


@view_function
def calculate(request, name, column):
    sid = SentimentIntensityAnalyzer()

    ChickfilAReviews = hmod.Reviews.objects.filter(restaurant=name)

    # The general sentiment score with VADER
    genSent = []
    for r in ChickfilAReviews:
        sent_text = nltk.sent_tokenize(r.review)
        for sent in sent_text:
            ss = sid.polarity_scores(sent)
            genSent.append(ss['compound'])
    genSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)
    print(genSentVader)

    # Identify which sentences belong in each category
    foodWords = Counter()
    foodQualSent = set()
    custServSent = set()
    covidSent = set()
    words = []
    text = ''

    for r in ChickfilAReviews:
        text += r.review
        sent_text = nltk.sent_tokenize(r.review)
        for sent in sent_text:
            tWords = nltk.word_tokenize(sent)
            for t in tWords:
                words.append(t)
                if(t in custServ):
                    custServSent.add(sent)
                if(t in covid):
                    covidSent.add(sent)
                if(is_food(t)):
                    foodWords[str(wnl.lemmatize(t.lower()))] += 1
                    foodQualSent.add(sent)

    # Find the most common bigrams
    col = Text(words).collocation_list()
    col2 = []
    for c in col:
        mybool = False
        tWords = nltk.word_tokenize(c)
        for t in tWords:
            if(is_food(t)):
                mybool = True
        if mybool:
            col2.append(c)

    foodBigrams = Counter()
    bigramFoodDict = {}
    # Find which sentences have the most common bigrams
    sent_text = nltk.sent_tokenize(text)
    for c in col2:
        foodBigramSentences = set()
        for sent in sent_text:

            if c.lower() in sent.lower():
                foodBigramSentences.add(sent.lower())
                foodBigrams[str(c.lower())] += 1
        bigramFoodDict[c.lower()] = foodBigramSentences

    # Only include bigrams that occur at least 3 times
    col3 = []
    for w, i in foodBigrams.most_common(10):
        if(i > 2):
            col3.append(w)

    # Find the sentiment scores for each bigram
    bigramSentiment = {}
    for f in col3:
        foodSent = []
        for s in bigramFoodDict[f.lower()]:
            ss = sid.polarity_scores(s)
            foodSent.append(ss['compound'])
        if(len(foodSent) > 0):
            calc = round((1 + (sum(foodSent) / len(foodSent))) / 2, 3)
            bigramSentiment[f.lower()] = calc

    # Find the most common food mentions
    commonFoods = []
    for f, i in foodWords.most_common(10):
        commonFoods.append(f)

    # Remove duplicate words
    removeThese = []
    for c in col3:
        for f in commonFoods:
            if(f in c):
                removeThese.append(f)
    l3 = [x for x in commonFoods if x not in removeThese]

    # Gather all of the sentences for the most common food mentions
    commonFoodDict = {}
    for f in l3:
        fsentences = set()
        for r in ChickfilAReviews:
            sent_text = nltk.sent_tokenize(r.review)
            for sent in sent_text:
                tWords = nltk.word_tokenize(sent)
                for t in tWords:
                    if(wnl.lemmatize(t.lower()) == f):
                        fsentences.add(sent)
        commonFoodDict[f] = fsentences

    # Find sentiment scores for each of the most common foods
    commonSentiment = {}
    for f in l3:
        foodSent = []
        for s in commonFoodDict[f]:
            ss = sid.polarity_scores(s)
            foodSent.append(ss['compound'])
        calc = round((1 + (sum(foodSent) / len(foodSent))) / 2, 3)
        commonSentiment[f] = calc

    # Merge the two dictionaries
    commonSentiment.update(bigramSentiment)
    cf1 = sorted(commonSentiment.items(), key=lambda x: x[1], reverse=True)

    # VADER sentiment analysis for sentences relating to customer service
    genSent = []
    for s in custServSent:
        ss = sid.polarity_scores(s)
        genSent.append(ss['compound'])
    custServSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)

    # VADER sentiment analysis for sentences relating to food quality
    genSent = []
    for s in foodQualSent:
        ss = sid.polarity_scores(s)
        genSent.append(ss['compound'])
    foodQualSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)

    # VADER sentiment analysis for sentences relating to covid
    genSent = []
    for s in covidSent:
        ss = sid.polarity_scores(s)
        genSent.append(ss['compound'])
    covidSentVader = round((1 + (sum(genSent) / len(genSent))) / 2, 3)

    context = {
        'genSentVader': genSentVader,
        'custServSentVader': custServSentVader,
        'foodQualSentVader': foodQualSentVader,
        'covidSentVader': covidSentVader,
        'commonFoods': cf1,
        'name': name,
        'column': column,
    }

    return request.dmp.render('/homepage/templates/index.charts.html', context)
