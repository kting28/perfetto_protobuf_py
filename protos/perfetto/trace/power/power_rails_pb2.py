# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/power/power_rails.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-protos/perfetto/trace/power/power_rails.proto\x12\x0fperfetto.protos\"\xb1\x02\n\nPowerRails\x12\x43\n\x0frail_descriptor\x18\x01 \x03(\x0b\x32*.perfetto.protos.PowerRails.RailDescriptor\x12;\n\x0b\x65nergy_data\x18\x02 \x03(\x0b\x32&.perfetto.protos.PowerRails.EnergyData\x1a^\n\x0eRailDescriptor\x12\r\n\x05index\x18\x01 \x01(\r\x12\x11\n\trail_name\x18\x02 \x01(\t\x12\x13\n\x0bsubsys_name\x18\x03 \x01(\t\x12\x15\n\rsampling_rate\x18\x04 \x01(\r\x1a\x41\n\nEnergyData\x12\r\n\x05index\x18\x01 \x01(\r\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x04\x12\x0e\n\x06\x65nergy\x18\x03 \x01(\x04')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.power.power_rails_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POWERRAILS._serialized_start=67
  _POWERRAILS._serialized_end=372
  _POWERRAILS_RAILDESCRIPTOR._serialized_start=211
  _POWERRAILS_RAILDESCRIPTOR._serialized_end=305
  _POWERRAILS_ENERGYDATA._serialized_start=307
  _POWERRAILS_ENERGYDATA._serialized_end=372
# @@protoc_insertion_point(module_scope)
