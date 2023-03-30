# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/ftrace/trusty.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)protos/perfetto/trace/ftrace/trusty.proto\x12\x0fperfetto.protos\"F\n\x14TrustySmcFtraceEvent\x12\n\n\x02r0\x18\x01 \x01(\x04\x12\n\n\x02r1\x18\x02 \x01(\x04\x12\n\n\x02r2\x18\x03 \x01(\x04\x12\n\n\x02r3\x18\x04 \x01(\x04\"\'\n\x18TrustySmcDoneFtraceEvent\x12\x0b\n\x03ret\x18\x01 \x01(\x04\"L\n\x1aTrustyStdCall32FtraceEvent\x12\n\n\x02r0\x18\x01 \x01(\x04\x12\n\n\x02r1\x18\x02 \x01(\x04\x12\n\n\x02r2\x18\x03 \x01(\x04\x12\n\n\x02r3\x18\x04 \x01(\x04\"-\n\x1eTrustyStdCall32DoneFtraceEvent\x12\x0b\n\x03ret\x18\x01 \x01(\x03\"H\n\x1cTrustyShareMemoryFtraceEvent\x12\x0b\n\x03len\x18\x01 \x01(\x04\x12\x0c\n\x04lend\x18\x02 \x01(\r\x12\r\n\x05nents\x18\x03 \x01(\r\"i\n TrustyShareMemoryDoneFtraceEvent\x12\x0e\n\x06handle\x18\x01 \x01(\x04\x12\x0b\n\x03len\x18\x02 \x01(\x04\x12\x0c\n\x04lend\x18\x03 \x01(\r\x12\r\n\x05nents\x18\x04 \x01(\r\x12\x0b\n\x03ret\x18\x05 \x01(\x05\",\n\x1eTrustyReclaimMemoryFtraceEvent\x12\n\n\x02id\x18\x01 \x01(\x04\"=\n\"TrustyReclaimMemoryDoneFtraceEvent\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0b\n\x03ret\x18\x02 \x01(\x05\"#\n\x14TrustyIrqFtraceEvent\x12\x0b\n\x03irq\x18\x01 \x01(\x05\"S\n\x1fTrustyIpcHandleEventFtraceEvent\x12\x0c\n\x04\x63han\x18\x01 \x01(\r\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\r\x12\x10\n\x08srv_name\x18\x03 \x01(\t\"H\n\x1bTrustyIpcConnectFtraceEvent\x12\x0c\n\x04\x63han\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\x05\"J\n\x1eTrustyIpcConnectEndFtraceEvent\x12\x0c\n\x04\x63han\x18\x01 \x01(\r\x12\x0b\n\x03\x65rr\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\x05\"\x82\x01\n\x19TrustyIpcWriteFtraceEvent\x12\x0e\n\x06\x62uf_id\x18\x01 \x01(\x04\x12\x0c\n\x04\x63han\x18\x02 \x01(\r\x12\x10\n\x08kind_shm\x18\x03 \x01(\x05\x12\x12\n\nlen_or_err\x18\x04 \x01(\x05\x12\x0f\n\x07shm_cnt\x18\x05 \x01(\x04\x12\x10\n\x08srv_name\x18\x06 \x01(\t\"M\n\x18TrustyIpcPollFtraceEvent\x12\x0c\n\x04\x63han\x18\x01 \x01(\r\x12\x11\n\tpoll_mask\x18\x02 \x01(\r\x12\x10\n\x08srv_name\x18\x03 \x01(\t\":\n\x18TrustyIpcReadFtraceEvent\x12\x0c\n\x04\x63han\x18\x01 \x01(\r\x12\x10\n\x08srv_name\x18\x02 \x01(\t\"r\n\x1bTrustyIpcReadEndFtraceEvent\x12\x0e\n\x06\x62uf_id\x18\x01 \x01(\x04\x12\x0c\n\x04\x63han\x18\x02 \x01(\r\x12\x12\n\nlen_or_err\x18\x03 \x01(\x05\x12\x0f\n\x07shm_cnt\x18\x04 \x01(\x04\x12\x10\n\x08srv_name\x18\x05 \x01(\t\"H\n\x16TrustyIpcRxFtraceEvent\x12\x0e\n\x06\x62uf_id\x18\x01 \x01(\x04\x12\x0c\n\x04\x63han\x18\x02 \x01(\r\x12\x10\n\x08srv_name\x18\x03 \x01(\t\"G\n\x1bTrustyEnqueueNopFtraceEvent\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\r\x12\x0c\n\x04\x61rg2\x18\x02 \x01(\r\x12\x0c\n\x04\x61rg3\x18\x03 \x01(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.ftrace.trusty_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRUSTYSMCFTRACEEVENT._serialized_start=62
  _TRUSTYSMCFTRACEEVENT._serialized_end=132
  _TRUSTYSMCDONEFTRACEEVENT._serialized_start=134
  _TRUSTYSMCDONEFTRACEEVENT._serialized_end=173
  _TRUSTYSTDCALL32FTRACEEVENT._serialized_start=175
  _TRUSTYSTDCALL32FTRACEEVENT._serialized_end=251
  _TRUSTYSTDCALL32DONEFTRACEEVENT._serialized_start=253
  _TRUSTYSTDCALL32DONEFTRACEEVENT._serialized_end=298
  _TRUSTYSHAREMEMORYFTRACEEVENT._serialized_start=300
  _TRUSTYSHAREMEMORYFTRACEEVENT._serialized_end=372
  _TRUSTYSHAREMEMORYDONEFTRACEEVENT._serialized_start=374
  _TRUSTYSHAREMEMORYDONEFTRACEEVENT._serialized_end=479
  _TRUSTYRECLAIMMEMORYFTRACEEVENT._serialized_start=481
  _TRUSTYRECLAIMMEMORYFTRACEEVENT._serialized_end=525
  _TRUSTYRECLAIMMEMORYDONEFTRACEEVENT._serialized_start=527
  _TRUSTYRECLAIMMEMORYDONEFTRACEEVENT._serialized_end=588
  _TRUSTYIRQFTRACEEVENT._serialized_start=590
  _TRUSTYIRQFTRACEEVENT._serialized_end=625
  _TRUSTYIPCHANDLEEVENTFTRACEEVENT._serialized_start=627
  _TRUSTYIPCHANDLEEVENTFTRACEEVENT._serialized_end=710
  _TRUSTYIPCCONNECTFTRACEEVENT._serialized_start=712
  _TRUSTYIPCCONNECTFTRACEEVENT._serialized_end=784
  _TRUSTYIPCCONNECTENDFTRACEEVENT._serialized_start=786
  _TRUSTYIPCCONNECTENDFTRACEEVENT._serialized_end=860
  _TRUSTYIPCWRITEFTRACEEVENT._serialized_start=863
  _TRUSTYIPCWRITEFTRACEEVENT._serialized_end=993
  _TRUSTYIPCPOLLFTRACEEVENT._serialized_start=995
  _TRUSTYIPCPOLLFTRACEEVENT._serialized_end=1072
  _TRUSTYIPCREADFTRACEEVENT._serialized_start=1074
  _TRUSTYIPCREADFTRACEEVENT._serialized_end=1132
  _TRUSTYIPCREADENDFTRACEEVENT._serialized_start=1134
  _TRUSTYIPCREADENDFTRACEEVENT._serialized_end=1248
  _TRUSTYIPCRXFTRACEEVENT._serialized_start=1250
  _TRUSTYIPCRXFTRACEEVENT._serialized_end=1322
  _TRUSTYENQUEUENOPFTRACEEVENT._serialized_start=1324
  _TRUSTYENQUEUENOPFTRACEEVENT._serialized_end=1395
# @@protoc_insertion_point(module_scope)
