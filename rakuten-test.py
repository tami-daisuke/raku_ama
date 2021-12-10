import requests




def set_api_parameter():
    keyword = input("何を検索しますか？：")
    shopCode = input("ショップコードは？：")
    genreId = input("ジャンルIDは？：")

    parameter = {
        "format"        : "json",
        "keyword"       : keyword,
        "shopCode"      : shopCode,
        "genreId"       : genreId,
        "applicationId" : "1022438453734169183",
        "formatVersion" : 2,
        "page"          : 1,
        "hits"          : 30
    }
    return parameter


url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"




search_param = set_api_parameter()



response = requests.get(url, params = search_param)
result = response.json()

print (result)

item = result ["Items"][0]

print (item["itemName"])
print (item["itemPrice"])
