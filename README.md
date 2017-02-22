# Pisco: Personality Identification in Source Code
[![Build Status](https://travis-ci.com/Liebeck/pisco.svg?token=qYUFfiWV6mqYYR5fELB6)](https://travis-ci.com/Liebeck/pisco)

Pisco is a program that identifies the personality trait of a software developer based on his or her Java code. It was developed for the [PR-SOCO challenge 2016](http://www.autoritas.net/prsoco/). Our research paper can be accessed [here](http://ceur-ws.org/Vol-1737/T1-8.pdf).


## Abstract of our paper
We developed an approach to automatically predict the personality traits of Java developers based on their source code for the PR-SOCO challenge 2016. The challenge provides a data set consisting of source code with their associated developers' personality traits (neuroticism, extraversion, openness, agreeableness, and conscientiousness). Our approach adapts features from the authorship identification domain and utilizes features that were specically engineered for the PR-SOCO challenge. We experiment with two learning methods: linear regression and k-nearest neighbors regressor. The results are reported in terms of the Pearson product-moment correlation and root mean square error.


## Dependencies
* [docker](https://www.docker.com/)
* [knife](https://github.com/pasmod/knife) (will be automatically pulled from Docker Hub)

## How to setup the project:
This will install all required dependencies.
``` bash
cd pisco
make build
```


## How to evaluate all features
``` bash
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features all
```

## How to evaluate single features
### Style Features
``` bash
make run
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_method_names
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_method_parameter_names
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_field_names
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_local_variable_names_in_methods
```

### Structure Features
``` bash
make run
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_classes
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features cyclomatic_complexity
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_methods
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_method_parameters
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_methods
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_fields
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_local_variables_in_methods
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features duplicate_code_measure
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features contains_IDE_template_text
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features ratio_of_external_libraries
```


### Misc Features
``` bash
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_number_of_empty_classes
python evaluate.py --train_corpus=openness --recognizer=linear_regression --features ratio_of_unparsable_sections
```



## Creating Submission Files
Copy the required config file into the configs folder or a specific run and execute:
``` bash
python run.py --run_folder runs/run1
```

# Citation
I you want to cite us in your work, please use the following BibTeX entry:
``` bash
@inproceedings{pisco,
  author    = {Matthias Liebeck and
               Pashutan Modaresi and
               Alexander Askinadze and
               Stefan Conrad},
  title     = {{Pisco: {A} Computational Approach to Predict Personality Types from
               Java Source Code}},
  booktitle = {Working notes of {FIRE} 2016 - Forum for Information Retrieval Evaluation},
  pages     = {43--47},
  year      = {2016},
  url       = {http://ceur-ws.org/Vol-1737/T1-8.pdf},
},
```