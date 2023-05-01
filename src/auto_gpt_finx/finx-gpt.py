#! python
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
import requests
from . import AutoGPTFinX

plugin = AutoGPTFinX()

def analyze_investment_security(self, security_id: str, as_of_date: str) -> Optional[Dict[str, Any]]:
    """Analyze security using FinX API"""
    url = f"https://hedgefunds.finx.io/cms2/calculate_security_analytics"
    params = {
        "security_id": security_id, # "SPY
        "finx_api_key": self.finx_api_key,
        "as_of_date": as_of_date
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
