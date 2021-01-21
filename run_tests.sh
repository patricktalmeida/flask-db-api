#!/usr/bin/env bash

set -euo pipefail

pushd src/tests/

listed_tests=$(ls *.py)
for test_case in $listed_tests; do
    python3 $test_case
done

popd