#!/usr/bin/env bash

set -o errexit
set -o pipefail
cmd="$@"

function mysql_ready(){
python << END

import sys
import mysqlclient
import environ
}