#!/bin/bash
echo "FinX Plugin For Auto-GPT Installation Script"
echo "Please follow the installation prompts:"
echo newline
echo "Enter the full path of your Auto-GPT workspace (ex: /home/ubuntu/Auto-GPT/auto_gpt_workspace)"
read workspace
if [[ "$(workspace: -1)" == "/" ]]; then
  workspace="$(workspace:0:-1)"
fi
cp requirements.txt $workspace/finx-requirements.txt
cd $workspace
echo "FinX Plugin for Auto-GPT will now install dependencies."
pip install -r finx-requirements.txt
echo "FinX Plugin for Auto-GPT dependency installation complete."
echo "Now you will need to configure your Auto-GPT Environment (default is Auto-GPT/.env)"
echo "Please enter the following values into your .env file"
echo "*****************************************************"
echo "FINX_API_KEY=slug_my_finx_api_key"
echo "FINX_REGISTERED_EMAIL=slug_registered_email"
echo "FINX_WORKSPACE=slug_my_workspace_path"
echo "*****************************************************"
echo "One you have entered the values, replace the slug values with you actual FinX API Key, email and data path."
echo "Also add the AutoGPTFinXPlugin to your ALLOWLISTED_PLUGINS list in the .env file:"
echo "ALLOWLISTED_PLUGINS=[AutoGPTFinXPlugin,]"
