# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: order_service.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'order_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13order_service.proto\"M\n\x0cOrderRequest\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x1a\n\x08toppings\x18\x02 \x03(\x0e\x32\x08.Topping\x12\x13\n\x0b\x63ustomer_id\x18\x03 \x01(\t\"1\n\rOrderResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08order_id\x18\x02 \x01(\t\"!\n\rStatusRequest\x12\x10\n\x08order_id\x18\x01 \x01(\t\".\n\x0eStatusResponse\x12\x1c\n\x06status\x18\x01 \x01(\x0e\x32\x0c.OrderStatus*O\n\x07Topping\x12\x17\n\x13TOPPING_UNSPECIFIED\x10\x00\x12\x15\n\x11TOPPING_PEPPORONI\x10\x01\x12\x14\n\x10TOPPING_JALAPENO\x10\x02*\x96\x01\n\x0bOrderStatus\x12\x1b\n\x17OrderStatus_UNSPECIFIED\x10\x00\x12\x18\n\x14OrderStatus_RECEIVED\x10\x01\x12\x1a\n\x16OrderStatus_INPROGRESS\x10\x02\x12\x19\n\x15OrderStatus_COMPLETED\x10\x03\x12\x19\n\x15OrderStatus_CANCELLED\x10\x04\x32s\n\x0cOrderService\x12+\n\nPlaceOrder\x12\r.OrderRequest\x1a\x0e.OrderResponse\x12\x36\n\x11StreamOrderStatus\x12\x0e.StatusRequest\x1a\x0f.StatusResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TOPPING']._serialized_start=236
  _globals['_TOPPING']._serialized_end=315
  _globals['_ORDERSTATUS']._serialized_start=318
  _globals['_ORDERSTATUS']._serialized_end=468
  _globals['_ORDERREQUEST']._serialized_start=23
  _globals['_ORDERREQUEST']._serialized_end=100
  _globals['_ORDERRESPONSE']._serialized_start=102
  _globals['_ORDERRESPONSE']._serialized_end=151
  _globals['_STATUSREQUEST']._serialized_start=153
  _globals['_STATUSREQUEST']._serialized_end=186
  _globals['_STATUSRESPONSE']._serialized_start=188
  _globals['_STATUSRESPONSE']._serialized_end=234
  _globals['_ORDERSERVICE']._serialized_start=470
  _globals['_ORDERSERVICE']._serialized_end=585
# @@protoc_insertion_point(module_scope)
