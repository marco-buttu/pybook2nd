#!/usr/bin/env bash

BASE_PATH="https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin"

if hash wget 2>/dev/null; then
    wget --no-check-certificate -qO- "${BASE_PATH}/pyenv-installer" | bash
else
    if hash curl 2>/dev/null; then
        curl -L "${BASE_PATH}/pyenv-installer" | bash
    else
        echo 'Both curl and wget are not installed, can not continue.'
    fi
fi
