set -ex

ruff format *.py
ruff check *.py

python Generate.py