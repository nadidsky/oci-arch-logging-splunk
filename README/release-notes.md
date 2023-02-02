# OCI Logging Add-On v2

## Release 2.2.2
- Fix related to multi-threading support
- Updated OCI Python SDK to 2.64.0

## Release 2.2.1
- Local File System Key is the default
- Support for upload of OCI API Key file is moved to `More settings`
- Updated OCI Python SDK to 2.54.0
- Updated [README.md](README.md) with prerequisites and troubleshooting

## Release 2.2.0
- Added help text to inputs screen
- Restored Support for uploading an RSA OCI API Key 
- Support for local file system key file is moved to `More settings`
    - Local File System Key is required for Splunk Version 8.0
- Added logger.info message for unsupported data in the stream
- Added logger.info for when data is not returned.  This is track the plugin is running without using DEBUG
- PEP8 clean up

## Release 2.1.1
- Added release notes
- Converted to an OCI API key stored on the Heavy Forwarder instead of uploaded via the Web UI
- Support for OCI API Keys generated from the console
- Updated OCI Python SDK to 2.45.1
- Removed __pycache__ and other clean up
- Renamed input variable *Worker Processes* to *Number of partitions*