# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/crosschain/v1/crosschain.proto, cosmos/crosschain/v1/event.proto, cosmos/crosschain/v1/genesis.proto, cosmos/crosschain/v1/query.proto, cosmos/crosschain/v1/tx.proto
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
class Params(betterproto.Message):
    """Params holds parameters for the cross chain module."""

    init_module_balance: str = betterproto.string_field(1)
    """initial balance to mint for crosschain module when the chain starts"""


@dataclass(eq=False, repr=False)
class ChannelPermission(betterproto.Message):
    """ChannelPermission defines the fields of the channel permission"""

    dest_chain_id: int = betterproto.uint32_field(1)
    """destination chain id"""

    channel_id: int = betterproto.uint32_field(2)
    """channel id"""

    permission: int = betterproto.uint32_field(3)
    """permission status, 1 for allow, 0 for forbidden"""


@dataclass(eq=False, repr=False)
class EventCrossChain(betterproto.Message):
    """EventCrossChain is emitted when there is a cross chain package created"""

    src_chain_id: int = betterproto.uint32_field(1)
    """Source chain id of the cross chain package"""

    dest_chain_id: int = betterproto.uint32_field(2)
    """Destination chain id of the cross chainpackage"""

    channel_id: int = betterproto.uint32_field(3)
    """Channel id of the cross chain package"""

    sequence: int = betterproto.uint64_field(4)
    """Sequence of the cross chain package"""

    package_type: int = betterproto.uint32_field(5)
    """Package type of the cross chain package, like SYN, ACK and FAIL_ACK"""

    timestamp: int = betterproto.uint64_field(6)
    """Timestamp of the cross chain package"""

    package_load: str = betterproto.string_field(7)
    """Payload of the cross chain package"""

    relayer_fee: str = betterproto.string_field(8)
    """Relayer fee for the cross chain package"""

    ack_relayer_fee: str = betterproto.string_field(9)
    """Relayer fee for the ACK or FAIL_ACK package of this cross chain package"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the oracle module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the parameters of related to oracle module."""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    params: "Params" = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class QueryCrossChainPackageRequest(betterproto.Message):
    """
    QueryCrossChainPackageRequest is the request type for the Query/CrossChainPackage
    RPC method.
    """

    dest_chain_id: int = betterproto.uint32_field(1)
    """destination chain id"""

    channel_id: int = betterproto.uint32_field(2)
    """channel id of the cross chain package"""

    sequence: int = betterproto.uint64_field(3)
    """sequence of the cross chain package"""


@dataclass(eq=False, repr=False)
class QueryCrossChainPackageResponse(betterproto.Message):
    """
    QueryCrossChainPackageResponse is the response type for the Query/CrossChainPackage
    RPC method.
    """

    package: bytes = betterproto.bytes_field(1)
    """content of the cross chain package"""


@dataclass(eq=False, repr=False)
class QuerySendSequenceRequest(betterproto.Message):
    """
    QuerySendSequenceRequest is the request type for the Query/SendSequence RPC method.
    """

    dest_chain_id: int = betterproto.uint32_field(1)
    """destination chain id"""

    channel_id: int = betterproto.uint32_field(2)
    """channel id of the cross chain package"""


@dataclass(eq=False, repr=False)
class QuerySendSequenceResponse(betterproto.Message):
    """
    QuerySendSequenceResponse is the response type for the Query/SendSequence RPC
    method.
    """

    sequence: int = betterproto.uint64_field(1)
    """sequence of the cross chain package"""


@dataclass(eq=False, repr=False)
class QueryReceiveSequenceRequest(betterproto.Message):
    """
    QuerySendSequenceRequest is the request type for the Query/ReceiveSequence RPC
    method.
    """

    dest_chain_id: int = betterproto.uint32_field(1)
    """destination chain id"""

    channel_id: int = betterproto.uint32_field(2)
    """channel id of the cross chain package"""


@dataclass(eq=False, repr=False)
class QueryReceiveSequenceResponse(betterproto.Message):
    """
    QuerySendSequenceResponse is the response type for the Query/ReceiveSequence RPC
    method.
    """

    sequence: int = betterproto.uint64_field(1)
    """sequence of the cross chain package"""


@dataclass(eq=False, repr=False)
class MsgUpdateParams(betterproto.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless
    overwritten).
    """

    params: "Params" = betterproto.message_field(2)
    """
    params defines the x/crosschain parameters to update.
    NOTE: All parameters must be supplied.
    """


@dataclass(eq=False, repr=False)
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgUpdateChannelPermissions(betterproto.Message):
    """
    MsgUpdateChannelPermissions is the Msg/MsgUpdateChannelPermissions request type.
    """

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless
    overwritten).
    """

    channel_permissions: List["ChannelPermission"] = betterproto.message_field(2)
    """channel_permissions defines the channel permissions to update"""


@dataclass(eq=False, repr=False)
class MsgUpdateChannelPermissionsResponse(betterproto.Message):
    """
    MsgUpdateChannelPermissionsResponse defines the response structure for executing a
    MsgUpdateChannelPermissions message.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgMintModuleTokens(betterproto.Message):
    """
    MsgMintModuleTokens is the Msg/MintModuleTokens request type.
    The Msg is used to mint tokens for the crosschain module.
    This Only permitted to be called by the authority(gov).
    """

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless
    overwritten).
    """

    amount: str = betterproto.string_field(2)
    """initial balance to mint for crosschain module when the chain starts"""


