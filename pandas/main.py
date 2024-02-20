import pandas as pd

dataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'data': [3, 7, 2]
}

var = pd.DataFrame(dataset)

print(var)
