# Pisco: Personality Identification in Source Code
[![Build Status](https://travis-ci.com/Liebeck/pisco.svg?token=qYUFfiWV6mqYYR5fELB6)](https://travis-ci.com/Liebeck/pisco)

## Abstract
We developed an approach to automatically predict the personality traits of Java developers based on their source code for the PR-SOCO challenge 2016. The challenge provides a data set consisting of source code with their associated developers' personality traits (neuroticism, extraversion, openness, agreeableness, and conscientiousness). Our approach adapts features from the authorship identication domain and utilizes features that were specically engineered for the PR-SOCO challenge. We experiment with two learning methods: linear regression and k-nearest neighbors regressor. The results are reported in terms of the Pearson product-moment correlation and root mean square error.

Our paper is can be accessed [here](http://ceur-ws.org/Vol-1737/T1-8.pdf)


## Dependencies
* [docker](https://www.docker.com/)
* [knife](https://github.com/pasmod/knife) (will be automatically pulled from Docker Hub)

## How to setup the project:
This will install all required dependencies.
``` bash
  cd pisco
  make build
```
## How to Evaluate Single Features
### Style Features
``` bash
  make run
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_method_names
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_method_parameter_names
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_field_names
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features mean_length_of_local_variable_names_in_methods
```

### Style Features
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


  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features comment_length
  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features contains_suppress_warnings


  python evaluate.py --train_corpus=openness --recognizer=linear_regression --features all

```

## Hilbert Cluster Grid Search
``` bash
qsub -v dimension=agreeableness,score=RMSE,recognizer=linear_regression,njobs=20,base_path=/home/malie102/jobs/pisco,nfeatures=16 hilbert_matthias.job
```

## Creating Submission Files
Copy the required config file into the configs folder or a specific run and execute:
``` bash
python run.py --run_folder runs/run1
```

# Citation
I you want to cite us in your work, please use the following BibTeX entry:
``` bash

```




