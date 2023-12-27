import pandas as pd

data = pd.read_csv("creditcard_2023.csv")

train_part = data.sample(frac = 0.7)
test_part  = data.drop(train_part.index)


train_part.to_csv("creditcart_train.csv")
test_part.to_csv("creditcart_test.csv")