import enum


class TaskStatus(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    archived = "archived"


class TaskPriority(enum.Enum):
    immediate = "immediate"
    high = "high"
    moderate = "moderate"
    low = "low"