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
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api import launch_stage_pb2  # type: ignore
from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.run_v2.services.revisions import pagers
from google.cloud.run_v2.types import condition
from google.cloud.run_v2.types import k8s_min
from google.cloud.run_v2.types import revision
from google.cloud.run_v2.types import vendor_settings
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import RevisionsTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import RevisionsGrpcAsyncIOTransport
from .client import RevisionsClient


class RevisionsAsyncClient:
    """Cloud Run Revision Control Plane API."""

    _client: RevisionsClient

    DEFAULT_ENDPOINT = RevisionsClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = RevisionsClient.DEFAULT_MTLS_ENDPOINT

    connector_path = staticmethod(RevisionsClient.connector_path)
    parse_connector_path = staticmethod(RevisionsClient.parse_connector_path)
    crypto_key_path = staticmethod(RevisionsClient.crypto_key_path)
    parse_crypto_key_path = staticmethod(RevisionsClient.parse_crypto_key_path)
    revision_path = staticmethod(RevisionsClient.revision_path)
    parse_revision_path = staticmethod(RevisionsClient.parse_revision_path)
    secret_path = staticmethod(RevisionsClient.secret_path)
    parse_secret_path = staticmethod(RevisionsClient.parse_secret_path)
    secret_version_path = staticmethod(RevisionsClient.secret_version_path)
    parse_secret_version_path = staticmethod(RevisionsClient.parse_secret_version_path)
    service_path = staticmethod(RevisionsClient.service_path)
    parse_service_path = staticmethod(RevisionsClient.parse_service_path)
    common_billing_account_path = staticmethod(
        RevisionsClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        RevisionsClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(RevisionsClient.common_folder_path)
    parse_common_folder_path = staticmethod(RevisionsClient.parse_common_folder_path)
    common_organization_path = staticmethod(RevisionsClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        RevisionsClient.parse_common_organization_path
    )
    common_project_path = staticmethod(RevisionsClient.common_project_path)
    parse_common_project_path = staticmethod(RevisionsClient.parse_common_project_path)
    common_location_path = staticmethod(RevisionsClient.common_location_path)
    parse_common_location_path = staticmethod(
        RevisionsClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RevisionsAsyncClient: The constructed client.
        """
        return RevisionsClient.from_service_account_info.__func__(RevisionsAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            RevisionsAsyncClient: The constructed client.
        """
        return RevisionsClient.from_service_account_file.__func__(RevisionsAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return RevisionsClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> RevisionsTransport:
        """Returns the transport used by the client instance.

        Returns:
            RevisionsTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(RevisionsClient).get_transport_class, type(RevisionsClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, RevisionsTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the revisions client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.RevisionsTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = RevisionsClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def get_revision(
        self,
        request: Union[revision.GetRevisionRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> revision.Revision:
        r"""Gets information about a Revision.

        .. code-block:: python

            from google.cloud import run_v2

            def sample_get_revision():
                # Create a client
                client = run_v2.RevisionsClient()

                # Initialize request argument(s)
                request = run_v2.GetRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.run_v2.types.GetRevisionRequest, dict]):
                The request object. Request message for obtaining a
                Revision by its full name.
            name (:class:`str`):
                Required. The full name of the
                Revision. Format:
                projects/{project}/locations/{location}/services/{service}/revisions/{revision}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.run_v2.types.Revision:
                A Revision is an immutable snapshot
                of code and configuration.  A Revision
                references a container image. Revisions
                are only created by updates to its
                parent Service.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = revision.GetRevisionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_revision,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_revisions(
        self,
        request: Union[revision.ListRevisionsRequest, dict] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListRevisionsAsyncPager:
        r"""List Revisions from a given Service, or from a given
        location.


        .. code-block:: python

            from google.cloud import run_v2

            def sample_list_revisions():
                # Create a client
                client = run_v2.RevisionsClient()

                # Initialize request argument(s)
                request = run_v2.ListRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.run_v2.types.ListRevisionsRequest, dict]):
                The request object. Request message for retrieving a
                list of Revisions.
            parent (:class:`str`):
                Required. The Service from which the
                Revisions should be listed. To list all
                Revisions across Services, use "-"
                instead of Service name. Format:
                projects/{project}/locations/{location}/services/{service}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.run_v2.services.revisions.pagers.ListRevisionsAsyncPager:
                Response message containing a list of
                Revisions.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = revision.ListRevisionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_revisions,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListRevisionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_revision(
        self,
        request: Union[revision.DeleteRevisionRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Delete a Revision.

        .. code-block:: python

            from google.cloud import run_v2

            def sample_delete_revision():
                # Create a client
                client = run_v2.RevisionsClient()

                # Initialize request argument(s)
                request = run_v2.DeleteRevisionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_revision(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.run_v2.types.DeleteRevisionRequest, dict]):
                The request object. Request message for deleting a
                retired Revision. Revision lifecycle is usually managed
                by making changes to the parent Service. Only retired
                revisions can be deleted with this API.
            name (:class:`str`):
                Required. The name of the Revision to
                delete. Format:
                projects/{project}/locations/{location}/services/{service}/revisions/{revision}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.run_v2.types.Revision` A Revision is an immutable snapshot of code and configuration. A Revision
                   references a container image. Revisions are only
                   created by updates to its parent Service.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = revision.DeleteRevisionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_revision,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            revision.Revision,
            metadata_type=revision.Revision,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-run",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("RevisionsAsyncClient",)
