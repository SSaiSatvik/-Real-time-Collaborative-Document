# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doc.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'doc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdoc.proto\x1a\x1bgoogle/protobuf/empty.proto\"V\n\x08Transfer\x12\x16\n\x0etype_operation\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x10\n\x08position\x18\x03 \x01(\x05\x12\x12\n\nis_initial\x18\x04 \x01(\x08\"U\n\x08LogEntry\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0etype_operation\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x10\n\x08position\x18\x04 \x01(\x05\x32\x41\n\x15\x43ollaborativeDocument\x12(\n\x0c\x45\x64itDocument\x12\t.Transfer\x1a\t.Transfer(\x01\x30\x01\x32\x39\n\x06Logger\x12/\n\nLogChanges\x12\t.LogEntry\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRANSFER']._serialized_start=42
  _globals['_TRANSFER']._serialized_end=128
  _globals['_LOGENTRY']._serialized_start=130
  _globals['_LOGENTRY']._serialized_end=215
  _globals['_COLLABORATIVEDOCUMENT']._serialized_start=217
  _globals['_COLLABORATIVEDOCUMENT']._serialized_end=282
  _globals['_LOGGER']._serialized_start=284
  _globals['_LOGGER']._serialized_end=341
# @@protoc_insertion_point(module_scope)
