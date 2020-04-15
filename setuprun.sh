#!/bin/sh

set -e
cd $(dirname $0)
pip3 install selenium
pip3 install webdriver_manager
pip3 install pytest
pip3 install behave
/usr/bin/env behave
