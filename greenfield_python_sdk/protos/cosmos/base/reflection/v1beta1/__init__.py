# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/base/reflection/v1beta1/reflection.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List, Optional

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class ListAllInterfacesRequest(betterproto.Message):
    """ListAllInterfacesRequest is the request type of the ListAllInterfaces RPC."""

    pass


@dataclass(eq=False, repr=False)
class ListAllInterfacesResponse(betterproto.Message):
    """ListAllInterfacesResponse is the response type of the ListAllInterfaces RPC."""

    interface_names: List[str] = betterproto.string_field(1)
    """interface_names is an array of all the registered interfaces."""


@dataclass(eq=False, repr=False)
class ListImplementationsRequest(betterproto.Message):
    """
    ListImplementationsRequest is the request type of the ListImplementations
    RPC.
    """

    interface_name: str = betterproto.string_field(1)
    """interface_name defines the interface to query the implementations for."""


@dataclass(eq=False, repr=False)
class ListImplementationsResponse(betterproto.Message):
    """
    ListImplementationsResponse is the response type of the ListImplementations
    RPC.
    """

    implementation_message_names: List[str] = betterproto.string_field(1)


class ReflectionServiceStub(betterproto.ServiceStub):
    async def list_all_interfaces(
        self,
        list_all_interfaces_request: "ListAllInterfacesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ListAllInterfacesResponse":
        return await self._unary_unary(
            "/cosmos.base.reflection.v1beta1.ReflectionService/ListAllInterfaces",
            list_all_interfaces_request,
            ListAllInterfacesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def list_implementations(
        self,
        list_implementations_request: "ListImplementationsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ListImplementationsResponse":
        return await self._unary_unary(
            "/cosmos.base.reflection.v1beta1.ReflectionService/ListImplementations",
            list_implementations_request,
            ListImplementationsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class ReflectionServiceBase(ServiceBase):
    async def list_all_interfaces(
        self, list_all_interfaces_request: "ListAllInterfacesRequest"
    ) -> "ListAllInterfacesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_implementations(
        self, list_implementations_request: "ListImplementationsRequest"
    ) -> "ListImplementationsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_list_all_interfaces(
        self,
        stream: "grpclib.server.Stream[ListAllInterfacesRequest, ListAllInterfacesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.list_all_interfaces(request)
        await stream.send_message(response)

    async def __rpc_list_implementations(
        self,
        stream: "grpclib.server.Stream[ListImplementationsRequest, ListImplementationsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.list_implementations(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.base.reflection.v1beta1.ReflectionService/ListAllInterfaces": grpclib.const.Handler(
                self.__rpc_list_all_interfaces,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListAllInterfacesRequest,
                ListAllInterfacesResponse,
            ),
            "/cosmos.base.reflection.v1beta1.ReflectionService/ListImplementations": grpclib.const.Handler(
                self.__rpc_list_implementations,
                grpclib.const.Cardinality.UNARY_UNARY,
                ListImplementationsRequest,
                ListImplementationsResponse,
            ),
        }
