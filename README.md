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
  - Will you create the next generation of Risk, Prepayment and Defualt models?

## Installation

Get started with FinX-Plugin in 5 minutes.

**1. Clone the Auto-GPT-FinX-Plugin repository**

   Clone this repository and navigate to the `Auto-GPT-FinX-Plugin` folder in your terminal:
   ```
   git clone https://github.com/FinX-IO/Auto-GPT-FinX-Plugin.git
   ```
   
**2. Install required dependencies**
   
   Execute the following command to install FinX-IO Python SDK and dependencies:
   ```
   pip install -r requirements.txt
   ```
   
**3. Package the plugin as a zip file**
   
   If you cloned the repository, compress the plugin into a zip file or download the repository as a zip file.
   
**4. Install Auto-GPT**

   If not already installed, clone the [Auto-GPT repository](https://github.com/Significant-Gravitas/Auto-GPT), follow the installation instructions and navigate to the `Auot-GPT` folder.

**5. Copy the zip file into the `Auto-GPT Plugin` folder**

   Transfer the `FinX-GPT-Plugin` zip file into the plugins subfolder in the `Auto-GPT` repository.

**6. Locate the `.env.template` file**

   Find the `.env.template` file in the `/Auto-GPT` folder.

**7. Duplicate and rename the file**
   
   Duplicate the `.env.template` file and rename to `.env` in the `/Auto-GPT` folder.

**8. Open the `.env` file**
   
   Open the `.env.template` file in a text editor. Note: Your operating system may hide files starting with a dot.

**9. Add FinX Plugin configuration settings**
   
   Append the following configuration setting to the end of the file:
   ```
   ###################################################################################
   FinX-Plugin
   ################################################################################
   FINX_API_KEY=my_finx_api_key
   FINX_REGISTERED_EMAIL=my_finx_registered_email
   FINX_WORKSPACE=my_finx_workspace_path_relative_to_default_workspace
   ```
   
- Get a FinX API Key at [here](https://app.finx.io)

**10. Allowlist Plugin**
    
    In the `.env` file search for `ALLOWEDLISTED_PLUGINS` and add the FinX-Plugin. Note: Sets of listed plugins that are allowed (Example: Plugin1,Plugin2)
    ```
    ###################################################################################
    FinX-Plugin
    ################################################################################
    ALLOWEDLISTED_PLUGINS=FinX
    ```
    
## Some Available Commands

More exhaustive documentation of commands is available <a href="https://app.finx.io/docs" target="_blank">here</a>

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

