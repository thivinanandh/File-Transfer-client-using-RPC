#!/bin/bash

fuser -k 8000/tcp
python3 server3.py
