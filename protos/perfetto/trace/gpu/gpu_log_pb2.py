# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/gpu/gpu_log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'protos/perfetto/trace/gpu/gpu_log.proto\x12\x0fperfetto.protos\"\x84\x02\n\x06GpuLog\x12\x32\n\x08severity\x18\x01 \x01(\x0e\x32 .perfetto.protos.GpuLog.Severity\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x13\n\x0blog_message\x18\x03 \x01(\t\"\xa3\x01\n\x08Severity\x12\x1c\n\x18LOG_SEVERITY_UNSPECIFIED\x10\x00\x12\x18\n\x14LOG_SEVERITY_VERBOSE\x10\x01\x12\x16\n\x12LOG_SEVERITY_DEBUG\x10\x02\x12\x15\n\x11LOG_SEVERITY_INFO\x10\x03\x12\x18\n\x14LOG_SEVERITY_WARNING\x10\x04\x12\x16\n\x12LOG_SEVERITY_ERROR\x10\x05')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.gpu.gpu_log_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GPULOG._serialized_start=61
  _GPULOG._serialized_end=321
  _GPULOG_SEVERITY._serialized_start=158
  _GPULOG_SEVERITY._serialized_end=321
# @@protoc_insertion_point(module_scope)
