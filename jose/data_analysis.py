import pandas as pd

url = "https://raw.githubusercontent.com/georgematheuslima/projeto-aeroporto/master/jose/diaria.txt?token=AOPHFUVJAOSRGVYJHTMXADS7IV7LM"
data = pd.read_csv(url, sep=" ")
print(data)
