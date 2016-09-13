# Pisco: Personality Identification in Source Code
[![Build Status](https://travis-ci.com/Liebeck/pisco.svg?token=qYUFfiWV6mqYYR5fELB6)](https://travis-ci.com/Liebeck/pisco)

Given a source code collection of a programmer, Pisco identifies her personality trait!

## Dependencies
* [docker](https://www.docker.com/)
* [knife](https://github.com/pasmod/knife) (will be automatically pulled from Docker Hub)

## How to setup the project:
This will install all required dependencies.
``` bash
  cd pisco
  make build
```
## How to Evaluate a Feature
``` bash
  make run
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features word_unigram
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features class_level
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_methods_per_class
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_methods_per_class
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features ratio_of_external_libraries
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_function_parameters_per_class
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_function_name_length
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_function_parameter_name_length
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features sum_number_of_empty_classes
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features ratio_of_unparsable_sections
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features contains_IDE_template_text
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_fields_per_class
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features all

```

## Workflow
``` bash
  git pull
```

(optionally ``` make build```)

``` bash
  make run
```

evaluate (see [How to evaluate a feature](#how-to-evaluate-a-feature))

If you want to push your changes you follow these steps:

``` bash
make run
py.test --pep8
git status
git add 'path'
git commit -m 'message'
git push
 ```
