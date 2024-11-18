# FastAPI Authentication Endpoints Documentation

## Endpoints

### 1. **POST /register-user (User Registration)**
- **Input**: `UserCreateSchema`
- **Output**: `UserResponseSchema`
- **Flow**:
  1. Hashes the user's password using `bcrypt` and stores it securely in the database.
  2. Creates a new user in the database.
  3. Handles `IntegrityError` to raise `USER_ALREADY_EXISTS` if the user already exists.
  4. Returns the user data on successful registration.

---

### 2. **POST /auth/login (User Login)**
- **Input**: `UserLoginSchema`
- **Output**: `LoginResponseSchema`
- **Flow**:
  1. Fetches the user by email from the database.
  2. If the user is not found, raises `USER_NOT_FOUND`.
  3. Verifies the provided password using `passlib.context`.
  4. If the password is invalid, raises `INVALID_PASSWORD`.
  5. Generates an access token for the user and returns it in the response.

---

### 3. **POST /auth/refresh-token (Token Refresh)**
- **Input**: Refresh token from the `Refresh-Token` header.
- **Output**: `RefreshTokenResponseSchema`
- **Flow**:
  1. Validates the refresh token using `validate_refresh_token`.
  2. Generates a new access token for the user and returns it.

---

### 4. **GET /me (Get User Details)**
- **Input**: Authorization header with an access token.
- **Output**: `UserResponseSchema`
- **Flow**:
  1. Validates the access token using `valid_user`.
  2. Fetches the user's details from the database.
  3. If the user is not found, raises `USER_NOT_FOUND`.
  4. Returns the user details.

---

## Code Highlights

### **Password Handling**
- Uses `bcrypt.hashpw` to securely hash passwords.
- Passwords are stored as hashed values in the database, ensuring they are not stored in plaintext.

### **Token Management**
- `generate_user_token`: Generates access tokens for authentication.
- `validate_refresh_token`: Ensures refresh tokens are valid and returns the associated user's email.

### **Error Handling**
Custom exceptions provide standardized error responses:
- `USER_NOT_FOUND` (404): User does not exist.
- `INVALID_PASSWORD` (400): Password does not match.
- `USER_ALREADY_EXISTS` (400): Attempt to register an already existing user.

### **Database Interaction**
- Uses SQLAlchemy's session management (`get_session`) for database operations.
- Commits and rolls back transactions to ensure database consistency.

---
