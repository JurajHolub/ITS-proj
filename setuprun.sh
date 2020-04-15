#!/bin/sh

set -e
cd $(dirname $0)
pip3 install behave
/usr/bin/env behave
