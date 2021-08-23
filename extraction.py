import pandas as pd


def extraction(url):
    data = pd.read_json(f"{url}")

    data = data[
        ["name", "id", "description", "homepage", "zipcode", "email", "employeeCount"]
    ]
    
    return data


extracted = extraction(
    "/Users/alexanderkubel/Coding/Python/reverse_engineering/WerLiefertWas/data.json"
)
print(extracted)
