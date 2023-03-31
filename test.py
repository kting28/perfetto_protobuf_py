import gen.perfetto_trace_pb2 as trace

TYPE_UNSPECIFIED = trace.TrackEvent.Type.TYPE_UNSPECIFIED
TYPE_SLICE_BEGIN = trace.TrackEvent.Type.TYPE_SLICE_BEGIN
TYPE_SLICE_END = trace.TrackEvent.Type.TYPE_SLICE_END
TYPE_INSTANT = trace.TrackEvent.Type.TYPE_INSTANT
TYPE_COUNTER = trace.TrackEvent.Type.TYPE_COUNTER

top = trace.Trace()

#tc = trace_config.TraceConfig()
#ds = trace_config.TraceConfig.DataSource() 
#ds.config.name = "track_event"
#tc.data_sources.append(ds)
#
#
tp = trace.TracePacket()
tp.track_descriptor.uuid = 894893984 
tp.track_descriptor.process.pid = 1234
tp.track_descriptor.process.process_name = "My process name"
top.packet.append(tp)


tp = trace.TracePacket()
tp.track_descriptor.uuid = 49083589894
tp.track_descriptor.parent_uuid = 894893984
tp.track_descriptor.thread.pid = 1234
tp.track_descriptor.thread.tid = 5678
tp.track_descriptor.thread.thread_name = "My thread name"

top.packet.append(tp)

tp = trace.TracePacket()

da1 = trace.DebugAnnotation()
da1.name = "foo"
da1.int_value = 42
da2 = trace.DebugAnnotation()
da2.name = "bar"
da2.int_value = 42

da3 = trace.DebugAnnotation()
da3.name ="args"
da3.dict_entries.append(da1)
da3.dict_entries.append(da2)

tp.timestamp = 200
tp.track_event.type = TYPE_SLICE_BEGIN
tp.track_event.track_uuid = 49083589894
tp.track_event.name = "My special parent"
tp.track_event.debug_annotations.append(da3)
tp.trusted_packet_sequence_id = 3903809


top.packet.append(tp)

tp = trace.TracePacket()
tp.timestamp = 250
tp.track_event.type = TYPE_SLICE_BEGIN
tp.track_event.track_uuid = 49083589894
tp.track_event.name = "My special child"
tp.trusted_packet_sequence_id = 3903809

top.packet.append(tp)

tp = trace.TracePacket()

tp.timestamp = 290
tp.track_event.type = TYPE_SLICE_END
tp.track_event.track_uuid = 49083589894
tp.trusted_packet_sequence_id = 3903809

top.packet.append(tp)

tp = trace.TracePacket()
tp.timestamp = 300
tp.track_event.type = TYPE_SLICE_END
tp.track_event.track_uuid = 49083589894
tp.trusted_packet_sequence_id = 3903809


with open("./output.perfetto-trace", "wb") as fd:
    print(top)
    fd.write(top.SerializeToString())

