# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.run_v2.types import k8s_min
from google.cloud.run_v2.types import vendor_settings
from google.protobuf import duration_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.run.v2',
    manifest={
        'RevisionTemplate',
    },
)


class RevisionTemplate(proto.Message):
    r"""RevisionTemplate describes the data a revision should have
    when created from a template.

    Attributes:
        revision (str):
            The unique name for the revision. If this
            field is omitted, it will be automatically
            generated based on the Service name.
        labels (MutableMapping[str, str]):
            KRM-style labels for the resource.

            .. raw:: html

                <p>Cloud Run API v2 does not support labels with `run.googleapis.com`,
                `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev`
                namespaces, and they will be rejected. All system labels in v1 now have a
                corresponding field in v2 RevisionTemplate.
        annotations (MutableMapping[str, str]):
            KRM-style annotations for the resource.

            .. raw:: html

                <p>Cloud Run API v2 does not support annotations with `run.googleapis.com`,
                `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev`
                namespaces, and they will be rejected. All system annotations in v1 now
                have a corresponding field in v2 RevisionTemplate.
        scaling (google.cloud.run_v2.types.RevisionScaling):
            Scaling settings for this Revision.
        vpc_access (google.cloud.run_v2.types.VpcAccess):
            VPC Access configuration to use for this
            Revision. For more information, visit
            https://cloud.google.com/run/docs/configuring/connecting-vpc.
        timeout (google.protobuf.duration_pb2.Duration):
            Max allowed time for an instance to respond
            to a request.
        service_account (str):
            Email address of the IAM service account
            associated with the revision of the service. The
            service account represents the identity of the
            running revision, and determines what
            permissions the revision has. If not provided,
            the revision will use the project's default
            service account.
        containers (MutableSequence[google.cloud.run_v2.types.Container]):
            Holds the single container that defines the
            unit of execution for this Revision.
        volumes (MutableSequence[google.cloud.run_v2.types.Volume]):
            A list of Volumes to make available to
            containers.
        execution_environment (google.cloud.run_v2.types.ExecutionEnvironment):
            The sandbox environment to host this
            Revision.
        encryption_key (str):
            A reference to a customer managed encryption
            key (CMEK) to use to encrypt this container
            image. For more information, go to
            https://cloud.google.com/run/docs/securing/using-cmek
        max_instance_request_concurrency (int):
            Sets the maximum number of requests that each
            serving instance can receive.
    """

    revision: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    scaling: vendor_settings.RevisionScaling = proto.Field(
        proto.MESSAGE,
        number=4,
        message=vendor_settings.RevisionScaling,
    )
    vpc_access: vendor_settings.VpcAccess = proto.Field(
        proto.MESSAGE,
        number=6,
        message=vendor_settings.VpcAccess,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=9,
    )
    containers: MutableSequence[k8s_min.Container] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=k8s_min.Container,
    )
    volumes: MutableSequence[k8s_min.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=k8s_min.Volume,
    )
    execution_environment: vendor_settings.ExecutionEnvironment = proto.Field(
        proto.ENUM,
        number=13,
        enum=vendor_settings.ExecutionEnvironment,
    )
    encryption_key: str = proto.Field(
        proto.STRING,
        number=14,
    )
    max_instance_request_concurrency: int = proto.Field(
        proto.INT32,
        number=15,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
