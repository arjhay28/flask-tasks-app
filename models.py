
from sqlalchemy import Column, Integer, String, func, Text, DateTime, Enum
from sqlalchemy.orm import DeclarativeBase
from enums import TaskPriority, TaskStatus

class Base(DeclarativeBase):
    pass




class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(
        Enum(TaskStatus, name="task_status"), 
        default=TaskStatus.pending,
        nullable=False
    )
    priority = Column(
        Enum(TaskPriority,name="task_priority"),
        default=TaskPriority.moderate,
        nullable=False
    )
    due_date = Column(DateTime)
    
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
