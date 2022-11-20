from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(frozen=True, kw_only=True)
class Message(ABC):
    msg_id: UUID = field(default_factory=uuid4)
    msg_creation_time: datetime = field(default_factory=datetime.utcnow)
