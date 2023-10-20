# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/crypto/secp256r1/keys.proto
# plugin: python-betterproto
# This file has been @generated
from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class PubKey(betterproto.Message):
    """PubKey defines a secp256r1 ECDSA public key."""

    key: bytes = betterproto.bytes_field(1)
    """
    Point on secp256r1 curve in a compressed representation as specified in section
    4.3.6 of ANSI X9.62: https://webstore.ansi.org/standards/ascx9/ansix9621998
    """


@dataclass(eq=False, repr=False)
class PrivKey(betterproto.Message):
    """PrivKey defines a secp256r1 ECDSA private key."""

    secret: bytes = betterproto.bytes_field(1)
    """secret number serialized using big-endian encoding"""
