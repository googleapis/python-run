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

from google.cloud.run_v2.services.revisions.client import RevisionsClient
from google.cloud.run_v2.services.revisions.async_client import RevisionsAsyncClient
from google.cloud.run_v2.services.services.client import ServicesClient
from google.cloud.run_v2.services.services.async_client import ServicesAsyncClient

from google.cloud.run_v2.types.condition import Condition
from google.cloud.run_v2.types.k8s_min import CloudSqlInstance
from google.cloud.run_v2.types.k8s_min import Container
from google.cloud.run_v2.types.k8s_min import ContainerPort
from google.cloud.run_v2.types.k8s_min import EnvVar
from google.cloud.run_v2.types.k8s_min import EnvVarSource
from google.cloud.run_v2.types.k8s_min import HTTPGetAction
from google.cloud.run_v2.types.k8s_min import HTTPHeader
from google.cloud.run_v2.types.k8s_min import Probe
from google.cloud.run_v2.types.k8s_min import ResourceRequirements
from google.cloud.run_v2.types.k8s_min import SecretKeySelector
from google.cloud.run_v2.types.k8s_min import SecretVolumeSource
from google.cloud.run_v2.types.k8s_min import TCPSocketAction
from google.cloud.run_v2.types.k8s_min import VersionToPath
from google.cloud.run_v2.types.k8s_min import Volume
from google.cloud.run_v2.types.k8s_min import VolumeMount
from google.cloud.run_v2.types.revision import DeleteRevisionRequest
from google.cloud.run_v2.types.revision import GetRevisionRequest
from google.cloud.run_v2.types.revision import ListRevisionsRequest
from google.cloud.run_v2.types.revision import ListRevisionsResponse
from google.cloud.run_v2.types.revision import Revision
from google.cloud.run_v2.types.revision_template import RevisionTemplate
from google.cloud.run_v2.types.service import CreateServiceRequest
from google.cloud.run_v2.types.service import DeleteServiceRequest
from google.cloud.run_v2.types.service import GetServiceRequest
from google.cloud.run_v2.types.service import ListServicesRequest
from google.cloud.run_v2.types.service import ListServicesResponse
from google.cloud.run_v2.types.service import Service
from google.cloud.run_v2.types.service import UpdateServiceRequest
from google.cloud.run_v2.types.traffic_target import TrafficTarget
from google.cloud.run_v2.types.traffic_target import TrafficTargetStatus
from google.cloud.run_v2.types.traffic_target import TrafficTargetAllocationType
from google.cloud.run_v2.types.vendor_settings import BinaryAuthorization
from google.cloud.run_v2.types.vendor_settings import RevisionScaling
from google.cloud.run_v2.types.vendor_settings import VpcAccess
from google.cloud.run_v2.types.vendor_settings import ExecutionEnvironment
from google.cloud.run_v2.types.vendor_settings import IngressTraffic

__all__ = ('RevisionsClient',
    'RevisionsAsyncClient',
    'ServicesClient',
    'ServicesAsyncClient',
    'Condition',
    'CloudSqlInstance',
    'Container',
    'ContainerPort',
    'EnvVar',
    'EnvVarSource',
    'HTTPGetAction',
    'HTTPHeader',
    'Probe',
    'ResourceRequirements',
    'SecretKeySelector',
    'SecretVolumeSource',
    'TCPSocketAction',
    'VersionToPath',
    'Volume',
    'VolumeMount',
    'DeleteRevisionRequest',
    'GetRevisionRequest',
    'ListRevisionsRequest',
    'ListRevisionsResponse',
    'Revision',
    'RevisionTemplate',
    'CreateServiceRequest',
    'DeleteServiceRequest',
    'GetServiceRequest',
    'ListServicesRequest',
    'ListServicesResponse',
    'Service',
    'UpdateServiceRequest',
    'TrafficTarget',
    'TrafficTargetStatus',
    'TrafficTargetAllocationType',
    'BinaryAuthorization',
    'RevisionScaling',
    'VpcAccess',
    'ExecutionEnvironment',
    'IngressTraffic',
)
