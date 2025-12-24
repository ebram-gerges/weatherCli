from datetime import datetime

from database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    is_done = Column(Boolean, default=False)
    in_progress = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    end_by = Column(DateTime, nullable=True)

    def __str__(self):
        # Adds a checkmark if done, construction sign if in progress, else a dot
        status = "✅" if self.is_done else "🚧" if self.in_progress else "🔴"
        return f"{status} {self.content}"
