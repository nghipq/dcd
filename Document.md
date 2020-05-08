### Registering new user

**Definite**

`POST /user/auth/register`

**Requests**
- `"username": String`
- `"email": String`
- `"phonenumber": String`
- `"address": String`
- `"password": String`
- `"confirm_password": String`

**Response**

- `201 Created` on success


```
    json {
        "success": True
    }
```
### User login

**Definite**

`POST /user/auth/login`

**Arguments**
- `"email": String`
- `"password": String`
**Response**

- `201 Created` on success

```
    json {
        "success": True,
        "username": String,
        "id": Integer 
    }
```
### Store register
**Definite**

`POST /store/auth/register`

**Arguments**

- `"name: String"`
- `"email: String"`
- `"phonenumber: String"`
- `"address: String"`
- `"lx": float`
- `"ly": float`
- `"password: String"`
- `"confirm_password: String"`

**Response**

- `201 Created` on success

```
    json {
        "success": True
    }
```
### Store login

**Definite**

`POST /store/auth/login`

**Arguments**

- `"email": String`
- `"password": String`

**Response**
- `201 Created` on success

```
    json {
        "success": True,
        "name": String,
        "id": Integer 
    }
```

### Insert new product

**Definite**
`POST /store/product/create`

**Arguments**

- `"name: String"`
- `"storeID: Integer"`
- `"description: String"`
- `"price: String"`
- `"quantity: String"`
- `"types: String"`
- `"photo: file"`

**Responses**
- `201 Created` on success

```
    json {
        success: true
    }
```

### Delete product by id

***Definites**
`GET /store/product/delete`

**Arguments**
- `"id: Integer"`

**Response**
- `201 Created` on success

```
    json {
        success: true
    }
```

### Update product by id

**Definite**
`POST /store/product/update`

**Arguments**

- `"id: Integer"`
- `"name: String"`
- `"description: String"`
- `"price: String"`
- `"quantity: String"`

**Response**
- `201 Created` on success
```
    json{
        success: True
    }
```

### get product
**Definite**
`GET /user/product/getProducts`

**Response**
- `201 Created` on success
```
    json{
        allproduct
    }
```

### create bill
**Definite**
`POST /store/bill/create`
**Arguments**
- `"userId": integer`
- `"address": String`
- `"lx": float`
- `"ly" : float`
- `"phone": String`
- `"products": String`
**Response**
- `201 Created` on success
```
    json{
        success: True
    }
```
### get bill
**Definite**
` GET /store/bill/getBills`
**Response**
- `201 Created` on success
```
    json{
        allbill
    }
```
### update bill by id
**Definite**
`POST /store/bill/update`
**Arguments**
- `"id": integer`
- `"check": integer`
**Response**
- `201 Created` on success
```
    json{
         success: True
    }
```

### Get location of all sickness

**Definite**

`Get /location`

**Response**

- `201 Created` on success

```
    json [
        {
            "sicknessId": String,
            "lx": float,
            "ly": float
        }
    ]
```
### Diaglogic sickness
**Definite**

`POST /diaglogic`

**Arguments**

- `"image": String`
- `"user_id": Integer`
- `"lx": float`
- `"ly": float`

**Response**
- `201 Created` on success

```
    json {
        "sickness": String,
        "description": String,
        "solution": String,
        "accurancy": String
    }
```
### sickness
**Definite**
`POST /sickness`
**Arguments**
`"name": String`
`"description": String`
`"solution": String`
**Response**
- `201 Created` on success

```
    json {
        success: true
    }
```

### department
**Definite**
`POST /department`
**Arguments**
`"name": String`
`"address": String`
`"phonenumber": String`
**Response**
- `201 Created` on success`


