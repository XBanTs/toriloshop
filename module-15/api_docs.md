# ToriloShop API Documentation

## Base URL

```text
http://127.0.0.1:8000/api/
```

---

# Authentication

ToriloShop API supports two authentication methods:

## 1. JWT (JSON Web Token) — Recommended

### Obtain Tokens

```http
POST /api/token/jwt/
Content-Type: application/json
```

### Request Body

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

### Response

```json
{
    "access": "eyJhbGciOiJIUzI1NiIs...",
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

### Use the Access Token in Requests

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### Refresh Expired Access Token

```http
POST /api/token/refresh/
Content-Type: application/json
```

### Request Body

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

## 2. Token Authentication

### Obtain Token

```http
POST /api/token/
Content-Type: application/json
```

### Request Body

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

### Response

```json
{
    "token": "abc123def456..."
}
```

### Use the Token in Requests

```text
Authorization: Token abc123def456...
```

---

# Endpoints

# Products

## List All Products

```http
GET /api/products/
```

**Authentication Required:** No

## Query Parameters

| Parameter      | Type    | Description                                 | Example                              |
|----------------|---------|---------------------------------------------|--------------------------------------|
| page           | integer | Page number                                 | `?page=2`                            |
| category       | integer | Filter by category ID                       | `?category=1`                        |
| is_available   | boolean | Filter by availability                      | `?is_available=true`                 |
| search         | string  | Search by name, description, or category    | `?search=laptop`                     |
| ordering       | string  | Sort by field (`-` for descending order)    | `?ordering=price` or `?ordering=-price` |

## Response (200 OK)

```json
{
    "count": 43,
    "next": "http://127.0.0.1:8000/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "iPhone 15 Pro",
            "description": "Apple iPhone 15 Pro with A17 Pro chip...",
            "price": "1499.99",
            "stock": 15,
            "is_available": true,
            "image": null,
            "category": {
                "id": 1,
                "name": "Electronics",
                "description": "...",
                "product_count": 10,
                "created_at": "2026-05-13T...",
                "updated_at": "2026-05-13T..."
            },
            "created_by": {
                "id": 1,
                "username": "admin",
                "email": "admin@toriloshop.com"
            },
            "created_at": "2026-05-13T...",
            "updated_at": "2026-05-13T..."
        }
    ]
}
```

---

## Create a Product

```http
POST /api/products/
```

**Authentication Required:** Yes (Token or JWT)

### Headers

```text
Content-Type: application/json
```

### Request Body

```json
{
    "name": "Wireless Keyboard",
    "description": "Ergonomic wireless keyboard",
    "price": "89.99",
    "stock": 25,
    "category_id": 1
}
```

### Response

- `201 Created` — Returns the created product object.
- `401 Unauthorized` — Missing or invalid token.

---

## Retrieve a Product

```http
GET /api/products/{id}/
```

**Authentication Required:** No

### Response

- `200 OK` — Returns a single product object.
- `404 Not Found` — Product does not exist.

---

## Update a Product (Full Update)

```http
PUT /api/products/{id}/
```

**Authentication Required:** Yes (Must be the product creator)

### Headers

```text
Content-Type: application/json
```

### Request Body

```json
{
    "name": "Updated Product Name",
    "description": "Updated description",
    "price": "99.99",
    "stock": 50,
    "category_id": 1
}
```

### Response

- `200 OK` — Updated product object.
- `403 Forbidden` — Not the product creator.

---

## Delete a Product

```http
DELETE /api/products/{id}/
```

**Authentication Required:** Yes (Must be the product creator)

### Response

- `204 No Content` — Product deleted successfully.
- `403 Forbidden` — Not the product creator.

---

# Categories

## List All Categories

```http
GET /api/categories/
```

**Authentication Required:** No

## Response (200 OK)

```json
{
    "count": 6,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Electronics",
            "description": "Smartphones, laptops, tablets...",
            "product_count": 10,
            "created_at": "2026-05-13T...",
            "updated_at": "2026-05-13T..."
        }
    ]
}
```

---

# Status Codes

| Code | Meaning |
|------|----------|
| 200 | OK — Request succeeded |
| 201 | Created — Resource created successfully |
| 204 | No Content — Deleted successfully |
| 400 | Bad Request — Invalid input |
| 401 | Unauthorized — Missing or invalid token |
| 403 | Forbidden — Not allowed (not the owner) |
| 404 | Not Found — Resource does not exist |

---

# Pagination

All list endpoints return paginated responses with the following structure:

```json
{
    "count": 43,
    "next": "...",
    "previous": "...",
    "results": [...]
}
```

## Pagination Fields

| Field | Description |
|------|-------------|
| count | Total number of records |
| next | URL of next page (`null` if last page) |
| previous | URL of previous page (`null` if first page) |
| results | Array of items returned per page |
