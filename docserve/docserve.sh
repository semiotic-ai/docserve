#!/bin/bash

# development and installation commands
python_command() {
    poetry run python
}

shell_command() {
    poetry shell
}

install_command() {
    poetry install
}

# ascii art
ascii_art() {
    bash "$(dirname "$0")/intro.sh"
}

# main run 
main_run() {
    poetry run python -m docserve.main
}

# help command
show_help() {
    echo "Usage: ./nli [option]"
    echo "Options:"
    echo "  install                         Install all package dependencies"
    echo "  run                             Run the main script"
}

# run the script
if [ -z "$1" ]; then
    show_help
else
    case "$1" in
        "install") install_command ;;
        "run") main_run ;;
        *) show_help ;;
    esac
fi