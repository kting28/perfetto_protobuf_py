import gen.perfetto_trace_pb2 as trace

# Generate a 64-bit uuid
# technically can collide since uuid is 128-bits
# not important in this example
def uuid64():
    import uuid
    return uuid.uuid4().int>>64

# Alias the slice constants 
TYPE_UNSPECIFIED = trace.TrackEvent.Type.TYPE_UNSPECIFIED
TYPE_SLICE_BEGIN = trace.TrackEvent.Type.TYPE_SLICE_BEGIN
TYPE_SLICE_END = trace.TrackEvent.Type.TYPE_SLICE_END
TYPE_INSTANT = trace.TrackEvent.Type.TYPE_INSTANT
TYPE_COUNTER = trace.TrackEvent.Type.TYPE_COUNTER

# Define process uuid
my_process_uuid = uuid64()

# Define thread uuid
my_thread_uuid = uuid64()
trusted_packet_sequence_id = uuid64()>>32


# This is the top container of all packets
top = trace.Trace()

# Emit this packet once *before* you emit the first event for this process.
tp = trace.TracePacket()
tp.track_descriptor.uuid = my_process_uuid
tp.track_descriptor.process.pid = 1234
tp.track_descriptor.process.process_name = "My process name"
top.packet.append(tp)


# Emit this packet once *before* you emit the first event for this thread.
tp = trace.TracePacket()
tp.track_descriptor.uuid = my_thread_uuid
tp.track_descriptor.parent_uuid = my_process_uuid
tp.track_descriptor.thread.pid = 1234
tp.track_descriptor.thread.tid = 5678
tp.track_descriptor.thread.thread_name = "My thread name"
top.packet.append(tp)


#--------------------------------------------------------------------------------
#                       Thread-scoped (sync) slices
#
# source: https://perfetto.dev/docs/reference/synthetic-track-event
# NOTE: in the legacy JSON tracing format, this section correspond to 
# B/E/I/X events with the associated M (metadata) events.

# Thread scoped slices are used to trace execution of functions on a single
# thread. As only one function runs on a single thread over time, this requires
# that child slices nest perfectly inside parent slices and do not partially
# overlap.
#--------------------------------------------------------------------------------
# The events for this thread start here
tp = trace.TracePacket()

# DebugAnnotation demonstration - thees can be used to add arbitrary payloads
# to the event
da1 = trace.DebugAnnotation()
da1.name = "foo"
da1.int_value = 42
da2 = trace.DebugAnnotation()
da2.name = "bar"
da2.int_value = 43

da3 = trace.DebugAnnotation()
da3.name ="args"  # Dict style args
da3.dict_entries.append(da1)
da3.dict_entries.append(da2)

# Call: Parent entrance 
tp.timestamp = 200
tp.track_event.type = TYPE_SLICE_BEGIN
tp.track_event.track_uuid = my_thread_uuid
tp.track_event.name = "My special parent"
tp.track_event.debug_annotations.append(da3)
tp.trusted_packet_sequence_id = trusted_packet_sequence_id
top.packet.append(tp)

# Call: Parent calls a function "special child"
tp = trace.TracePacket()
tp.timestamp = 250
tp.track_event.type = TYPE_SLICE_BEGIN
tp.track_event.track_uuid = my_thread_uuid
tp.track_event.name = "My special child"
tp.trusted_packet_sequence_id = trusted_packet_sequence_id
top.packet.append(tp)

# Call: Child calls a function "special child2"
tp = trace.TracePacket()
tp.timestamp = 255
tp.track_event.type = TYPE_SLICE_BEGIN
tp.track_event.track_uuid = my_thread_uuid
tp.track_event.name = "My special child2"
tp.trusted_packet_sequence_id = trusted_packet_sequence_id
top.packet.append(tp)

# Return
tp = trace.TracePacket()
tp.timestamp = 260
tp.track_event.type = TYPE_SLICE_END
tp.track_event.track_uuid = my_thread_uuid
tp.trusted_packet_sequence_id = trusted_packet_sequence_id
top.packet.append(tp)

# Return
tp = trace.TracePacket()
tp.timestamp = 290
tp.track_event.type = TYPE_SLICE_END
tp.track_event.track_uuid = my_thread_uuid
tp.trusted_packet_sequence_id = trusted_packet_sequence_id
top.packet.append(tp)

# Return
tp = trace.TracePacket()
tp.timestamp = 300
tp.track_event.type = TYPE_SLICE_END
tp.track_event.track_uuid = my_thread_uuid
tp.trusted_packet_sequence_id = trusted_packet_sequence_id
top.packet.append(tp)

# Events do not need to ordered in the packets
tp = trace.TracePacket()
tp.timestamp = 285
tp.track_event.type = TYPE_INSTANT
tp.track_event.name = "Instant event"
tp.track_event.track_uuid = my_thread_uuid
tp.trusted_packet_sequence_id = trusted_packet_sequence_id
top.packet.append(tp)


# Write the data out as binary
with open("./output.perfetto-trace", "wb") as fd:
    print(top)
    fd.write(top.SerializeToString())

