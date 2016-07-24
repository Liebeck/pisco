# Pisco

Given a source code collection of a programmer, Pisco identifies her personality trait!

## Dependencies
* [docker](https://www.docker.com/)

## How to setup the project:
``` bash
  cd pisco
  make build
```
# Architecture
* **Pipeline:** Main pipeline that is executed for the evaluation. It will be used for 3-fold cross validation and a grid search.
* **Transformers:** Features are called transformers. Each transformer must return a [scikit-learn pipeline object](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) that will later the combined in /pisco/pipeline/pipleline.py with the main pipeline.



