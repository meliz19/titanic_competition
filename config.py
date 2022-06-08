# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dataset_overview(fn_csv):
	df = pd.read_csv(fn_csv)
	df.head()
