# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/track_event/chrome_renderer_scheduler_state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGprotos/perfetto/trace/track_event/chrome_renderer_scheduler_state.proto\x12\x0fperfetto.protos\"~\n\x1c\x43hromeRendererSchedulerState\x12\x32\n\trail_mode\x18\x01 \x01(\x0e\x32\x1f.perfetto.protos.ChromeRAILMode\x12\x17\n\x0fis_backgrounded\x18\x02 \x01(\x08\x12\x11\n\tis_hidden\x18\x03 \x01(\x08*}\n\x0e\x43hromeRAILMode\x12\x12\n\x0eRAIL_MODE_NONE\x10\x00\x12\x16\n\x12RAIL_MODE_RESPONSE\x10\x01\x12\x17\n\x13RAIL_MODE_ANIMATION\x10\x02\x12\x12\n\x0eRAIL_MODE_IDLE\x10\x03\x12\x12\n\x0eRAIL_MODE_LOAD\x10\x04')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.track_event.chrome_renderer_scheduler_state_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHROMERAILMODE._serialized_start=220
  _CHROMERAILMODE._serialized_end=345
  _CHROMERENDERERSCHEDULERSTATE._serialized_start=92
  _CHROMERENDERERSCHEDULERSTATE._serialized_end=218
# @@protoc_insertion_point(module_scope)
