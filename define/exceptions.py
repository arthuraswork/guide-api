from enum import Enum
from fastapi import  HTTPException, status
class Exceptions(Enum):
    BASE_EXCEPTION = HTTPException(status.HTTP_400_BAD_REQUEST, "Your request contains undefined error")
    LOGIC_EXCEPTION = HTTPException(status.HTTP_400_BAD_REQUEST, "Your request contains has no sens")