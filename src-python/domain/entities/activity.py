from dataclasses import dataclass
import pandas as pd
from decimal import Decimal

@dataclass
class Activity:
    title: str
    category: str # May change later
    description: str = ''
    planned_date_of_completion: pd.DatetimeIndex # May change later
    actual_date_of_completion: pd.DatetimeIndex # May change later
    status: bool = False
    mood_before: float
    mood_after: float

    def __post_init__(self):
        # Subject to change later in the project
        if not ((0.0 <= self.mood_before <= 10.0) and (0.0 <= self.mood_after <= 10.0)):
            raise ValueError("Mood values must range from 0.0 to 10.0")
        
        if ((Decimal(str(self.mood_before)).as_tuple().exponent < -1) or (Decimal(str(self.mood_after)).as_tuple().exponent < -1)):
            raise ValueError("Mood values must have only 1 decimal digit")
    
