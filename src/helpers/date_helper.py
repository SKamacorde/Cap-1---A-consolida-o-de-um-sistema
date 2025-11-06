from datetime import datetime
import pandas as pd

class DateHelper:
    @staticmethod
    def now():
        """Retorna data e hora atual."""
        return datetime.now()
    
    def parse_date(date_str):
            try:
               return datetime.strptime(date_str, "%d/%m/%y %H:%M:%S")
            except Exception:
                return pd.NaT