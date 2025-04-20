from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from src.config import SECRET_KEY
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
from src.config import ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timezone, timedelta







#Initializing context for hashing passwords 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define the OAuth2 scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

#converting passwd to hashed password
def get_password_hash(password):
    return pwd_context.hash(password)

#compare password and hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#Updating datetime 
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None

        return username 
    except jwt.PyJWTError:
        return None
    
    


