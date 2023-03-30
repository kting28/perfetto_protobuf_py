from protos.perfetto.trace import trace_packet_pb2 as trace_packet
from protos.perfetto.config import trace_config_pb2 as trace_config
from protos.perfetto.trace.track_event import track_event_pb2 as track_event
from protos.perfetto.trace.track_event import track_descriptor_pb2 as track_descriptor

TYPE_UNSPECIFIED = track_event.TrackEvent.Type.TYPE_UNSPECIFIED
TYPE_SLICE_BEGIN = track_event.TrackEvent.Type.TYPE_SLICE_BEGIN
TYPE_SLICE_END = track_event.TrackEvent.Type.TYPE_SLICE_END
TYPE_INSTANT = track_event.TrackEvent.Type.TYPE_INSTANT
TYPE_COUNTER = track_event.TrackEvent.Type.TYPE_COUNTER

packet_list = []

tc = trace_config.TraceConfig()
ds = trace_config.TraceConfig.DataSource() 
ds.config.name = "track_event"
tc.data_sources.append(ds)

packet_list.append(tc)

tp = trace_packet.TracePacket()
tp.track_descriptor.uuid = 894893984 
tp.track_descriptor.process.pid = 1234
tp.track_descriptor.process.process_name = "My process name"

packet_list.append(tp)


tp = trace_packet.TracePacket()
tp.track_descriptor.uuid = 49083589894
tp.track_descriptor.parent_uuid = 894893984
tp.track_descriptor.thread.pid = 1234
tp.track_descriptor.thread.tid = 5678
tp.track_descriptor.thread.thread_name = "My thread name"

packet_list.append(tp)

tp = trace_packet.TracePacket()

tp.timestamp = 200
tp.track_event.type = TYPE_SLICE_BEGIN
tp.track_event.track_uuid = 49083589894
tp.track_event.name = "My special parent"
tp.trusted_packet_sequence_id = 3903809

packet_list.append(tp)

tp = trace_packet.TracePacket()
tp.timestamp = 250
tp.track_event.type = TYPE_SLICE_BEGIN
tp.track_event.track_uuid = 49083589894
tp.track_event.name = "My special child"
tp.trusted_packet_sequence_id = 3903809

packet_list.append(tp)

tp = trace_packet.TracePacket()

tp.timestamp = 290
tp.track_event.type = TYPE_SLICE_END
tp.track_event.track_uuid = 49083589894
tp.trusted_packet_sequence_id = 3903809

packet_list.append(tp)

tp = trace_packet.TracePacket()
tp.timestamp = 300
tp.track_event.type = TYPE_SLICE_END
tp.track_event.track_uuid = 49083589894
tp.trusted_packet_sequence_id = 3903809

packet_list.append(tp)

with open("./output.bin", "wb") as fd:
    for p in packet_list:
        print(p)
        fd.write(p.SerializeToString())

