import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(6,4),index = list(range(6)),columns = list('ABCD'))
print(df)
