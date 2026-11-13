#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp="$(mktemp)"
error_output="$(mktemp)"
trap 'rm -f "$tmp" "$error_output"' EXIT

fingerprint="64bb12f28a7d39d2cf921024c6d36019ea3808481bd4471511bd83ca64f20435"

cat > "$tmp" <<EOF_SIGNER
Verifies
Verified using v2 scheme (APK Signature Scheme v2): true
Number of signers: 1
Signer #1 certificate SHA-256 digest: $fingerprint
EOF_SIGNER
bash "$root/scripts/verify-apksigner-fingerprint.sh" "$tmp" "$fingerprint"

cat > "$tmp" <<EOF_V2_SIGNER
Verifies
Verified using v2 scheme (APK Signature Scheme v2): true
Number of signers: 1
V2 Signer: certificate SHA-256 digest: $fingerprint
EOF_V2_SIGNER
bash "$root/scripts/verify-apksigner-fingerprint.sh" "$tmp" "$fingerprint"

(
  cd "$root/reproducible-builds"
  bash ../scripts/verify-apksigner-fingerprint.sh "$tmp" "$fingerprint"
)

# This is an intentional negative test. Capture the verifier's expected
# ::error:: output so GitHub Actions does not annotate a passing job as failed.
if bash "$root/scripts/verify-apksigner-fingerprint.sh" "$tmp" "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" 2>"$error_output"; then
  echo "Expected a mismatched signer fingerprint to be rejected" >&2
  exit 1
fi
grep -Fq "APK signer differs from the published GhostWeb Signal identity" "$error_output"

echo "Both supported apksigner formats accepted; mismatched fingerprint rejected."
