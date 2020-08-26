import pandas as pd

url = "https://raw.githubusercontent.com/georgematheuslima/projeto-aeroporto/master/jose/diaria.txt?token=AOPHFUX3DH2O3HRDJ36EG5C7IWCEQ"
data = pd.read_csv(url)
print(data)
