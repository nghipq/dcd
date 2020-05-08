from server.models import User, Post, Sickness, Store, Product, Bill, postsSchema, productsSchema, billsSchema,Department
from urllib import parse

def get_queries(request):
    return dict(parse.parse_qsl(parse.urlsplit(request.url).query))

def filter_arr_by_queries(arr, queries):
    
    def filter_by_query(item):
        rs = True
        for key, value in queries.items():
            rs = rs and (str(item[key]) == value)
        return rs
    
    listFilter = list(filter(filter_by_query, arr))
    return listFilter

def format_products_list(arr):
    res = []
    for product in arr:
        feature = {
            "id": str(product["id"]),
            "storeId": str(product["store"]),
            "storeName": Store.query.filter_by(id = product["store"]).first().name,
            "name": product["name"],
            "description": product["description"],
            "price": product["price"],
            "quantity": product["quantity"],
            "images": product["images"],
            "types": product["types"],
            "brand": product["brand"]
        }

        res.append(feature)
    
    return res

def format_bills_list(arr):
    res = []
    for bill in arr:
        username = User.query.filter_by(id = int(bill["userId"])).first().username
        billProducts = bill["products"]
        billProducts = billProducts.split(",")

        products = dict()
        for product in billProducts:
            pName = product[0]
            products[pName] = product[2:]

        feature = {
            "id": str(bill["id"]),
            "username": username,
            "products": products,
            "total_price": bill["totalPrice"],
            "address": bill["address"],
            "phonenumber": bill["phone"],
            "check": str(bill["isCheck"]),
            "date": str(bill["date_register"])
        }

        res.append(feature)
    return res