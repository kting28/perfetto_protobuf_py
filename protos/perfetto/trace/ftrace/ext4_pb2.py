# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/perfetto/trace/ftrace/ext4.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'protos/perfetto/trace/ftrace/ext4.proto\x12\x0fperfetto.protos\"`\n\x1b\x45xt4DaWriteBeginFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\"_\n\x19\x45xt4DaWriteEndFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0e\n\x06\x63opied\x18\x05 \x01(\r\"Z\n\x1c\x45xt4SyncFileEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06parent\x18\x03 \x01(\x04\x12\x10\n\x08\x64\x61tasync\x18\x04 \x01(\x05\"D\n\x1b\x45xt4SyncFileExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03ret\x18\x03 \x01(\x05\"b\n\x1c\x45xt4AllocDaBlocksFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x13\n\x0b\x64\x61ta_blocks\x18\x03 \x01(\r\x12\x13\n\x0bmeta_blocks\x18\x04 \x01(\r\"\xc1\x01\n\x1d\x45xt4AllocateBlocksFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05\x62lock\x18\x03 \x01(\x04\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0f\n\x07logical\x18\x05 \x01(\r\x12\r\n\x05lleft\x18\x06 \x01(\r\x12\x0e\n\x06lright\x18\x07 \x01(\r\x12\x0c\n\x04goal\x18\x08 \x01(\x04\x12\r\n\x05pleft\x18\t \x01(\x04\x12\x0e\n\x06pright\x18\n \x01(\x04\x12\r\n\x05\x66lags\x18\x0b \x01(\r\"S\n\x1c\x45xt4AllocateInodeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03\x64ir\x18\x03 \x01(\x04\x12\x0c\n\x04mode\x18\x04 \x01(\r\"Q\n#Ext4BeginOrderedTruncateFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x10\n\x08new_size\x18\x03 \x01(\x03\"U\n\x1c\x45xt4CollapseRangeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x03\"\xca\x01\n\x1d\x45xt4DaReleaseSpaceFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x10\n\x08i_blocks\x18\x03 \x01(\x04\x12\x14\n\x0c\x66reed_blocks\x18\x04 \x01(\x05\x12\x1c\n\x14reserved_data_blocks\x18\x05 \x01(\x05\x12\x1c\n\x14reserved_meta_blocks\x18\x06 \x01(\x05\x12\x1d\n\x15\x61llocated_meta_blocks\x18\x07 \x01(\x05\x12\x0c\n\x04mode\x18\x08 \x01(\r\"\xa8\x01\n\x1d\x45xt4DaReserveSpaceFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x10\n\x08i_blocks\x18\x03 \x01(\x04\x12\x1c\n\x14reserved_data_blocks\x18\x04 \x01(\x05\x12\x1c\n\x14reserved_meta_blocks\x18\x05 \x01(\x05\x12\x0c\n\x04mode\x18\x06 \x01(\r\x12\x11\n\tmd_needed\x18\x07 \x01(\x05\"\xe4\x01\n#Ext4DaUpdateReserveSpaceFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x10\n\x08i_blocks\x18\x03 \x01(\x04\x12\x13\n\x0bused_blocks\x18\x04 \x01(\x05\x12\x1c\n\x14reserved_data_blocks\x18\x05 \x01(\x05\x12\x1c\n\x14reserved_meta_blocks\x18\x06 \x01(\x05\x12\x1d\n\x15\x61llocated_meta_blocks\x18\x07 \x01(\x05\x12\x13\n\x0bquota_claim\x18\x08 \x01(\x05\x12\x0c\n\x04mode\x18\t \x01(\r\"\xcf\x01\n\x1b\x45xt4DaWritePagesFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x12\n\nfirst_page\x18\x03 \x01(\x04\x12\x13\n\x0bnr_to_write\x18\x04 \x01(\x03\x12\x11\n\tsync_mode\x18\x05 \x01(\x05\x12\x11\n\tb_blocknr\x18\x06 \x01(\x04\x12\x0e\n\x06\x62_size\x18\x07 \x01(\r\x12\x0f\n\x07\x62_state\x18\x08 \x01(\r\x12\x0f\n\x07io_done\x18\t \x01(\x05\x12\x15\n\rpages_written\x18\n \x01(\x05\"g\n!Ext4DaWritePagesExtentFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\x04\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\"^\n\x1c\x45xt4DirectIOEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x04\x12\n\n\x02rw\x18\x05 \x01(\x05\"j\n\x1b\x45xt4DirectIOExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x04\x12\n\n\x02rw\x18\x05 \x01(\x05\x12\x0b\n\x03ret\x18\x06 \x01(\x05\"G\n\x1c\x45xt4DiscardBlocksFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03\x62lk\x18\x02 \x01(\x04\x12\r\n\x05\x63ount\x18\x03 \x01(\x04\"]\n$Ext4DiscardPreallocationsFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03len\x18\x03 \x01(\r\x12\x0e\n\x06needed\x18\x04 \x01(\r\"B\n\x18\x45xt4DropInodeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04\x64rop\x18\x03 \x01(\x05\"q\n\x1c\x45xt4EsCacheExtentFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0c\n\x04pblk\x18\x05 \x01(\x04\x12\x0e\n\x06status\x18\x06 \x01(\r\"V\n,Ext4EsFindDelayedExtentRangeEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\"\x80\x01\n+Ext4EsFindDelayedExtentRangeExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0c\n\x04pblk\x18\x05 \x01(\x04\x12\x0e\n\x06status\x18\x06 \x01(\x04\"r\n\x1d\x45xt4EsInsertExtentFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0c\n\x04pblk\x18\x05 \x01(\x04\x12\x0e\n\x06status\x18\x06 \x01(\x04\"L\n\"Ext4EsLookupExtentEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\"\x85\x01\n!Ext4EsLookupExtentExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0c\n\x04pblk\x18\x05 \x01(\x04\x12\x0e\n\x06status\x18\x06 \x01(\x04\x12\r\n\x05\x66ound\x18\x07 \x01(\x05\"T\n\x1d\x45xt4EsRemoveExtentFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x03\"q\n\x17\x45xt4EsShrinkFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x11\n\tnr_shrunk\x18\x02 \x01(\x05\x12\x11\n\tscan_time\x18\x03 \x01(\x04\x12\x12\n\nnr_skipped\x18\x04 \x01(\x05\x12\x0f\n\x07retried\x18\x05 \x01(\x05\"R\n\x1c\x45xt4EsShrinkCountFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x12\n\nnr_to_scan\x18\x02 \x01(\x05\x12\x11\n\tcache_cnt\x18\x03 \x01(\x05\"V\n Ext4EsShrinkScanEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x12\n\nnr_to_scan\x18\x02 \x01(\x05\x12\x11\n\tcache_cnt\x18\x03 \x01(\x05\"T\n\x1f\x45xt4EsShrinkScanExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x11\n\tnr_shrunk\x18\x02 \x01(\x05\x12\x11\n\tcache_cnt\x18\x03 \x01(\x05\"D\n\x19\x45xt4EvictInodeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05nlink\x18\x03 \x01(\x05\"\x95\x01\n+Ext4ExtConvertToInitializedEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06m_lblk\x18\x03 \x01(\r\x12\r\n\x05m_len\x18\x04 \x01(\r\x12\x0e\n\x06u_lblk\x18\x05 \x01(\r\x12\r\n\x05u_len\x18\x06 \x01(\r\x12\x0e\n\x06u_pblk\x18\x07 \x01(\x04\"\xc7\x01\n.Ext4ExtConvertToInitializedFastpathFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06m_lblk\x18\x03 \x01(\r\x12\r\n\x05m_len\x18\x04 \x01(\r\x12\x0e\n\x06u_lblk\x18\x05 \x01(\r\x12\r\n\x05u_len\x18\x06 \x01(\r\x12\x0e\n\x06u_pblk\x18\x07 \x01(\x04\x12\x0e\n\x06i_lblk\x18\x08 \x01(\r\x12\r\n\x05i_len\x18\t \x01(\r\x12\x0e\n\x06i_pblk\x18\n \x01(\x04\"\x9f\x01\n(Ext4ExtHandleUnwrittenExtentsFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05\x66lags\x18\x03 \x01(\x05\x12\x0c\n\x04lblk\x18\x04 \x01(\r\x12\x0c\n\x04pblk\x18\x05 \x01(\x04\x12\x0b\n\x03len\x18\x06 \x01(\r\x12\x11\n\tallocated\x18\x07 \x01(\r\x12\x0e\n\x06newblk\x18\x08 \x01(\x04\"P\n\x19\x45xt4ExtInCacheFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03ret\x18\x04 \x01(\x05\"T\n\x1c\x45xt4ExtLoadExtentFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04pblk\x18\x03 \x01(\x04\x12\x0c\n\x04lblk\x18\x04 \x01(\r\"f\n Ext4ExtMapBlocksEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\"\x90\x01\n\x1f\x45xt4ExtMapBlocksExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05\x66lags\x18\x03 \x01(\r\x12\x0c\n\x04pblk\x18\x04 \x01(\x04\x12\x0c\n\x04lblk\x18\x05 \x01(\r\x12\x0b\n\x03len\x18\x06 \x01(\r\x12\x0e\n\x06mflags\x18\x07 \x01(\r\x12\x0b\n\x03ret\x18\x08 \x01(\x05\"b\n\x1c\x45xt4ExtPutInCacheFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\r\n\x05start\x18\x05 \x01(\x04\"d\n\x1d\x45xt4ExtRemoveSpaceFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05start\x18\x03 \x01(\r\x12\x0b\n\x03\x65nd\x18\x04 \x01(\r\x12\r\n\x05\x64\x65pth\x18\x05 \x01(\x05\"\xc1\x01\n!Ext4ExtRemoveSpaceDoneFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05start\x18\x03 \x01(\r\x12\x0b\n\x03\x65nd\x18\x04 \x01(\r\x12\r\n\x05\x64\x65pth\x18\x05 \x01(\x05\x12\x0f\n\x07partial\x18\x06 \x01(\x03\x12\x12\n\neh_entries\x18\x07 \x01(\r\x12\x0f\n\x07pc_lblk\x18\x08 \x01(\r\x12\x0f\n\x07pc_pclu\x18\t \x01(\x04\x12\x10\n\x08pc_state\x18\n \x01(\x05\"A\n\x17\x45xt4ExtRmIdxFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04pblk\x18\x03 \x01(\x04\"\xba\x01\n\x18\x45xt4ExtRmLeafFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0f\n\x07partial\x18\x03 \x01(\x03\x12\r\n\x05start\x18\x04 \x01(\r\x12\x0f\n\x07\x65\x65_lblk\x18\x05 \x01(\r\x12\x0f\n\x07\x65\x65_pblk\x18\x06 \x01(\x04\x12\x0e\n\x06\x65\x65_len\x18\x07 \x01(\x05\x12\x0f\n\x07pc_lblk\x18\x08 \x01(\r\x12\x0f\n\x07pc_pclu\x18\t \x01(\x04\x12\x10\n\x08pc_state\x18\n \x01(\x05\"a\n\x1c\x45xt4ExtShowExtentFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04pblk\x18\x03 \x01(\x04\x12\x0c\n\x04lblk\x18\x04 \x01(\r\x12\x0b\n\x03len\x18\x05 \x01(\r\"q\n\x1d\x45xt4FallocateEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x03\x12\x0c\n\x04mode\x18\x05 \x01(\x05\x12\x0b\n\x03pos\x18\x06 \x01(\x03\"b\n\x1c\x45xt4FallocateExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0e\n\x06\x62locks\x18\x04 \x01(\r\x12\x0b\n\x03ret\x18\x05 \x01(\x05\"\x89\x01\n Ext4FindDelallocRangeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04\x66rom\x18\x03 \x01(\r\x12\n\n\x02to\x18\x04 \x01(\r\x12\x0f\n\x07reverse\x18\x05 \x01(\x05\x12\r\n\x05\x66ound\x18\x06 \x01(\x05\x12\x11\n\tfound_blk\x18\x07 \x01(\r\"c\n\x15\x45xt4ForgetFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05\x62lock\x18\x03 \x01(\x04\x12\x13\n\x0bis_metadata\x18\x04 \x01(\x05\x12\x0c\n\x04mode\x18\x05 \x01(\r\"p\n\x19\x45xt4FreeBlocksFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05\x62lock\x18\x03 \x01(\x04\x12\r\n\x05\x63ount\x18\x04 \x01(\x04\x12\r\n\x05\x66lags\x18\x05 \x01(\x05\x12\x0c\n\x04mode\x18\x06 \x01(\r\"l\n\x18\x45xt4FreeInodeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03uid\x18\x03 \x01(\r\x12\x0b\n\x03gid\x18\x04 \x01(\r\x12\x0e\n\x06\x62locks\x18\x05 \x01(\x04\x12\x0c\n\x04mode\x18\x06 \x01(\r\"}\n)Ext4GetImpliedClusterAllocExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\r\n\x05\x66lags\x18\x02 \x01(\r\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0c\n\x04pblk\x18\x04 \x01(\x04\x12\x0b\n\x03len\x18\x05 \x01(\r\x12\x0b\n\x03ret\x18\x06 \x01(\x05\"]\n&Ext4GetReservedClusterAllocFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\"f\n Ext4IndMapBlocksEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04lblk\x18\x03 \x01(\r\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\"\x90\x01\n\x1f\x45xt4IndMapBlocksExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05\x66lags\x18\x03 \x01(\r\x12\x0c\n\x04pblk\x18\x04 \x01(\x04\x12\x0c\n\x04lblk\x18\x05 \x01(\r\x12\x0b\n\x03len\x18\x06 \x01(\r\x12\x0e\n\x06mflags\x18\x07 \x01(\r\x12\x0b\n\x03ret\x18\x08 \x01(\x05\"S\n\x1a\x45xt4InsertRangeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x03\"h\n\x1d\x45xt4InvalidatepageFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\x12\x0e\n\x06offset\x18\x04 \x01(\x04\x12\x0e\n\x06length\x18\x05 \x01(\r\"\x81\x01\n\x1b\x45xt4JournalStartFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\n\n\x02ip\x18\x02 \x01(\x04\x12\x0e\n\x06\x62locks\x18\x03 \x01(\x05\x12\x12\n\nrsv_blocks\x18\x04 \x01(\x05\x12\x0f\n\x07nblocks\x18\x05 \x01(\x05\x12\x14\n\x0crevoke_creds\x18\x06 \x01(\x05\"N\n#Ext4JournalStartReservedFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\n\n\x02ip\x18\x02 \x01(\x04\x12\x0e\n\x06\x62locks\x18\x03 \x01(\x05\"r\n\'Ext4JournalledInvalidatepageFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\x12\x0e\n\x06offset\x18\x04 \x01(\x04\x12\x0e\n\x06length\x18\x05 \x01(\r\"g\n!Ext4JournalledWriteEndFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0e\n\x06\x63opied\x18\x05 \x01(\r\"4\n\x18\x45xt4LoadInodeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\"<\n\x1e\x45xt4LoadInodeBitmapFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\r\n\x05group\x18\x02 \x01(\r\"E\n\x1d\x45xt4MarkInodeDirtyFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\n\n\x02ip\x18\x03 \x01(\x04\"9\n\x1b\x45xt4MbBitmapLoadFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\r\n\x05group\x18\x02 \x01(\r\">\n Ext4MbBuddyBitmapLoadFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\r\n\x05group\x18\x02 \x01(\r\"E\n&Ext4MbDiscardPreallocationsFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0e\n\x06needed\x18\x02 \x01(\x05\"m\n\x1b\x45xt4MbNewGroupPaFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x11\n\tpa_pstart\x18\x03 \x01(\x04\x12\x11\n\tpa_lstart\x18\x04 \x01(\x04\x12\x0e\n\x06pa_len\x18\x05 \x01(\r\"m\n\x1b\x45xt4MbNewInodePaFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x11\n\tpa_pstart\x18\x03 \x01(\x04\x12\x11\n\tpa_lstart\x18\x04 \x01(\x04\x12\x0e\n\x06pa_len\x18\x05 \x01(\r\"Q\n\x1f\x45xt4MbReleaseGroupPaFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x11\n\tpa_pstart\x18\x02 \x01(\x04\x12\x0e\n\x06pa_len\x18\x03 \x01(\r\"Y\n\x1f\x45xt4MbReleaseInodePaFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05\x62lock\x18\x03 \x01(\x04\x12\r\n\x05\x63ount\x18\x04 \x01(\r\"\x86\x03\n\x1b\x45xt4MballocAllocFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x14\n\x0corig_logical\x18\x03 \x01(\r\x12\x12\n\norig_start\x18\x04 \x01(\x05\x12\x12\n\norig_group\x18\x05 \x01(\r\x12\x10\n\x08orig_len\x18\x06 \x01(\x05\x12\x14\n\x0cgoal_logical\x18\x07 \x01(\r\x12\x12\n\ngoal_start\x18\x08 \x01(\x05\x12\x12\n\ngoal_group\x18\t \x01(\r\x12\x10\n\x08goal_len\x18\n \x01(\x05\x12\x16\n\x0eresult_logical\x18\x0b \x01(\r\x12\x14\n\x0cresult_start\x18\x0c \x01(\x05\x12\x14\n\x0cresult_group\x18\r \x01(\r\x12\x12\n\nresult_len\x18\x0e \x01(\x05\x12\r\n\x05\x66ound\x18\x0f \x01(\r\x12\x0e\n\x06groups\x18\x10 \x01(\r\x12\r\n\x05\x62uddy\x18\x11 \x01(\r\x12\r\n\x05\x66lags\x18\x12 \x01(\r\x12\x0c\n\x04tail\x18\x13 \x01(\r\x12\n\n\x02\x63r\x18\x14 \x01(\r\"y\n\x1d\x45xt4MballocDiscardFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x14\n\x0cresult_start\x18\x03 \x01(\x05\x12\x14\n\x0cresult_group\x18\x04 \x01(\r\x12\x12\n\nresult_len\x18\x05 \x01(\x05\"v\n\x1a\x45xt4MballocFreeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x14\n\x0cresult_start\x18\x03 \x01(\x05\x12\x14\n\x0cresult_group\x18\x04 \x01(\r\x12\x12\n\nresult_len\x18\x05 \x01(\x05\"\xe2\x01\n\x1e\x45xt4MballocPreallocFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x14\n\x0corig_logical\x18\x03 \x01(\r\x12\x12\n\norig_start\x18\x04 \x01(\x05\x12\x12\n\norig_group\x18\x05 \x01(\r\x12\x10\n\x08orig_len\x18\x06 \x01(\x05\x12\x16\n\x0eresult_logical\x18\x07 \x01(\r\x12\x14\n\x0cresult_start\x18\x08 \x01(\x05\x12\x14\n\x0cresult_group\x18\t \x01(\r\x12\x12\n\nresult_len\x18\n \x01(\x05\"y\n#Ext4OtherInodeUpdateTimeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x10\n\x08orig_ino\x18\x03 \x01(\x04\x12\x0b\n\x03uid\x18\x04 \x01(\r\x12\x0b\n\x03gid\x18\x05 \x01(\r\x12\x0c\n\x04mode\x18\x06 \x01(\r\"_\n\x18\x45xt4PunchHoleFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x03\x12\x0c\n\x04mode\x18\x05 \x01(\x05\"R\n\"Ext4ReadBlockBitmapLoadFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\r\n\x05group\x18\x02 \x01(\r\x12\x10\n\x08prefetch\x18\x03 \x01(\r\"B\n\x17\x45xt4ReadpageFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\"E\n\x1a\x45xt4ReleasepageFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\"\xc8\x01\n\x1b\x45xt4RemoveBlocksFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0c\n\x04\x66rom\x18\x03 \x01(\r\x12\n\n\x02to\x18\x04 \x01(\r\x12\x0f\n\x07partial\x18\x05 \x01(\x03\x12\x0f\n\x07\x65\x65_pblk\x18\x06 \x01(\x04\x12\x0f\n\x07\x65\x65_lblk\x18\x07 \x01(\r\x12\x0e\n\x06\x65\x65_len\x18\x08 \x01(\r\x12\x0f\n\x07pc_lblk\x18\t \x01(\r\x12\x0f\n\x07pc_pclu\x18\n \x01(\x04\x12\x10\n\x08pc_state\x18\x0b \x01(\x05\"\xb1\x01\n\x1c\x45xt4RequestBlocksFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03len\x18\x03 \x01(\r\x12\x0f\n\x07logical\x18\x04 \x01(\r\x12\r\n\x05lleft\x18\x05 \x01(\r\x12\x0e\n\x06lright\x18\x06 \x01(\r\x12\x0c\n\x04goal\x18\x07 \x01(\x04\x12\r\n\x05pleft\x18\x08 \x01(\x04\x12\x0e\n\x06pright\x18\t \x01(\x04\x12\r\n\x05\x66lags\x18\n \x01(\r\"E\n\x1b\x45xt4RequestInodeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03\x64ir\x18\x02 \x01(\x04\x12\x0c\n\x04mode\x18\x03 \x01(\r\"2\n\x15\x45xt4SyncFsFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0c\n\x04wait\x18\x02 \x01(\x05\"m\n\x1a\x45xt4TrimAllFreeFtraceEvent\x12\x11\n\tdev_major\x18\x01 \x01(\x05\x12\x11\n\tdev_minor\x18\x02 \x01(\x05\x12\r\n\x05group\x18\x03 \x01(\r\x12\r\n\x05start\x18\x04 \x01(\x05\x12\x0b\n\x03len\x18\x05 \x01(\x05\"l\n\x19\x45xt4TrimExtentFtraceEvent\x12\x11\n\tdev_major\x18\x01 \x01(\x05\x12\x11\n\tdev_minor\x18\x02 \x01(\x05\x12\r\n\x05group\x18\x03 \x01(\r\x12\r\n\x05start\x18\x04 \x01(\x05\x12\x0b\n\x03len\x18\x05 \x01(\x05\"H\n\x1c\x45xt4TruncateEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06\x62locks\x18\x03 \x01(\x04\"G\n\x1b\x45xt4TruncateExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06\x62locks\x18\x03 \x01(\x04\"T\n\x1a\x45xt4UnlinkEnterFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06parent\x18\x03 \x01(\x04\x12\x0c\n\x04size\x18\x04 \x01(\x03\"B\n\x19\x45xt4UnlinkExitFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03ret\x18\x03 \x01(\x05\"^\n\x19\x45xt4WriteBeginFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\r\n\x05\x66lags\x18\x05 \x01(\r\"]\n\x17\x45xt4WriteEndFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03pos\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\r\x12\x0e\n\x06\x63opied\x18\x05 \x01(\r\"C\n\x18\x45xt4WritepageFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\"\xe0\x01\n\x19\x45xt4WritepagesFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x13\n\x0bnr_to_write\x18\x03 \x01(\x03\x12\x15\n\rpages_skipped\x18\x04 \x01(\x03\x12\x13\n\x0brange_start\x18\x05 \x01(\x03\x12\x11\n\trange_end\x18\x06 \x01(\x03\x12\x17\n\x0fwriteback_index\x18\x07 \x01(\x04\x12\x11\n\tsync_mode\x18\x08 \x01(\x05\x12\x13\n\x0b\x66or_kupdate\x18\t \x01(\r\x12\x14\n\x0crange_cyclic\x18\n \x01(\r\"\xa2\x01\n\x1f\x45xt4WritepagesResultFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0b\n\x03ret\x18\x03 \x01(\x05\x12\x15\n\rpages_written\x18\x04 \x01(\x05\x12\x15\n\rpages_skipped\x18\x05 \x01(\x03\x12\x17\n\x0fwriteback_index\x18\x06 \x01(\x04\x12\x11\n\tsync_mode\x18\x07 \x01(\x05\"_\n\x18\x45xt4ZeroRangeFtraceEvent\x12\x0b\n\x03\x64\x65v\x18\x01 \x01(\x04\x12\x0b\n\x03ino\x18\x02 \x01(\x04\x12\x0e\n\x06offset\x18\x03 \x01(\x03\x12\x0b\n\x03len\x18\x04 \x01(\x03\x12\x0c\n\x04mode\x18\x05 \x01(\x05')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.perfetto.trace.ftrace.ext4_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXT4DAWRITEBEGINFTRACEEVENT._serialized_start=60
  _EXT4DAWRITEBEGINFTRACEEVENT._serialized_end=156
  _EXT4DAWRITEENDFTRACEEVENT._serialized_start=158
  _EXT4DAWRITEENDFTRACEEVENT._serialized_end=253
  _EXT4SYNCFILEENTERFTRACEEVENT._serialized_start=255
  _EXT4SYNCFILEENTERFTRACEEVENT._serialized_end=345
  _EXT4SYNCFILEEXITFTRACEEVENT._serialized_start=347
  _EXT4SYNCFILEEXITFTRACEEVENT._serialized_end=415
  _EXT4ALLOCDABLOCKSFTRACEEVENT._serialized_start=417
  _EXT4ALLOCDABLOCKSFTRACEEVENT._serialized_end=515
  _EXT4ALLOCATEBLOCKSFTRACEEVENT._serialized_start=518
  _EXT4ALLOCATEBLOCKSFTRACEEVENT._serialized_end=711
  _EXT4ALLOCATEINODEFTRACEEVENT._serialized_start=713
  _EXT4ALLOCATEINODEFTRACEEVENT._serialized_end=796
  _EXT4BEGINORDEREDTRUNCATEFTRACEEVENT._serialized_start=798
  _EXT4BEGINORDEREDTRUNCATEFTRACEEVENT._serialized_end=879
  _EXT4COLLAPSERANGEFTRACEEVENT._serialized_start=881
  _EXT4COLLAPSERANGEFTRACEEVENT._serialized_end=966
  _EXT4DARELEASESPACEFTRACEEVENT._serialized_start=969
  _EXT4DARELEASESPACEFTRACEEVENT._serialized_end=1171
  _EXT4DARESERVESPACEFTRACEEVENT._serialized_start=1174
  _EXT4DARESERVESPACEFTRACEEVENT._serialized_end=1342
  _EXT4DAUPDATERESERVESPACEFTRACEEVENT._serialized_start=1345
  _EXT4DAUPDATERESERVESPACEFTRACEEVENT._serialized_end=1573
  _EXT4DAWRITEPAGESFTRACEEVENT._serialized_start=1576
  _EXT4DAWRITEPAGESFTRACEEVENT._serialized_end=1783
  _EXT4DAWRITEPAGESEXTENTFTRACEEVENT._serialized_start=1785
  _EXT4DAWRITEPAGESEXTENTFTRACEEVENT._serialized_end=1888
  _EXT4DIRECTIOENTERFTRACEEVENT._serialized_start=1890
  _EXT4DIRECTIOENTERFTRACEEVENT._serialized_end=1984
  _EXT4DIRECTIOEXITFTRACEEVENT._serialized_start=1986
  _EXT4DIRECTIOEXITFTRACEEVENT._serialized_end=2092
  _EXT4DISCARDBLOCKSFTRACEEVENT._serialized_start=2094
  _EXT4DISCARDBLOCKSFTRACEEVENT._serialized_end=2165
  _EXT4DISCARDPREALLOCATIONSFTRACEEVENT._serialized_start=2167
  _EXT4DISCARDPREALLOCATIONSFTRACEEVENT._serialized_end=2260
  _EXT4DROPINODEFTRACEEVENT._serialized_start=2262
  _EXT4DROPINODEFTRACEEVENT._serialized_end=2328
  _EXT4ESCACHEEXTENTFTRACEEVENT._serialized_start=2330
  _EXT4ESCACHEEXTENTFTRACEEVENT._serialized_end=2443
  _EXT4ESFINDDELAYEDEXTENTRANGEENTERFTRACEEVENT._serialized_start=2445
  _EXT4ESFINDDELAYEDEXTENTRANGEENTERFTRACEEVENT._serialized_end=2531
  _EXT4ESFINDDELAYEDEXTENTRANGEEXITFTRACEEVENT._serialized_start=2534
  _EXT4ESFINDDELAYEDEXTENTRANGEEXITFTRACEEVENT._serialized_end=2662
  _EXT4ESINSERTEXTENTFTRACEEVENT._serialized_start=2664
  _EXT4ESINSERTEXTENTFTRACEEVENT._serialized_end=2778
  _EXT4ESLOOKUPEXTENTENTERFTRACEEVENT._serialized_start=2780
  _EXT4ESLOOKUPEXTENTENTERFTRACEEVENT._serialized_end=2856
  _EXT4ESLOOKUPEXTENTEXITFTRACEEVENT._serialized_start=2859
  _EXT4ESLOOKUPEXTENTEXITFTRACEEVENT._serialized_end=2992
  _EXT4ESREMOVEEXTENTFTRACEEVENT._serialized_start=2994
  _EXT4ESREMOVEEXTENTFTRACEEVENT._serialized_end=3078
  _EXT4ESSHRINKFTRACEEVENT._serialized_start=3080
  _EXT4ESSHRINKFTRACEEVENT._serialized_end=3193
  _EXT4ESSHRINKCOUNTFTRACEEVENT._serialized_start=3195
  _EXT4ESSHRINKCOUNTFTRACEEVENT._serialized_end=3277
  _EXT4ESSHRINKSCANENTERFTRACEEVENT._serialized_start=3279
  _EXT4ESSHRINKSCANENTERFTRACEEVENT._serialized_end=3365
  _EXT4ESSHRINKSCANEXITFTRACEEVENT._serialized_start=3367
  _EXT4ESSHRINKSCANEXITFTRACEEVENT._serialized_end=3451
  _EXT4EVICTINODEFTRACEEVENT._serialized_start=3453
  _EXT4EVICTINODEFTRACEEVENT._serialized_end=3521
  _EXT4EXTCONVERTTOINITIALIZEDENTERFTRACEEVENT._serialized_start=3524
  _EXT4EXTCONVERTTOINITIALIZEDENTERFTRACEEVENT._serialized_end=3673
  _EXT4EXTCONVERTTOINITIALIZEDFASTPATHFTRACEEVENT._serialized_start=3676
  _EXT4EXTCONVERTTOINITIALIZEDFASTPATHFTRACEEVENT._serialized_end=3875
  _EXT4EXTHANDLEUNWRITTENEXTENTSFTRACEEVENT._serialized_start=3878
  _EXT4EXTHANDLEUNWRITTENEXTENTSFTRACEEVENT._serialized_end=4037
  _EXT4EXTINCACHEFTRACEEVENT._serialized_start=4039
  _EXT4EXTINCACHEFTRACEEVENT._serialized_end=4119
  _EXT4EXTLOADEXTENTFTRACEEVENT._serialized_start=4121
  _EXT4EXTLOADEXTENTFTRACEEVENT._serialized_end=4205
  _EXT4EXTMAPBLOCKSENTERFTRACEEVENT._serialized_start=4207
  _EXT4EXTMAPBLOCKSENTERFTRACEEVENT._serialized_end=4309
  _EXT4EXTMAPBLOCKSEXITFTRACEEVENT._serialized_start=4312
  _EXT4EXTMAPBLOCKSEXITFTRACEEVENT._serialized_end=4456
  _EXT4EXTPUTINCACHEFTRACEEVENT._serialized_start=4458
  _EXT4EXTPUTINCACHEFTRACEEVENT._serialized_end=4556
  _EXT4EXTREMOVESPACEFTRACEEVENT._serialized_start=4558
  _EXT4EXTREMOVESPACEFTRACEEVENT._serialized_end=4658
  _EXT4EXTREMOVESPACEDONEFTRACEEVENT._serialized_start=4661
  _EXT4EXTREMOVESPACEDONEFTRACEEVENT._serialized_end=4854
  _EXT4EXTRMIDXFTRACEEVENT._serialized_start=4856
  _EXT4EXTRMIDXFTRACEEVENT._serialized_end=4921
  _EXT4EXTRMLEAFFTRACEEVENT._serialized_start=4924
  _EXT4EXTRMLEAFFTRACEEVENT._serialized_end=5110
  _EXT4EXTSHOWEXTENTFTRACEEVENT._serialized_start=5112
  _EXT4EXTSHOWEXTENTFTRACEEVENT._serialized_end=5209
  _EXT4FALLOCATEENTERFTRACEEVENT._serialized_start=5211
  _EXT4FALLOCATEENTERFTRACEEVENT._serialized_end=5324
  _EXT4FALLOCATEEXITFTRACEEVENT._serialized_start=5326
  _EXT4FALLOCATEEXITFTRACEEVENT._serialized_end=5424
  _EXT4FINDDELALLOCRANGEFTRACEEVENT._serialized_start=5427
  _EXT4FINDDELALLOCRANGEFTRACEEVENT._serialized_end=5564
  _EXT4FORGETFTRACEEVENT._serialized_start=5566
  _EXT4FORGETFTRACEEVENT._serialized_end=5665
  _EXT4FREEBLOCKSFTRACEEVENT._serialized_start=5667
  _EXT4FREEBLOCKSFTRACEEVENT._serialized_end=5779
  _EXT4FREEINODEFTRACEEVENT._serialized_start=5781
  _EXT4FREEINODEFTRACEEVENT._serialized_end=5889
  _EXT4GETIMPLIEDCLUSTERALLOCEXITFTRACEEVENT._serialized_start=5891
  _EXT4GETIMPLIEDCLUSTERALLOCEXITFTRACEEVENT._serialized_end=6016
  _EXT4GETRESERVEDCLUSTERALLOCFTRACEEVENT._serialized_start=6018
  _EXT4GETRESERVEDCLUSTERALLOCFTRACEEVENT._serialized_end=6111
  _EXT4INDMAPBLOCKSENTERFTRACEEVENT._serialized_start=6113
  _EXT4INDMAPBLOCKSENTERFTRACEEVENT._serialized_end=6215
  _EXT4INDMAPBLOCKSEXITFTRACEEVENT._serialized_start=6218
  _EXT4INDMAPBLOCKSEXITFTRACEEVENT._serialized_end=6362
  _EXT4INSERTRANGEFTRACEEVENT._serialized_start=6364
  _EXT4INSERTRANGEFTRACEEVENT._serialized_end=6447
  _EXT4INVALIDATEPAGEFTRACEEVENT._serialized_start=6449
  _EXT4INVALIDATEPAGEFTRACEEVENT._serialized_end=6553
  _EXT4JOURNALSTARTFTRACEEVENT._serialized_start=6556
  _EXT4JOURNALSTARTFTRACEEVENT._serialized_end=6685
  _EXT4JOURNALSTARTRESERVEDFTRACEEVENT._serialized_start=6687
  _EXT4JOURNALSTARTRESERVEDFTRACEEVENT._serialized_end=6765
  _EXT4JOURNALLEDINVALIDATEPAGEFTRACEEVENT._serialized_start=6767
  _EXT4JOURNALLEDINVALIDATEPAGEFTRACEEVENT._serialized_end=6881
  _EXT4JOURNALLEDWRITEENDFTRACEEVENT._serialized_start=6883
  _EXT4JOURNALLEDWRITEENDFTRACEEVENT._serialized_end=6986
  _EXT4LOADINODEFTRACEEVENT._serialized_start=6988
  _EXT4LOADINODEFTRACEEVENT._serialized_end=7040
  _EXT4LOADINODEBITMAPFTRACEEVENT._serialized_start=7042
  _EXT4LOADINODEBITMAPFTRACEEVENT._serialized_end=7102
  _EXT4MARKINODEDIRTYFTRACEEVENT._serialized_start=7104
  _EXT4MARKINODEDIRTYFTRACEEVENT._serialized_end=7173
  _EXT4MBBITMAPLOADFTRACEEVENT._serialized_start=7175
  _EXT4MBBITMAPLOADFTRACEEVENT._serialized_end=7232
  _EXT4MBBUDDYBITMAPLOADFTRACEEVENT._serialized_start=7234
  _EXT4MBBUDDYBITMAPLOADFTRACEEVENT._serialized_end=7296
  _EXT4MBDISCARDPREALLOCATIONSFTRACEEVENT._serialized_start=7298
  _EXT4MBDISCARDPREALLOCATIONSFTRACEEVENT._serialized_end=7367
  _EXT4MBNEWGROUPPAFTRACEEVENT._serialized_start=7369
  _EXT4MBNEWGROUPPAFTRACEEVENT._serialized_end=7478
  _EXT4MBNEWINODEPAFTRACEEVENT._serialized_start=7480
  _EXT4MBNEWINODEPAFTRACEEVENT._serialized_end=7589
  _EXT4MBRELEASEGROUPPAFTRACEEVENT._serialized_start=7591
  _EXT4MBRELEASEGROUPPAFTRACEEVENT._serialized_end=7672
  _EXT4MBRELEASEINODEPAFTRACEEVENT._serialized_start=7674
  _EXT4MBRELEASEINODEPAFTRACEEVENT._serialized_end=7763
  _EXT4MBALLOCALLOCFTRACEEVENT._serialized_start=7766
  _EXT4MBALLOCALLOCFTRACEEVENT._serialized_end=8156
  _EXT4MBALLOCDISCARDFTRACEEVENT._serialized_start=8158
  _EXT4MBALLOCDISCARDFTRACEEVENT._serialized_end=8279
  _EXT4MBALLOCFREEFTRACEEVENT._serialized_start=8281
  _EXT4MBALLOCFREEFTRACEEVENT._serialized_end=8399
  _EXT4MBALLOCPREALLOCFTRACEEVENT._serialized_start=8402
  _EXT4MBALLOCPREALLOCFTRACEEVENT._serialized_end=8628
  _EXT4OTHERINODEUPDATETIMEFTRACEEVENT._serialized_start=8630
  _EXT4OTHERINODEUPDATETIMEFTRACEEVENT._serialized_end=8751
  _EXT4PUNCHHOLEFTRACEEVENT._serialized_start=8753
  _EXT4PUNCHHOLEFTRACEEVENT._serialized_end=8848
  _EXT4READBLOCKBITMAPLOADFTRACEEVENT._serialized_start=8850
  _EXT4READBLOCKBITMAPLOADFTRACEEVENT._serialized_end=8932
  _EXT4READPAGEFTRACEEVENT._serialized_start=8934
  _EXT4READPAGEFTRACEEVENT._serialized_end=9000
  _EXT4RELEASEPAGEFTRACEEVENT._serialized_start=9002
  _EXT4RELEASEPAGEFTRACEEVENT._serialized_end=9071
  _EXT4REMOVEBLOCKSFTRACEEVENT._serialized_start=9074
  _EXT4REMOVEBLOCKSFTRACEEVENT._serialized_end=9274
  _EXT4REQUESTBLOCKSFTRACEEVENT._serialized_start=9277
  _EXT4REQUESTBLOCKSFTRACEEVENT._serialized_end=9454
  _EXT4REQUESTINODEFTRACEEVENT._serialized_start=9456
  _EXT4REQUESTINODEFTRACEEVENT._serialized_end=9525
  _EXT4SYNCFSFTRACEEVENT._serialized_start=9527
  _EXT4SYNCFSFTRACEEVENT._serialized_end=9577
  _EXT4TRIMALLFREEFTRACEEVENT._serialized_start=9579
  _EXT4TRIMALLFREEFTRACEEVENT._serialized_end=9688
  _EXT4TRIMEXTENTFTRACEEVENT._serialized_start=9690
  _EXT4TRIMEXTENTFTRACEEVENT._serialized_end=9798
  _EXT4TRUNCATEENTERFTRACEEVENT._serialized_start=9800
  _EXT4TRUNCATEENTERFTRACEEVENT._serialized_end=9872
  _EXT4TRUNCATEEXITFTRACEEVENT._serialized_start=9874
  _EXT4TRUNCATEEXITFTRACEEVENT._serialized_end=9945
  _EXT4UNLINKENTERFTRACEEVENT._serialized_start=9947
  _EXT4UNLINKENTERFTRACEEVENT._serialized_end=10031
  _EXT4UNLINKEXITFTRACEEVENT._serialized_start=10033
  _EXT4UNLINKEXITFTRACEEVENT._serialized_end=10099
  _EXT4WRITEBEGINFTRACEEVENT._serialized_start=10101
  _EXT4WRITEBEGINFTRACEEVENT._serialized_end=10195
  _EXT4WRITEENDFTRACEEVENT._serialized_start=10197
  _EXT4WRITEENDFTRACEEVENT._serialized_end=10290
  _EXT4WRITEPAGEFTRACEEVENT._serialized_start=10292
  _EXT4WRITEPAGEFTRACEEVENT._serialized_end=10359
  _EXT4WRITEPAGESFTRACEEVENT._serialized_start=10362
  _EXT4WRITEPAGESFTRACEEVENT._serialized_end=10586
  _EXT4WRITEPAGESRESULTFTRACEEVENT._serialized_start=10589
  _EXT4WRITEPAGESRESULTFTRACEEVENT._serialized_end=10751
  _EXT4ZERORANGEFTRACEEVENT._serialized_start=10753
  _EXT4ZERORANGEFTRACEEVENT._serialized_end=10848
# @@protoc_insertion_point(module_scope)
