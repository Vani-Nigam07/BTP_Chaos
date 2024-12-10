import EntropyHub as EH
import numpy as np

def Sample_Entropy(X):
    Sample_Entropy, A, B= EH.SampEn(X)



def Fuzzy_Entropy(X):
    Fuzzy_Entropy, C, D= EH.FuzzEn(X, 2, 0.2*np.std(X))