# Pisco
[!Build Status](https://travis-ci.com/Liebeck/pisco.svg?token=qYUFfiWV6mqYYR5fELB6)](https://travis-ci.com/Liebeck/pisco)

Given a source code collection of a programmer, Pisco identifies her personality trait!

## Dependencies
* [docker](https://www.docker.com/)
* [knife](https://github.com/pasmod/knife)

## How to setup the project:
``` bash
  cd pisco
  make build
```

## How to start knife:
* Pisco automatically pulls and runs knife. It means by running ``` make run ``` knife will also start. 
* Notice: Changes in knife take 2-3 minutes to be observable by pisco!! If you want to see the changes directly, build and start knife yourself!!

# Architecture
* **Pipeline:** Main pipeline that is executed for the evaluation. It will be used for 3-fold cross validation and a grid search.

* **Transformers:** Features are called transformers. Each transformer must return a [scikit-learn pipeline object](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) that will later be combined in /pisco/pipeline/pipleline.py with the main pipeline.
* 

# How to evaluate a feature
``` bash
  make run
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features unigram
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features class_level
```



