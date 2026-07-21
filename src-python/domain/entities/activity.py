from dataclasses import dataclass
import pandas as pd
from decimal import Decimal

@dataclass
class Activity:
    title: str
    category: str # May change later
    description: str
    planned_date_of_completion: pd.DatetimeIndex # May change later
    actual_date_of_completion: pd.DatetimeIndex # May change later
    status: bool
    mood_before: float
    mood_after: float

    def __post_init__(self):
        # All verifications are subject to change later in the project
        if not self.title or len(self.title) <= 0:
            raise ValueError("Title cannot be empty")

        # There will be eventually a check to see if the category exists in the database
        if not self.category or len(self.category) <= 0:
            raise ValueError("Category cannot be empty")

        if not self.description or len(self.description) <= 0:
            self.description = ""

        if not self.planned_date_of_completion:
            raise ValueError("Planned date of completion cannot be empty")

        if (self.actual_date_of_completion is not None) and (self.actual_date_of_completion < self.planned_date_of_completion):
            raise ValueError("Actual date of completion cannot be before planned date of completion")

        if self.status is None:
            self.status = False

        if not ((0.0 <= self.mood_before <= 10.0) and (0.0 <= self.mood_after <= 10.0)):
            raise ValueError("Mood values must range from 0.0 to 10.0")
        
        if ((Decimal(str(self.mood_before)).as_tuple().exponent < -1) or (Decimal(str(self.mood_after)).as_tuple().exponent < -1)):
            raise ValueError("Mood values must have only 1 decimal digit")
    
