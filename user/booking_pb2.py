# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"\x18\n\x06UserID\x12\x0e\n\x06userid\x18\x01 \x01(\t\"B\n\x11\x41\x64\x64\x42ookingRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07movieid\x18\x03 \x01(\t\"$\n\x05\x44\x61tes\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x03(\t\"5\n\x0c\x42ooking_info\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x15\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x06.Dates\"1\n\x0f\x42ookingResponse\x12\x1e\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\r.Booking_info\"\x08\n\x06\x45mpty12\x9d\x01\n\x07\x42ooking\x12*\n\x0bGetBookings\x12\x07.UserID\x1a\x10.BookingResponse\"\x00\x12\x30\n\x0fGetListBookings\x12\x07.Empty1\x1a\x10.BookingResponse\"\x00\x30\x01\x12\x34\n\nAddBooking\x12\x12.AddBookingRequest\x1a\x10.BookingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USERID']._serialized_start=17
  _globals['_USERID']._serialized_end=41
  _globals['_ADDBOOKINGREQUEST']._serialized_start=43
  _globals['_ADDBOOKINGREQUEST']._serialized_end=109
  _globals['_DATES']._serialized_start=111
  _globals['_DATES']._serialized_end=147
  _globals['_BOOKING_INFO']._serialized_start=149
  _globals['_BOOKING_INFO']._serialized_end=202
  _globals['_BOOKINGRESPONSE']._serialized_start=204
  _globals['_BOOKINGRESPONSE']._serialized_end=253
  _globals['_EMPTY1']._serialized_start=255
  _globals['_EMPTY1']._serialized_end=263
  _globals['_BOOKING']._serialized_start=266
  _globals['_BOOKING']._serialized_end=423
# @@protoc_insertion_point(module_scope)