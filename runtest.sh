#!/bin/bash

activate () {
  . ../projectenv/bin/activate
  python -m unittest tests/all_tests.py -v
  deactivate
}

activate
echo "Done"
