from pisco.pipeline import pipeline
from pisco.transformers.class_level import class_level
from pisco.loaders.plain_loader import load

# Load files
X, Y = load(labels=['openness'])
# Y = [y[0] for y in Y]
transformers = [class_level()]
p = pipeline.pipeline(transformers)

# Test prediction
p.fit(X, Y)
result = p.predict(X)
print('\nSuccess!')
