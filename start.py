from pisco.pipeline import pipeline
from pisco.transformers import unigram
from pisco.loaders.plain_loader import load
X,Y = load(level='document', labels=['openness'])
Y = [y[0] for y in Y]
transformers = [unigram.unigram()]
p = pipeline.pipeline(transformers)
print('Success!')
print(p)



