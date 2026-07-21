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

    def check_mood_values(mood_value):
        if not (0.0 <= mood_value <= 10.0):
            raise ValueError("Mood values must range from 0.0 to 10.0")
            return False
        
        if (Decimal(str(mood_value)).as_tuple().exponent < -1):
            raise ValueError("Mood values must have only 1 decimal digit")
            return False

        return True

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

        if not self.check_mood_values(self.mood_before):
            raise ValueError("Invalid mood values")

        if not self.check_mood_values(self.mood_after):
            raise ValueError("Invalid mood values")