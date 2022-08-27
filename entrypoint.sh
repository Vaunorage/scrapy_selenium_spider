#!/bin/bash

poetry shell

playwright install
python ./tunisie/main.py