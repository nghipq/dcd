
#FARM API
##Usage

All response will have the form
```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### Registering new user

**Definite**

`POST /user/register`

**Arguments**

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

`POST /user/login`

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

`POST /store/register`

**Arguments**

- `"name: String"`
- `"email: String"`
- `"password: String"`
- `"confirm_password: String"`
- `"phonenumber: String"`
- `"address: String"`

**Response**

- `201 Created` on success

```
    json {
        "success": True
    }
```

### Store login

**Definite**

`POST /store/login`

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
`POST /store/createProduct`

**Arguments**

- `"name: String"`
- `"description: String"`
- `"price: String"`
- `"quantity: String"`
- `"store: Integer"`

**Responses**

- `201 Created` on success

```
    json {
        success: true
    }
```

### Delete product by id

***Definites**
`POST /store/deleteProduct`

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
`POST /store/updateProduct`

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
