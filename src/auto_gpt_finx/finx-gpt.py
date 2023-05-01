#! python
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
import requests
from . import AutoGPTFinX
import finx

plugin = AutoGPTFinX()

def analyze_investment_security(self, security_id: str, as_of_date: str) -> Optional[Dict[str, Any]]:
    """Analyze security using FinX API"""
    results = finx.calculate_security_analytics(security_id, as_of_date)
    return results
