#!/bin/bash

# ensure that the scripts are executable
chmod +x ./graphdoc/graphdoc/run.sh
chmod +x ./graphdoc/mlflow-manager/run.sh
chmod +x ./docserve/docserve.sh
chmod +x ./docserve/intro.sh

# ascii art
intro() {
    bash "$(dirname "$0")/docserve/intro.sh"
}

# setup commands 
install_command() {
    echo "Installing all package dependencies..."
    
    echo "Setting up mlflow-manager..."
    cd graphdoc/mlflow-manager && ./run.sh install
    cd ../..

    echo "Setting up docserve..."
    cd docserve && ./docserve.sh install
    cd ..
}

# env command
env_setup() {
    echo "Setting up environment variables..."

    echo "Setting up mlflow-manager environment variables..."
    cd graphdoc/mlflow-manager/docker/ && cp .env.example .env
    cd ../../..

    echo "Setting up docserve environment variables..."
    cd docserve && cp .env.example .env
    cd ..

    echo "Set the OPENAI_API_KEY in the docserve/.env file"
    echo "You can keep the rest of the variables as is for now"
    
    # update the OPENAI_API_KEY from the cli
    read -p "Enter your OpenAI API key (press Enter to keep existing key): " openai_key
    if [ -n "$openai_key" ]; then
        if [[ "$OSTYPE" == "darwin"* ]]; then
            sed -i '' "s|^OPENAI_API_KEY=.*|OPENAI_API_KEY=$openai_key|" docserve/.env
        else
            sed -i "s|^OPENAI_API_KEY=.*|OPENAI_API_KEY=$openai_key|" docserve/.env
        fi
        echo "OpenAI API key updated successfully."
    else
        echo "Keeping existing OpenAI API key."
    fi
}

# mlflow command
mlflow_setup() {
    echo "Setting up mlflow and it's components..."
    cd graphdoc && ./run.sh mlflow-setup
    cd ..
}

# docserve main 
docserve_main() {
    echo "Running docserve example..."
    cd docserve && ./docserve.sh run
    cd ..
}

# good luck! 
good_luck() {
    echo "Good luck!"
    echo " - denver"

    echo "installing dependencies..."
    install_command
    clear

    echo "setting up environment variables..."
    env_setup
    clear

    echo "setting up mlflow..."
    mlflow_setup
    clear

    echo "running docserve example to ensure everything is working..."
    docserve_main
    clear
    intro
}

# help command
show_help() {
    echo "Usage: ./nli [option]"
    echo "Options:"
    echo "  intro                          Show the intro"
    echo "  install                        Install the required packages"
    echo "  env                            Setup the environment variables"
    echo "  mlflow-setup                   Setup the mlflow components"
    echo "  docserve-main                  Run the docserve example"
    echo "  good-luck                      let's get you started!"
}

# run the script
if [ -z "$1" ]; then
    show_help
else
    case "$1" in
        "intro") intro ;;
        "install") install_command ;;
        "env") env_setup ;;
        "mlflow-setup") mlflow_setup ;;
        "docserve-main") docserve_main ;; 
        "good-luck") good_luck ;;
        *) show_help ;;
    esac
fi