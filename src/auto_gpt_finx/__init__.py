#! python
"""FinX Plugin for Auto-GPT"""
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict
from auto_gpt_plugin_template import AutoGPTPluginTemplate


# FinX
from dotenv import load_dotenv
import os
from pathlib import Path
from .finx_gpt import *

PromptGenerator = TypeVar("PromptGenerator")

finx_api_key = os.getenv("FINX_API_KEY")
finx_registered_email = os.getenv("FINX_REGISTERED_EMAIL")

with open(str(Path(os.getcwd()) / ".env"), "r") as fp:
    load_dotenv(stream=fp)


class Message(TypedDict):
    """Message type for FinX API"""
    role: str
    content: str

class FinX(AutoGPTPluginTemplate):

    def __init__(self):
        super().__init__()
        self.finx_api_key = finx_api_key
        self.finx_registered_email = finx_registered_email
        self.finx_api_url = "https://api.finx.io"
        self._version = "0.0.1"
        self._name = "AutoGPT FinX Plugin"
        self._description = "FinX Plugin for Auto-GPT"

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        """Post prompt to FinX API"""
        prompt.add_command(
            "Calculate Investment Security Analytics",
            "calculate_security_analytics",
            {
                "security_id": "<security_id>",
                "as_of_date": "<as_of_date>",
                "price": "<price>"
            },
            calculate_security_analytics
        )
        prompt.add_command(
            "Get Investment Security Reference Data",
            "get_security_reference_data",
            {
                "security_id": "<security_id>"
            },
            get_security_reference_data
        )
        prompt.add_command(
            "Get Curve Data",
            "get_curve",
            {
                "curve_name": "<curve_name>",
                "currency": "<currency>",
                "start_date": "<start_date>",
                "end_date": "<end_date>",
                "country_code": "<country_code>",
                "fixing": "<fixing>",
                "tenor": "<tenor>"
            },
            get_curve
        )
        prompt.add_command(
            "Calculate Greeks",
            "calculate_greeks",
            {
                "s0": "<s0>",
                "k": "<k>",
                "r": "<r>",
                "sigma": "<sigma>",
                "q": "<q>",
                "t": "<t>",
                "price": "<price>",
                "option_side": "<option_side>",
                "option_type": "<option_type>"
            },
            calculate_greeks
        )
        prompt.add_command(
            "Calculate Security Key Rates",
            "calculate_security_key_rates",
            {
                "security_id": "<security_id>",
                "as_of_date": "<as_of_date>",
                "price": "<price>",
                "lognormal": "<lognormal>",
                "volatility": "<volatility>",
                "drift_a": "<drift_a>",
                "yield_shift": "<yield_shift>",
                "shock_in_bp": "<shock_in_bp>",
                "price_as_yield": "<price_as_yield>",
                "cpr": "<cpr>",
                "psa": "<psa>"
            },
            calculate_security_key_rates
        )
        prompt.add_command(
            "Generate Trinomial Tree",
            "generate_trinomial_tree",
            {
                "curve_data": "<curve_data>",
                "num_paths": "<num_paths>",
                "volatility": "<volatility>",
                "drift_a": "<drift_a>",
                "lognormal": "<lognormal>"
            },
            generate_trinomial_tree
        )
        prompt.add_command(
            "Generate Investment Security Cash Flows",
            "generate_investment_security_cash_flows",
            {
                "security_id": "<security_id>",
                "as_of_date": "<as_of_date>",
                "price": "<price>",
                "lognormal": "<lognormal>",
                "volatility": "<volatility>",
                "drift_a": "<drift_a>",
                "yield_shift": "<yield_shift>",
                "shock_in_bp": "<shock_in_bp>",
                "price_as_yield": "<price_as_yield>",
                "cpr": "<cpr>",
                "psa": "<psa>"
            },
            generate_investment_security_cash_flows
        )
        return prompt

    def can_handle_post_prompt(self) -> bool:
        return True

    def can_handle_on_response(self) -> bool:
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        pass

    def can_handle_on_planning(self) -> bool:
        return False

    def on_planning(self, prompt: PromptGenerator, messages: List[Message]) -> Optional[str]:
        pass

    def can_handle_post_planning(self) -> bool:
        return False

    def post_planning(self, response: str) -> str:
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
            self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
            self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
            self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        pass
