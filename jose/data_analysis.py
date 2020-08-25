import pandas as pd

url = "https://raw.githubusercontent.com/georgematheuslima/projeto-aeroporto/master/jose/diaria.txt?token=AOPHFUWI4MFY6MSR3WR4RIK7IWAWA"
data = pd.read_csv(url)
print(data)
