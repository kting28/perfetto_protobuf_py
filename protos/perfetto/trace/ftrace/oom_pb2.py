# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/ftrace/oom.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&protos/perfetto/trace/ftrace/oom.proto\x12\x0fperfetto.protos\"P\n\x1cOomScoreAdjUpdateFtraceEvent\x12\x0c\n\x04\x63omm\x18\x01 \x01(\t\x12\x15\n\room_score_adj\x18\x02 \x01(\x05\x12\x0b\n\x03pid\x18\x03 \x01(\x05\"$\n\x15MarkVictimFtraceEvent\x12\x0b\n\x03pid\x18\x01 \x01(\x05')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.ftrace.oom_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OOMSCOREADJUPDATEFTRACEEVENT._serialized_start=59
  _OOMSCOREADJUPDATEFTRACEEVENT._serialized_end=139
  _MARKVICTIMFTRACEEVENT._serialized_start=141
  _MARKVICTIMFTRACEEVENT._serialized_end=177
# @@protoc_insertion_point(module_scope)
