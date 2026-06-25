from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta
from jose import jwt , JWTError
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# print(secrets.token_hex(32))  # Generate a random secret key and print it
Secret_key = "b0be68708923ad46d9bce1dcb33d4cc1c5504a77d1c2866e8a9caf3d11c84127"  # Replace with your actual secret key
print("Secret Key:", Secret_key)
Algorithm = "HS256"  # Replace with your desired algorithm
Access_token_expire_minutes = 20  # Replace with your desired token expiration time in minutes


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_token(data: dict):
   

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Secret_key, algorithm=Algorithm)
    return encoded_jwt

router = APIRouter(
    prefix="/login",
    tags=["Login"]
    
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.username == request.username).first()
    if not seller or not pwd_context.verify(request.password, seller.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    access_token = generate_token({"sub": seller.username})
    return {"access_token": access_token, "token_type": "bearer"}



def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, Secret_key, algorithms=[Algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = db.query(models.Seller).filter(models.Seller.username == username).first()
    if user is None:
        raise credentials_exception
    return user