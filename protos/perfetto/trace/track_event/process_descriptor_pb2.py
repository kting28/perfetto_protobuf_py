# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/track_event/process_descriptor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:protos/perfetto/trace/track_event/process_descriptor.proto\x12\x0fperfetto.protos\"\xe7\x03\n\x11ProcessDescriptor\x12\x0b\n\x03pid\x18\x01 \x01(\x05\x12\x0f\n\x07\x63mdline\x18\x02 \x03(\t\x12\x14\n\x0cprocess_name\x18\x06 \x01(\t\x12\x18\n\x10process_priority\x18\x05 \x01(\x05\x12\x1a\n\x12start_timestamp_ns\x18\x07 \x01(\x03\x12Q\n\x13\x63hrome_process_type\x18\x04 \x01(\x0e\x32\x34.perfetto.protos.ProcessDescriptor.ChromeProcessType\x12\x19\n\x11legacy_sort_index\x18\x03 \x01(\x05\x12\x16\n\x0eprocess_labels\x18\x08 \x03(\t\"\xe1\x01\n\x11\x43hromeProcessType\x12\x17\n\x13PROCESS_UNSPECIFIED\x10\x00\x12\x13\n\x0fPROCESS_BROWSER\x10\x01\x12\x14\n\x10PROCESS_RENDERER\x10\x02\x12\x13\n\x0fPROCESS_UTILITY\x10\x03\x12\x12\n\x0ePROCESS_ZYGOTE\x10\x04\x12\x1a\n\x16PROCESS_SANDBOX_HELPER\x10\x05\x12\x0f\n\x0bPROCESS_GPU\x10\x06\x12\x18\n\x14PROCESS_PPAPI_PLUGIN\x10\x07\x12\x18\n\x14PROCESS_PPAPI_BROKER\x10\x08')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.track_event.process_descriptor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROCESSDESCRIPTOR._serialized_start=80
  _PROCESSDESCRIPTOR._serialized_end=567
  _PROCESSDESCRIPTOR_CHROMEPROCESSTYPE._serialized_start=342
  _PROCESSDESCRIPTOR_CHROMEPROCESSTYPE._serialized_end=567
# @@protoc_insertion_point(module_scope)