#! python
from typing import Any, Dict, Optional
import os
from finx.client import FinXClient

def analyze_investment_security(self, security_id: str, as_of_date: str) -> Optional[Dict[str, Any]]:
    """Analyze security using FinX API"""
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.calculate_security_analytics(security_id, as_of_date)
    return results
