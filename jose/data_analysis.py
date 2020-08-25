import pandas as pd

url = "https://raw.githubusercontent.com/georgematheuslima/projeto-aeroporto/master/jose/diaria.txt?token=AOPHFUQ4XG6Z7KCBZKGP4Y27IV6PG"
data = pd.read_csv(url, encoding='latin-1')
print(data)