@dataclass(eq=False, repr=False)
class MsgMintModuleTokensResponse(betterproto.Message):
    """
    MsgMintModuleTokensResponse defines the response structure for executing a
    MsgMintModuleTokens message.
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.crosschain.v1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def cross_chain_package(
        self,
        query_cross_chain_package_request: "QueryCrossChainPackageRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryCrossChainPackageResponse":
        return await self._unary_unary(
            "/cosmos.crosschain.v1.Query/CrossChainPackage",
            query_cross_chain_package_request,
            QueryCrossChainPackageResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def send_sequence(
        self,
        query_send_sequence_request: "QuerySendSequenceRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QuerySendSequenceResponse":
        return await self._unary_unary(
            "/cosmos.crosschain.v1.Query/SendSequence",
            query_send_sequence_request,
            QuerySendSequenceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def receive_sequence(
        self,
        query_receive_sequence_request: "QueryReceiveSequenceRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryReceiveSequenceResponse":
        return await self._unary_unary(
            "/cosmos.crosschain.v1.Query/ReceiveSequence",
            query_receive_sequence_request,
            QueryReceiveSequenceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def update_params(
        self,
        msg_update_params: "MsgUpdateParams",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgUpdateParamsResponse":
        return await self._unary_unary(
            "/cosmos.crosschain.v1.Msg/UpdateParams",
            msg_update_params,
            MsgUpdateParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_channel_permissions(
        self,
        msg_update_channel_permissions: "MsgUpdateChannelPermissions",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgUpdateChannelPermissionsResponse":
        return await self._unary_unary(
            "/cosmos.crosschain.v1.Msg/UpdateChannelPermissions",
            msg_update_channel_permissions,
            MsgUpdateChannelPermissionsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def mint_module_tokens(
        self,
        msg_mint_module_tokens: "MsgMintModuleTokens",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgMintModuleTokensResponse":
        return await self._unary_unary(
            "/cosmos.crosschain.v1.Msg/MintModuleTokens",
            msg_mint_module_tokens,
            MsgMintModuleTokensResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def params(self, query_params_request: "QueryParamsRequest") -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def cross_chain_package(
        self, query_cross_chain_package_request: "QueryCrossChainPackageRequest"
    ) -> "QueryCrossChainPackageResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def send_sequence(
        self, query_send_sequence_request: "QuerySendSequenceRequest"
    ) -> "QuerySendSequenceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def receive_sequence(
        self, query_receive_sequence_request: "QueryReceiveSequenceRequest"
    ) -> "QueryReceiveSequenceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]") -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_cross_chain_package(
        self,
        stream: "grpclib.server.Stream[QueryCrossChainPackageRequest, QueryCrossChainPackageResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.cross_chain_package(request)
        await stream.send_message(response)

    async def __rpc_send_sequence(
        self,
        stream: "grpclib.server.Stream[QuerySendSequenceRequest, QuerySendSequenceResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.send_sequence(request)
        await stream.send_message(response)

    async def __rpc_receive_sequence(
        self,
        stream: "grpclib.server.Stream[QueryReceiveSequenceRequest, QueryReceiveSequenceResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.receive_sequence(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.crosschain.v1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.crosschain.v1.Query/CrossChainPackage": grpclib.const.Handler(
                self.__rpc_cross_chain_package,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryCrossChainPackageRequest,
                QueryCrossChainPackageResponse,
            ),
            "/cosmos.crosschain.v1.Query/SendSequence": grpclib.const.Handler(
                self.__rpc_send_sequence,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySendSequenceRequest,
                QuerySendSequenceResponse,
            ),
            "/cosmos.crosschain.v1.Query/ReceiveSequence": grpclib.const.Handler(
                self.__rpc_receive_sequence,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryReceiveSequenceRequest,
                QueryReceiveSequenceResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def update_params(self, msg_update_params: "MsgUpdateParams") -> "MsgUpdateParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_channel_permissions(
        self, msg_update_channel_permissions: "MsgUpdateChannelPermissions"
    ) -> "MsgUpdateChannelPermissionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def mint_module_tokens(self, msg_mint_module_tokens: "MsgMintModuleTokens") -> "MsgMintModuleTokensResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_update_params(
        self, stream: "grpclib.server.Stream[MsgUpdateParams, MsgUpdateParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_params(request)
        await stream.send_message(response)

    async def __rpc_update_channel_permissions(
        self,
        stream: "grpclib.server.Stream[MsgUpdateChannelPermissions, MsgUpdateChannelPermissionsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_channel_permissions(request)
        await stream.send_message(response)

    async def __rpc_mint_module_tokens(
        self,
        stream: "grpclib.server.Stream[MsgMintModuleTokens, MsgMintModuleTokensResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.mint_module_tokens(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.crosschain.v1.Msg/UpdateParams": grpclib.const.Handler(
                self.__rpc_update_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateParams,
                MsgUpdateParamsResponse,
            ),
            "/cosmos.crosschain.v1.Msg/UpdateChannelPermissions": grpclib.const.Handler(
                self.__rpc_update_channel_permissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateChannelPermissions,
                MsgUpdateChannelPermissionsResponse,
            ),
            "/cosmos.crosschain.v1.Msg/MintModuleTokens": grpclib.const.Handler(
                self.__rpc_mint_module_tokens,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgMintModuleTokens,
                MsgMintModuleTokensResponse,
            ),
        }
