# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/interned_data/interned_data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.perfetto.trace.android import network_trace_pb2 as protos_dot_perfetto_dot_trace_dot_android_dot_network__trace__pb2
from protos.perfetto.trace.gpu import gpu_render_stage_event_pb2 as protos_dot_perfetto_dot_trace_dot_gpu_dot_gpu__render__stage__event__pb2
from protos.perfetto.trace.track_event import chrome_histogram_sample_pb2 as protos_dot_perfetto_dot_trace_dot_track__event_dot_chrome__histogram__sample__pb2
from protos.perfetto.trace.track_event import debug_annotation_pb2 as protos_dot_perfetto_dot_trace_dot_track__event_dot_debug__annotation__pb2
from protos.perfetto.trace.track_event import log_message_pb2 as protos_dot_perfetto_dot_trace_dot_track__event_dot_log__message__pb2
from protos.perfetto.trace.track_event import track_event_pb2 as protos_dot_perfetto_dot_trace_dot_track__event_dot_track__event__pb2
from protos.perfetto.trace.track_event import source_location_pb2 as protos_dot_perfetto_dot_trace_dot_track__event_dot_source__location__pb2
from protos.perfetto.trace.profiling import profile_common_pb2 as protos_dot_perfetto_dot_trace_dot_profiling_dot_profile__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7protos/perfetto/trace/interned_data/interned_data.proto\x12\x0fperfetto.protos\x1a\x31protos/perfetto/trace/android/network_trace.proto\x1a\x36protos/perfetto/trace/gpu/gpu_render_stage_event.proto\x1a?protos/perfetto/trace/track_event/chrome_histogram_sample.proto\x1a\x38protos/perfetto/trace/track_event/debug_annotation.proto\x1a\x33protos/perfetto/trace/track_event/log_message.proto\x1a\x33protos/perfetto/trace/track_event/track_event.proto\x1a\x37protos/perfetto/trace/track_event/source_location.proto\x1a\x34protos/perfetto/trace/profiling/profile_common.proto\"\xd8\n\n\x0cInternedData\x12\x38\n\x10\x65vent_categories\x18\x01 \x03(\x0b\x32\x1e.perfetto.protos.EventCategory\x12/\n\x0b\x65vent_names\x18\x02 \x03(\x0b\x32\x1a.perfetto.protos.EventName\x12\x44\n\x16\x64\x65\x62ug_annotation_names\x18\x03 \x03(\x0b\x32$.perfetto.protos.DebugAnnotationName\x12X\n!debug_annotation_value_type_names\x18\x1b \x03(\x0b\x32-.perfetto.protos.DebugAnnotationValueTypeName\x12\x39\n\x10source_locations\x18\x04 \x03(\x0b\x32\x1f.perfetto.protos.SourceLocation\x12R\n\x1dunsymbolized_source_locations\x18\x1c \x03(\x0b\x32+.perfetto.protos.UnsymbolizedSourceLocation\x12\x39\n\x10log_message_body\x18\x14 \x03(\x0b\x32\x1f.perfetto.protos.LogMessageBody\x12\x37\n\x0fhistogram_names\x18\x19 \x03(\x0b\x32\x1e.perfetto.protos.HistogramName\x12\x32\n\tbuild_ids\x18\x10 \x03(\x0b\x32\x1f.perfetto.protos.InternedString\x12\x36\n\rmapping_paths\x18\x11 \x03(\x0b\x32\x1f.perfetto.protos.InternedString\x12\x35\n\x0csource_paths\x18\x12 \x03(\x0b\x32\x1f.perfetto.protos.InternedString\x12\x37\n\x0e\x66unction_names\x18\x05 \x03(\x0b\x32\x1f.perfetto.protos.InternedString\x12\x45\n\x16profiled_frame_symbols\x18\x15 \x03(\x0b\x32%.perfetto.protos.ProfiledFrameSymbols\x12*\n\x08mappings\x18\x13 \x03(\x0b\x32\x18.perfetto.protos.Mapping\x12&\n\x06\x66rames\x18\x06 \x03(\x0b\x32\x16.perfetto.protos.Frame\x12.\n\ncallstacks\x18\x07 \x03(\x0b\x32\x1a.perfetto.protos.Callstack\x12;\n\x12vulkan_memory_keys\x18\x16 \x03(\x0b\x32\x1f.perfetto.protos.InternedString\x12\x43\n\x11graphics_contexts\x18\x17 \x03(\x0b\x32(.perfetto.protos.InternedGraphicsContext\x12P\n\x12gpu_specifications\x18\x18 \x03(\x0b\x32\x34.perfetto.protos.InternedGpuRenderStageSpecification\x12\x37\n\x0ekernel_symbols\x18\x1a \x03(\x0b\x32\x1f.perfetto.protos.InternedString\x12G\n\x1e\x64\x65\x62ug_annotation_string_values\x18\x1d \x03(\x0b\x32\x1f.perfetto.protos.InternedString\x12=\n\x0epacket_context\x18\x1e \x03(\x0b\x32%.perfetto.protos.NetworkPacketContext')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.interned_data.interned_data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INTERNEDDATA._serialized_start=524
  _INTERNEDDATA._serialized_end=1892
# @@protoc_insertion_point(module_scope)
