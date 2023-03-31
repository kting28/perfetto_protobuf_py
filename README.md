# Demonstration of Perfetto synthetic track event generation with python
The perfetto `.proto` definition was copied from the `perfetto.dev` repo.
See the [synthetic track event guide](https://perfetto.dev/docs/reference/synthetic-track-event) for some documentation on creating these events. The output binary file can be opened from the perfetto UI. The `traceconv` tool is copied here for examining the generated binary.

# Prerequisite
```
pip3 install protobuf
```

# Run
```
python3 ./test.py
# check the generated binary:
./traceconv text output.perfetto-trace
```

# Compiling proto definition
The `protoc` compiler can be found [here](https://github.com/protocolbuffers/protobuf/releases)

```
protoc perfetto_trace.proto --python_output=gen
```