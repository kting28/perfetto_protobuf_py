# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/power/android_energy_estimation_breakdown.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.perfetto.common import android_energy_consumer_descriptor_pb2 as protos_dot_perfetto_dot_common_dot_android__energy__consumer__descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEprotos/perfetto/trace/power/android_energy_estimation_breakdown.proto\x12\x0fperfetto.protos\x1a?protos/perfetto/common/android_energy_consumer_descriptor.proto\"\xc0\x02\n AndroidEnergyEstimationBreakdown\x12T\n\x1a\x65nergy_consumer_descriptor\x18\x01 \x01(\x0b\x32\x30.perfetto.protos.AndroidEnergyConsumerDescriptor\x12\x1a\n\x12\x65nergy_consumer_id\x18\x02 \x01(\x05\x12\x12\n\nenergy_uws\x18\x03 \x01(\x03\x12_\n\x11per_uid_breakdown\x18\x04 \x03(\x0b\x32\x44.perfetto.protos.AndroidEnergyEstimationBreakdown.EnergyUidBreakdown\x1a\x35\n\x12\x45nergyUidBreakdown\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x12\n\nenergy_uws\x18\x02 \x01(\x03')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.power.android_energy_estimation_breakdown_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ANDROIDENERGYESTIMATIONBREAKDOWN._serialized_start=156
  _ANDROIDENERGYESTIMATIONBREAKDOWN._serialized_end=476
  _ANDROIDENERGYESTIMATIONBREAKDOWN_ENERGYUIDBREAKDOWN._serialized_start=423
  _ANDROIDENERGYESTIMATIONBREAKDOWN_ENERGYUIDBREAKDOWN._serialized_end=476
# @@protoc_insertion_point(module_scope)
