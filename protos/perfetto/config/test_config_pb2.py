# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/config/test_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(protos/perfetto/config/test_config.proto\x12\x0fperfetto.protos\"\x8d\x04\n\nTestConfig\x12\x15\n\rmessage_count\x18\x01 \x01(\r\x12\x1f\n\x17max_messages_per_second\x18\x02 \x01(\r\x12\x0c\n\x04seed\x18\x03 \x01(\r\x12\x14\n\x0cmessage_size\x18\x04 \x01(\r\x12\x1e\n\x16send_batch_on_register\x18\x05 \x01(\x08\x12=\n\x0c\x64ummy_fields\x18\x06 \x01(\x0b\x32\'.perfetto.protos.TestConfig.DummyFields\x1a\xc3\x02\n\x0b\x44ummyFields\x12\x14\n\x0c\x66ield_uint32\x18\x01 \x01(\r\x12\x13\n\x0b\x66ield_int32\x18\x02 \x01(\x05\x12\x14\n\x0c\x66ield_uint64\x18\x03 \x01(\x04\x12\x13\n\x0b\x66ield_int64\x18\x04 \x01(\x03\x12\x15\n\rfield_fixed64\x18\x05 \x01(\x06\x12\x16\n\x0e\x66ield_sfixed64\x18\x06 \x01(\x10\x12\x15\n\rfield_fixed32\x18\x07 \x01(\x07\x12\x16\n\x0e\x66ield_sfixed32\x18\x08 \x01(\x0f\x12\x14\n\x0c\x66ield_double\x18\t \x01(\x01\x12\x13\n\x0b\x66ield_float\x18\n \x01(\x02\x12\x14\n\x0c\x66ield_sint64\x18\x0b \x01(\x12\x12\x14\n\x0c\x66ield_sint32\x18\x0c \x01(\x11\x12\x14\n\x0c\x66ield_string\x18\r \x01(\t\x12\x13\n\x0b\x66ield_bytes\x18\x0e \x01(\x0c')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.config.test_config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TESTCONFIG._serialized_start=62
  _TESTCONFIG._serialized_end=587
  _TESTCONFIG_DUMMYFIELDS._serialized_start=264
  _TESTCONFIG_DUMMYFIELDS._serialized_end=587
# @@protoc_insertion_point(module_scope)