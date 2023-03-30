# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/common/data_source_descriptor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.perfetto.common import ftrace_descriptor_pb2 as protos_dot_perfetto_dot_common_dot_ftrace__descriptor__pb2
from protos.perfetto.common import gpu_counter_descriptor_pb2 as protos_dot_perfetto_dot_common_dot_gpu__counter__descriptor__pb2
from protos.perfetto.common import track_event_descriptor_pb2 as protos_dot_perfetto_dot_common_dot_track__event__descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3protos/perfetto/common/data_source_descriptor.proto\x12\x0fperfetto.protos\x1a.protos/perfetto/common/ftrace_descriptor.proto\x1a\x33protos/perfetto/common/gpu_counter_descriptor.proto\x1a\x33protos/perfetto/common/track_event_descriptor.proto\"\xec\x02\n\x14\x44\x61taSourceDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x07 \x01(\x04\x12\x1b\n\x13will_notify_on_stop\x18\x02 \x01(\x08\x12\x1c\n\x14will_notify_on_start\x18\x03 \x01(\x08\x12\'\n\x1fhandles_incremental_state_clear\x18\x04 \x01(\x08\x12I\n\x16gpu_counter_descriptor\x18\x05 \x01(\x0b\x32%.perfetto.protos.GpuCounterDescriptorB\x02(\x01\x12I\n\x16track_event_descriptor\x18\x06 \x01(\x0b\x32%.perfetto.protos.TrackEventDescriptorB\x02(\x01\x12@\n\x11\x66trace_descriptor\x18\x08 \x01(\x0b\x32!.perfetto.protos.FtraceDescriptorB\x02(\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.common.data_source_descriptor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATASOURCEDESCRIPTOR.fields_by_name['gpu_counter_descriptor']._options = None
  _DATASOURCEDESCRIPTOR.fields_by_name['gpu_counter_descriptor']._serialized_options = b'(\001'
  _DATASOURCEDESCRIPTOR.fields_by_name['track_event_descriptor']._options = None
  _DATASOURCEDESCRIPTOR.fields_by_name['track_event_descriptor']._serialized_options = b'(\001'
  _DATASOURCEDESCRIPTOR.fields_by_name['ftrace_descriptor']._options = None
  _DATASOURCEDESCRIPTOR.fields_by_name['ftrace_descriptor']._serialized_options = b'(\001'
  _DATASOURCEDESCRIPTOR._serialized_start=227
  _DATASOURCEDESCRIPTOR._serialized_end=591
# @@protoc_insertion_point(module_scope)
