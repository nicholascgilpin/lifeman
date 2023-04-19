#!/bin/bash
set -euo pipefail

source myproject/bin/activate
python -m unittest discover -v