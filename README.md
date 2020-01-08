
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

`POST /register`

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

`POST /login`

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
