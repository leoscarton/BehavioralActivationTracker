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
    energy_level_before: float
    energy_level_after: float
    mood_delta: float
    energy_delta: float

    def check_mood_values(mood_value):
        if not (0.0 <= mood_value <= 10.0):
            raise ValueError("Mood values must range from 0.0 to 10.0")
        
        if (Decimal(str(mood_value)).as_tuple().exponent < -1):
            raise ValueError("Mood values must have only 1 decimal digit")

        return True

    def check_energy_values(energy_value):
        if not (0.0 <= energy_value <= 100.0):
            raise ValueError("Energy values must range from 0.0 to 100.0")
                
        if (Decimal(str(energy_value)).as_tuple().exponent < -1):
            raise ValueError("Energy values must have only 1 decimal digit")
        
        return True

    def update_mood_delta(self):
        self.mood_delta = self.mood_after - self.mood_before

    def update_energy_delta(self):
        self.energy_delta = self.energy_level_after - self.energy_level_before


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

        #if not self.check_mood_values(self.mood_before):
        #    raise ValueError("Invalid mood values")

        #if not self.check_mood_values(self.mood_after):
        #    raise ValueError("Invalid mood values")

        try:
            self.check_mood_values(self.mood_before)
            self.check_mood_values(self.mood_after)
            self.check_energy_values(self.energy_level_before)
            self.check_energy_values(self.energy_level_after)
        except ValueError as e:
            print(e) #Placeholder, probably will change in the future


#########################################################################################
#  Functions to change values of activities variables
#########################################################################################

    def change_title(self, new_title: str):
        if not new_title or len(new_title) <= 0:
            raise ValueError("New title cannot be empty")
        self.title = new_title
    
    def change_category(self, new_category: str):
        if not new_category or len(new_category) <= 0:
            raise ValueError("New category cannot be empty")
        self.category = new_category

    def change_description(self, new_description: str):
        if not new_description or len(new_description) <= 0:
            raise ValueError("New description cannot be empty")
        self.description = new_description

    def change_planned_date_of_completion(self, new_planned_date_of_completion: pd.DatetimeIndex):
        if not new_planned_date_of_completion:
            raise ValueError("New planned date of completion cannot be empty")
        self.planned_date_of_completion = new_planned_date_of_completion

    def change_actual_date_of_completion(self, new_actual_date_of_completion: pd.DatetimeIndex):
        if new_actual_date_of_completion < self.planned_date_of_completion:
            raise ValueError("Actual date of completion cannot be before planned date of completion")
        self.actual_date_of_completion = new_actual_date_of_completion

    def change_status(self, new_status: bool):
        self.status = new_status

    def change_mood_before(self, new_mood_before: float):
        try:
            self.check_mood_values(new_mood_before)
            self.mood_before = new_mood_before
            self.update_mood_delta()
        except ValueError as e:
            print(f"Invalid mood error: {e}") #Placeholder, probably will change in the future

    def change_mood_after(self, new_mood_after: float):
        try:
            self.check_mood_values(new_mood_after)
            self.mood_after = new_mood_after
            self.update_mood_delta()
        except ValueError as e:
            print(f"Invalid mood error: {e}") #Placeholder, probably will change in the future

    def change_energy_level_before(self, new_energy_before: float):
        try:
            self.check_energy_values(new_energy_before)
            self.energy_level_before = new_energy_before
            self.update_energy_delta()
        except ValueError as e:
            print(f"Invalid energy level error: {e}") #Placeholder, probably will change in the future

    def change_energy_level_after(self, new_energy_after: float):
        try:
            self.check_energy_values(new_energy_after)
            self.energy_level_after = new_energy_after
            self.update_energy_delta()
        except ValueError as e:
            print(f"Invalid energy level error: {e}") #Placeholder, probably will change in the future