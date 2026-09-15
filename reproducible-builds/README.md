# Reproducible Builds

[![Reproducible build](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/reprocheck.yml/badge.svg)](https://github.com/GhostWebEnterprise/ghostweb.signal/actions/workflows/reprocheck.yml)

Follow these instructions to verify that this source code is exactly the same code that was used to compile the APK distributed on the website.

The [reproducible-builds.org](https://reproducible-builds.org/) project has more information about this general topic.

## Prerequisites

- Docker
- Docker Compose
- Python 3

## Build and Verify

You can compile your own release of GhostWeb inside a Docker container and compare the resulted APK to the APK that is officially distributed. To do so, execute the following:

```shell
# Set the release version you want to check
export VERSION=v1.0.0

# Clone the source code repository
git clone https://github.com/GhostWebEnterprise/ghostweb.signal.git

# Go to this directory
cd ghostweb.signal/reproducible-builds

# Check out the release tag
git checkout $VERSION

# The following steps might be different for the chosen version.
# Before proceeding, you should open this tutorial (README.md file) and review the instructions.

# Build the APK using the Docker environment
docker compose up --build

# Download the official APK
wget https://github.com/GhostWebEnterprise/ghostweb.signal/releases/download/$VERSION/app-prod-website-release.apk

# Run the diff script to compare the APKs
python apkdiff/apkdiff.py app-prod-website-release.apk outputs/apk/prodWebsite/release/app-prod-website-release.apk

# Clean up the Docker environment
docker compose down
```

If you get `APKs match`, you have **successfully verified** that the official release matches with your own self-built version of GhostWeb. Congratulations!

If you get `APKs don't match`, please [report the issue](https://github.com/GhostWebEnterprise/ghostweb.signal/issues).
