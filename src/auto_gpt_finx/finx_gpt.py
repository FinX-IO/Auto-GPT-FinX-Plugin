#! python
from typing import Any, Dict, Optional
import os
from finx.client import FinXClient

def calculate_security_analytics(security_id: str, as_of_date: str, price: float = 100.00) -> Optional[Dict[str, Any]]:
    """Analyze security using FinX API"""
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.calculate_security_analytics(security_id, as_of_date, price)
    return results

def get_security_reference_data(security_id: str) -> Optional[Dict[str, Any]]:
    """Get security reference data using FinX API"""
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.get_security_reference_data(security_id)
    return results
