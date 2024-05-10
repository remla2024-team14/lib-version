# lib-version
A version-aware library consumed by the URL fishing detection application service

Uses semantic versioning `vMAJOR.MINOR.PATCH`

This library has an endpoint `/lib-version` for GET requests which will return the library's version. 
The version comes from either the latest tag on git or the `version.txt`, depending on which one is available.
The version of latest tag on git (if fetched) will always be written to `version.txt`.

The library also makes use of a workflow which allows for automated tagging on github.
