# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/trace.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.perfetto.trace import trace_packet_pb2 as protos_dot_perfetto_dot_trace_dot_trace__packet__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!protos/perfetto/trace/trace.proto\x12\x0fperfetto.protos\x1a(protos/perfetto/trace/trace_packet.proto\"5\n\x05Trace\x12,\n\x06packet\x18\x01 \x03(\x0b\x32\x1c.perfetto.protos.TracePacket')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.trace_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRACE._serialized_start=96
  _TRACE._serialized_end=149
# @@protoc_insertion_point(module_scope)