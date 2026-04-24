import numpy as np
from hmmlearn import hmm


observations = np.array([
    [0], [1], [2], [1], [0],
    [1], [2], [2], [1], [0]
])

model = hmm.MultinomialHMM(n_components=2, n_iter=100, random_state=42)


model.fit(observations)


hidden_states = model.predict(observations)

print("Hidden states sequence:")
print(hidden_states)


print("\nStart probabilities:")
print(model.startprob_)

print("\nTransition matrix:")
print(model.transmat_)

print("\nEmission probabilities:")
print(model.emissionprob_)


log_prob = model.score(observations)
print("\nLog likelihood of the observation sequence:")
print(log_prob)
