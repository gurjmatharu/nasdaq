import nasdaqdatalink

data = nasdaqdatalink.get("NSE/OIL")
print(data.head())
