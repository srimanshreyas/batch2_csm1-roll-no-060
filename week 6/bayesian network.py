import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import HillClimbSearch, BicScore, MaximumLikelihoodEstimator
f
data = pd.DataFrame({
    'Rain': [0, 1, 0, 1, 1, 0, 1, 0],
    'Sprinkler': [1, 0, 0, 1, 0, 1, 0, 1],
    'WetGrass': [1, 1, 0, 1, 1, 0, 1, 0]
})

hc = HillClimbSearch(data)
best_model = hc.estimate(scoring_method=BicScore(data))

print("Learned Structure:", best_model.edges())

model = BayesianNetwork(best_model.edges())

model.fit(data, estimator=MaximumLikelihoodEstimator)

inference = VariableElimination(model)

result = inference.query(variables=['WetGrass'], evidence={'Rain': 1})

print("\nInference Result P(WetGrass | Rain=1):")
print(result)
