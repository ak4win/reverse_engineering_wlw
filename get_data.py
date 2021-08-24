import requests
import json

from extraction import extraction


def request_companies(page, searchterm):
    url = "https://www.wlw.de/unified_search_backend/graphql"

    payload = {
        "query": "query ($ufsSessionId: String, $searchMethod: String, $q: String, $conceptSlug: String, $citySlug: String, $filters: [FilterInput!], $page: Int, $sort: String, $disableCityExtraction: Boolean, $cityExtractionRadius: String) {\n  search(ufsSessionId: $ufsSessionId, searchMethod: $searchMethod, q: $q, conceptSlug: $conceptSlug, citySlug: $citySlug, filters: $filters, page: $page, sort: $sort, disableCityExtraction: $disableCityExtraction, cityExtractionRadius: $cityExtractionRadius) {\n    ufsSessionId\n    paging {\n      total\n      currentPage\n      totalPages\n    }\n    companies {\n      id\n      uuid\n      name\n      highlightedName\n      description\n      highlightedDescription\n      secondaryHighlightedDescription\n      homepage\n      zipcode\n      city\n      countryCode\n      certificates\n      logoPath\n      profilePagePath\n      distance\n      email\n      debugData\n      employeeCount\n      foundingYear\n      acronym\n      customerId\n      isCustomer\n      fpaket\n      spaceType\n      pictures {\n        caption\n        path\n        position\n        sizes\n      }\n      logo {\n        sizes\n      }\n      filterResults {\n        key\n        title\n        value\n        matches\n      }\n      matchingCompanyCategory {\n        id\n        kpaket\n        toprankingPosition\n      }\n    }\n    cities {\n      slug\n      title\n      count\n    }\n    suggestions {\n      text\n      score\n    }\n    extractedCity {\n      name\n      radius\n    }\n    toprankingPositions {\n      companyId\n      position\n    }\n    companyCategory {\n      id\n      name\n    }\n    concept {\n      title\n    }\n    recommendations {\n      text\n      score\n      slug\n    }\n    canonicalConceptSlug\n    canonicalCompanyCategorySlug\n    conceptSlugTitle\n    companyCategorySlugTitle\n    verticalSlug\n    citySlugTitle\n    seoTextHtml\n    debugData\n  }\n}\n",
        "variables": {
            "ufsSessionId": "",
            "searchMethod": "direct",
            "locale": "de",
            "q": searchterm,
            "filters": [],
            "page": page,
            "sort": "best",
            "disableCityExtraction": False,
            "cityExtractionRadius": "50km",
        },
    }
    headers = {
        "cookie": "wlw_client_id=rBEAEGEiVlmZ2gEBA9N4Ag%3D%3D",
        "authority": "www.wlw.de",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "x-original-url": "https://www.wlw.de/de/suche/page/3?q=Software",
        "x-application-id": "unified-search-frontend",
        "x-referer": "https://www.wlw.de/de/suche/page/2?q=Software",
        "origin": "https://www.wlw.de",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.wlw.de/de/suche/page/3?q=Software",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,hr;q=0.4",
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    return json.loads(response.text)


def print_company(company):
    print(f"{company['name']}, {company['employeeCount']}")


searchterms = ["cybersecurity", "it-security"]


def get_data_from_seachterms():
    for searchterm in searchterms:
        page = 1
        all_compaines = []

        while True:
            response = request_companies(page, searchterm)

            companies = response["data"]["search"]["companies"]
            total_pages = response["data"]["search"]["paging"]["totalPages"]

            print(f"\n--- page {page} out of {total_pages} ---")

            for company in companies:
                all_compaines.append(company)
                print_company(company)

            page += 1

            if page > total_pages:
                break

        with open(f"companies/data_{searchterm}.json", "w") as jsonFile:
            jsonString = json.dumps(all_compaines)
            jsonFile.write(jsonString)

        extracted = extraction(searchterm)

        print(extracted)
