#!/bin/sh -e
set -x

ruff check --fix src
black src --line-length=120
