# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/config/sys_stats/sys_stats_config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.perfetto.common import sys_stats_counters_pb2 as protos_dot_perfetto_dot_common_dot_sys__stats__counters__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7protos/perfetto/config/sys_stats/sys_stats_config.proto\x12\x0fperfetto.protos\x1a/protos/perfetto/common/sys_stats_counters.proto\"\x84\x04\n\x0eSysStatsConfig\x12\x19\n\x11meminfo_period_ms\x18\x01 \x01(\r\x12:\n\x10meminfo_counters\x18\x02 \x03(\x0e\x32 .perfetto.protos.MeminfoCounters\x12\x18\n\x10vmstat_period_ms\x18\x03 \x01(\r\x12\x38\n\x0fvmstat_counters\x18\x04 \x03(\x0e\x32\x1f.perfetto.protos.VmstatCounters\x12\x16\n\x0estat_period_ms\x18\x05 \x01(\r\x12\x43\n\rstat_counters\x18\x06 \x03(\x0e\x32,.perfetto.protos.SysStatsConfig.StatCounters\x12\x19\n\x11\x64\x65vfreq_period_ms\x18\x07 \x01(\r\x12\x19\n\x11\x63pufreq_period_ms\x18\x08 \x01(\r\x12\x1b\n\x13\x62uddyinfo_period_ms\x18\t \x01(\r\x12\x1a\n\x12\x64iskstat_period_ms\x18\n \x01(\r\"{\n\x0cStatCounters\x12\x14\n\x10STAT_UNSPECIFIED\x10\x00\x12\x12\n\x0eSTAT_CPU_TIMES\x10\x01\x12\x13\n\x0fSTAT_IRQ_COUNTS\x10\x02\x12\x17\n\x13STAT_SOFTIRQ_COUNTS\x10\x03\x12\x13\n\x0fSTAT_FORK_COUNT\x10\x04')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.config.sys_stats.sys_stats_config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYSSTATSCONFIG._serialized_start=126
  _SYSSTATSCONFIG._serialized_end=642
  _SYSSTATSCONFIG_STATCOUNTERS._serialized_start=519
  _SYSSTATSCONFIG_STATCOUNTERS._serialized_end=642
# @@protoc_insertion_point(module_scope)
