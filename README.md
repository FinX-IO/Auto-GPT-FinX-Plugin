# Auto-GPT-FinX-Plugin
The FinX Plugin for Auto-GPT streamlines the capital markets research process by leveraging the prompt flexibility of Auto-GPT with FinX.io's institutional-grade cross-asset risk platform.

## Key Features

- Open source python SDK connected to FinX.io data and analytics engines.
  - Auto-GPT will automate your access to capital markets research by calling FinX.io python methods and integrating FinX capabilities into your own python code.
- Reference data covering the entire global capital markets.
  - Bonds, Equities, Derivatives, Currencies, Commodities, and more.
- Best-in-class quantitative risk analytics for institutional and professional use.
  - Yield, Spread, Duration, Convexity, Sensitivity, Greeks, Payment Speeds, and more.
- Accurate asset projections and simulations.
  - Perform stress-testing, cash flow projections, and scenario analysis.
- The industry's most advanced Cash Flow Testing engine, now Autonomously AI-Enabled.
  - Perform cash flow testing on individual securities or entire portfolios.
- Trinomial Trees for Bonds, Derivatives, and tough-to-value securities with optionality.
  - Will you create the next generation of Risk, Prepayment and Defualt models?"

## Installation

1. Clone this repository:

```
git clone https://github.com/FinX-IO/Auto-GPT-FinX-Plugin.git
```

2. Navigate to the Auto-GPT-FinX-Plugin folder in a terminal and run the install.sh script:

```
cd ~/Auto-GPT-FinX-Plugin
bash install.sh
```

3. Make sure that your Auto-GPT environment configuration is correct and has values populated for:

```
FINX_API_KEY=my_finx_api_key
FINX_REGISTERED_EMAIL=my_finx_registered_email
FINX_WORKSPACE=my_finx_workspace_path_relative_to_default_workspace

ALLOWLISTEDPLUGINS=[AutoGPTFinXPlugin]

## Some Available Commands

More exhaustive documentation of commands is available [here](https://app.finx.io/docs)

1. Run Auto-GPT with the following inputs in manual mode (--manual):

- AI Name: FinXGPT
- Role: analyze a treasury bond
- Goals:
  - Goal 1: find a treasury bond
  - Goal 2: find current market price for the found bond
  - Goal 3: run analytics for the found bond as of today
  - Goal 4: write the output as a report to a file 'treasury_bond.txt'
  
If you are configured correctly, you should get a response like this:

```
response
```

