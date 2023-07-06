# Changelog

## [0.9.0](https://github.com/googleapis/python-run/compare/v0.8.1...v0.9.0) (2023-07-06)


### Features

* Adds support for custom audiences ([#107](https://github.com/googleapis/python-run/issues/107)) ([bfd0829](https://github.com/googleapis/python-run/commit/bfd08297d6301c57e242819dba35006218d217e5))

## [0.8.1](https://github.com/googleapis/python-run/compare/v0.8.0...v0.8.1) (2023-07-04)


### Bug Fixes

* Add async context manager return types ([#105](https://github.com/googleapis/python-run/issues/105)) ([592b761](https://github.com/googleapis/python-run/commit/592b761bd1f04c7a6d0fb7d8e3b70ba54db01779))

## [0.8.0](https://github.com/googleapis/python-run/compare/v0.7.1...v0.8.0) (2023-05-25)


### Features

* Adds support for Session affinity in Service (GA) ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))
* Adds support for Startup CPU Boost (GA) ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))
* New 'port' field for HttpGetAction probe type ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))
* New fields/enum values ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))


### Documentation

* General documentation fixes. ([c907927](https://github.com/googleapis/python-run/commit/c907927b59079867825954786192954293aa6184))

## [0.7.1](https://github.com/googleapis/python-run/compare/v0.7.0...v0.7.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#93](https://github.com/googleapis/python-run/issues/93)) ([4db3679](https://github.com/googleapis/python-run/commit/4db3679a05db11882644fb1b6d5f8a0461758351))

## [0.7.0](https://github.com/googleapis/python-run/compare/v0.6.0...v0.7.0) (2023-01-20)


### Features

* Adding support for encryption_key_revocation_action and encryption_key_shutdown_duration for RevisionTemplate and ExecutionTemplate  ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))


### Bug Fixes

* Add context manager return types ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))


### Documentation

* Add documentation for enums ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))
* Documentation improvements, including clarification that v1 labels/annotations are rejected in v2 API ([bdb8baf](https://github.com/googleapis/python-run/commit/bdb8bafc7884624dea93082f1ef764768c9c13b6))

## [0.6.0](https://github.com/googleapis/python-run/compare/v0.5.0...v0.6.0) (2023-01-10)


### Features

* Add support for python 3.11 ([#78](https://github.com/googleapis/python-run/issues/78)) ([951b679](https://github.com/googleapis/python-run/commit/951b6794b0357b788097b53fdb2e2e2264536cff))

## [0.5.0](https://github.com/googleapis/python-run/compare/v0.4.2...v0.5.0) (2022-12-14)


### Features

* Add support for `google.cloud.run.__version__` ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* Add typing to proto.Message based class attributes ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* Adds Cloud Run Jobs v2 API client libraries ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* Adds Startup and Liveness probes to Cloud Run v2 API client libraries ([#60](https://github.com/googleapis/python-run/issues/60)) ([d4d22ec](https://github.com/googleapis/python-run/commit/d4d22ecf187d7b370f10d627ece28255cbe9c804))


### Bug Fixes

* Add dict typing for client_options ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))
* Drop usage of pkg_resources ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))
* Fix timeout default values ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([a19c445](https://github.com/googleapis/python-run/commit/a19c445b86b4b5897bbf171369a9b674f90cf803))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([cfedfb2](https://github.com/googleapis/python-run/commit/cfedfb23c599bc010efdfd4d2f435f5d4861020a))

## [0.4.2](https://github.com/googleapis/python-run/compare/v0.4.1...v0.4.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#58](https://github.com/googleapis/python-run/issues/58)) ([87dcb78](https://github.com/googleapis/python-run/commit/87dcb781affd73e25e3850e01a240e0e985f0570))
* **deps:** require google-api-core&gt;=1.33.2 ([87dcb78](https://github.com/googleapis/python-run/commit/87dcb781affd73e25e3850e01a240e0e985f0570))

## [0.4.1](https://github.com/googleapis/python-run/compare/v0.4.0...v0.4.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#55](https://github.com/googleapis/python-run/issues/55)) ([7a85bac](https://github.com/googleapis/python-run/commit/7a85bac07e66efd965453fd0ecb093976edca2f2))

## [0.4.0](https://github.com/googleapis/python-run/compare/v0.3.0...v0.4.0) (2022-09-13)


### Features

* Enable REST transport support ([#45](https://github.com/googleapis/python-run/issues/45)) ([0ccecb0](https://github.com/googleapis/python-run/commit/0ccecb079d3702026d14ef577fda27030f19f3aa))

## [0.3.0](https://github.com/googleapis/python-run/compare/v0.2.1...v0.3.0) (2022-08-15)


### Features

* add audience parameter ([0d02163](https://github.com/googleapis/python-run/commit/0d02163a93eade5b9218d5330ece1723e375a3ff))


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#33](https://github.com/googleapis/python-run/issues/33)) ([55bf980](https://github.com/googleapis/python-run/commit/55bf98023e2a6855a394e487db11b6aa7dc57c17))
* **deps:** require google-api-core>=1.32.0,>=2.8.0 ([0d02163](https://github.com/googleapis/python-run/commit/0d02163a93eade5b9218d5330ece1723e375a3ff))
* **deps:** require proto-plus >= 1.22.0 ([55bf980](https://github.com/googleapis/python-run/commit/55bf98023e2a6855a394e487db11b6aa7dc57c17))
* Updates pre-release Cloud Run v2 Preview client libraries to work with the latest API revision ([0d02163](https://github.com/googleapis/python-run/commit/0d02163a93eade5b9218d5330ece1723e375a3ff))

## [0.2.1](https://github.com/googleapis/python-run/compare/v0.2.0...v0.2.1) (2022-07-26)


### Bug Fixes

* require python 3.7+ ([#26](https://github.com/googleapis/python-run/issues/26)) ([854f73d](https://github.com/googleapis/python-run/commit/854f73db0893e080dc6098d134809692e8685f39))

## [0.2.0](https://github.com/googleapis/python-run/compare/v0.1.0...v0.2.0) (2022-04-14)


### Features

* AuditConfig for IAM v1 ([43244bc](https://github.com/googleapis/python-run/commit/43244bc4aba7e70e21348dc3c3b78c430b2bedb9))


### Bug Fixes

* **deps:** require grpc-google-iam-v1 >=0.12.4 ([43244bc](https://github.com/googleapis/python-run/commit/43244bc4aba7e70e21348dc3c3b78c430b2bedb9))


### Documentation

* fix type in docstring for map fields ([43244bc](https://github.com/googleapis/python-run/commit/43244bc4aba7e70e21348dc3c3b78c430b2bedb9))

## 0.1.0 (2022-04-03)


### Features

* generate v2 ([6fd2a11](https://github.com/googleapis/python-run/commit/6fd2a11558d444d454184ab5fe594618b441c2db))
