FROM pasmod/miniconder2

RUN apt-get update && \
	apt-get install -y build-essential python-dev python-matplotlib && \
	apt-get clean

RUN conda install -y \
  pip \
  numpy=1.12.0 \
  scikit-learn=0.18.1 \
  nltk=3.2.2

RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')" 

WORKDIR /var/www
ADD . .
RUN pip install -r requirements.txt
RUN pip install -e .

#RUN py.test --pep8
