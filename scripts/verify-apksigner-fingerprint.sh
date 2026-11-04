#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <apksigner-output-file> <expected-sha256>" >&2
  exit 2
fi

output_file="$1"
expected="${2,,}"

[[ "$expected" =~ ^[0-9a-f]{64}$ ]] || {
  echo "::error::Expected signer fingerprint must be a 64-character SHA-256 hex digest" >&2
  exit 2
}
test -s "$output_file" || {
  echo "::error::apksigner output is missing or empty: $output_file" >&2
  exit 1
}

if grep -Fxq -- "Signer #1 certificate SHA-256 digest: $expected" "$output_file" \
  || grep -Fxq -- "V2 Signer: certificate SHA-256 digest: $expected" "$output_file"; then
  exit 0
fi

echo "::error::APK signer differs from the published GhostWeb Signal identity: $output_file" >&2
exit 1
