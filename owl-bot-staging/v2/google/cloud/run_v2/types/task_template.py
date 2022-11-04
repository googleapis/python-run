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
import proto  # type: ignore

from google.cloud.run_v2.types import k8s_min
from google.cloud.run_v2.types import vendor_settings
from google.protobuf import duration_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.run.v2',
    manifest={
        'TaskTemplate',
    },
)


class TaskTemplate(proto.Message):
    r"""TaskTemplate describes the data a task should have when
    created from a template.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        containers (Sequence[google.cloud.run_v2.types.Container]):
            Holds the single container that defines the
            unit of execution for this task.
        volumes (Sequence[google.cloud.run_v2.types.Volume]):
            A list of Volumes to make available to
            containers.
        max_retries (int):
            Number of retries allowed per Task, before
            marking this Task failed.

            This field is a member of `oneof`_ ``retries``.
        timeout (google.protobuf.duration_pb2.Duration):
            Max allowed time duration the Task may be
            active before the system will actively try to
            mark it failed and kill associated containers.
            This applies per attempt of a task, meaning each
            retry can run for the full timeout.
        service_account (str):
            Email address of the IAM service account
            associated with the Task of a Job. The service
            account represents the identity of the running
            task, and determines what permissions the task
            has. If not provided, the task will use the
            project's default service account.
        execution_environment (google.cloud.run_v2.types.ExecutionEnvironment):
            The execution environment being used to host
            this Task.
        encryption_key (str):
            A reference to a customer managed encryption
            key (CMEK) to use to encrypt this container
            image. For more information, go to
            https://cloud.google.com/run/docs/securing/using-cmek
        vpc_access (google.cloud.run_v2.types.VpcAccess):
            VPC Access configuration to use for this
            Task. For more information, visit
            https://cloud.google.com/run/docs/configuring/connecting-vpc.
    """

    containers = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=k8s_min.Container,
    )
    volumes = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=k8s_min.Volume,
    )
    max_retries = proto.Field(
        proto.INT32,
        number=3,
        oneof='retries',
    )
    timeout = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    service_account = proto.Field(
        proto.STRING,
        number=5,
    )
    execution_environment = proto.Field(
        proto.ENUM,
        number=6,
        enum=vendor_settings.ExecutionEnvironment,
    )
    encryption_key = proto.Field(
        proto.STRING,
        number=7,
    )
    vpc_access = proto.Field(
        proto.MESSAGE,
        number=8,
        message=vendor_settings.VpcAccess,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
