# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/ftrace/sync.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'protos/perfetto/trace/ftrace/sync.proto\x12\x0fperfetto.protos\"4\n\x11SyncPtFtraceEvent\x12\x10\n\x08timeline\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"6\n\x17SyncTimelineFtraceEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"B\n\x13SyncWaitFtraceEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\r\n\x05\x62\x65gin\x18\x03 \x01(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.ftrace.sync_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYNCPTFTRACEEVENT._serialized_start=60
  _SYNCPTFTRACEEVENT._serialized_end=112
  _SYNCTIMELINEFTRACEEVENT._serialized_start=114
  _SYNCTIMELINEFTRACEEVENT._serialized_end=168
  _SYNCWAITFTRACEEVENT._serialized_start=170
  _SYNCWAITFTRACEEVENT._serialized_end=236
# @@protoc_insertion_point(module_scope)