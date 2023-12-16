import uuid
from datetime import datetime

from pydantic import BaseModel


class LogRequest(BaseModel):
    log: str


class LogResponse(BaseModel):
    message: str


class LogData(BaseModel):
    id: uuid.UUID
    ip_address: str
    http_method: str
    uri: str
    http_response: str
    timestamp: datetime
