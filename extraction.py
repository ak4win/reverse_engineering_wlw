import pandas as pd


def extraction(searchterm):
    data = pd.read_json(
        f"/Users/alexanderkubel/Coding/Python/reverse_engineering/WerLiefertWas/companies/data_{searchterm}.json"
    )

    data = data[
        [
            "name",
            "id",
            "description",
            "homepage",
            "zipcode",
            "email",
            "employeeCount",
        ]
    ]

    # Cleaning dataframe of the NaNs at the employeeCount
    data["employeeCount"] = data["employeeCount"].fillna("0")

    # Sort the dataframe descending from the number of employees
    data = data.sort_values(by=["employeeCount"], ascending=False)

    # Search and sort for a specific keyword
    # data["keyword"] = data["description"].str.find("web", 3)
    # data = data.sort_values(by=["keyword"], ascending=False)

    # export the cleaned data
    data.to_json(
        f"/Users/alexanderkubel/Coding/Python/reverse_engineering/WerLiefertWas/companies/data_{searchterm}.json"
    )

    return data
