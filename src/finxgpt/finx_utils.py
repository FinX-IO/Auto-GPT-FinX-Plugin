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

def get_curve(curve_name: str, currency: str, start_date: str, end_date: str, country_code: str, fixing: str, tenor: str) -> Optional[Dict[str, Any]]:
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.get_curve(curve_name, currency, start_date, end_date, country_code, fixing, tenor)
    return results

def calculate_greeks(s0: float, k: float, r: float, sigma: float, q: float, t: int, price: float, option_side: str, option_type: str) -> Optional[Dict[str, Any]]:
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.calculate_greeks(s0, k, r, sigma, q, t, price, option_side, option_type)
    return results

def calculate_security_key_rates(security_id: str, as_of_date: str, price: float = 100.00,  lognormal = True, volatility = None, drift_a = None, yield_shift = None, shock_in_bp = None, price_as_yield = None, cpr = None, psa = None) -> Optional[Dict[str, Any]]:
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.calculate_security_key_rates(security_id, as_of_date, price, lognormal, volatility, drift_a, yield_shift, shock_in_bp, price_as_yield, cpr, psa),
    return results

def generate_trinomial_tree(curve_data: list, num_paths: int, volatility: float = 0, drift_a: float = 0, lognormal = True):
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.calibrate_tree(curve_data, num_paths, volatility, drift_a, lognormal)
    return results

def generate_investment_security_cash_flows(security_id: str, as_of_date: str, price: float, lognormal: True, volatility: float, drift_a: float, yield_shift: float, shock_in_bp: float, price_as_yield: float, cpr: float, psa: float) -> Optional[Dict[str, Any]]:
    finx_api_key = os.getenv("FINX_API_KEY")
    if not finx_api_key:
        raise Exception("FINX_API_KEY not set")
    finx_client = FinXClient("socket", ssl=True, api_key=finx_api_key)
    results = finx_client.get_security_cash_flows(security_id, as_of_date, price, lognormal, volatility, drift_a, yield_shift, shock_in_bp, price_as_yield, cpr, psa)
    return results
