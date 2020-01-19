// Generated by gencpp from file freefloating_gazebo/ControlType.msg
// DO NOT EDIT!


#ifndef FREEFLOATING_GAZEBO_MESSAGE_CONTROLTYPE_H
#define FREEFLOATING_GAZEBO_MESSAGE_CONTROLTYPE_H

#include <ros/service_traits.h>


#include <freefloating_gazebo/ControlTypeRequest.h>
#include <freefloating_gazebo/ControlTypeResponse.h>


namespace freefloating_gazebo
{

struct ControlType
{

typedef ControlTypeRequest Request;
typedef ControlTypeResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ControlType
} // namespace freefloating_gazebo


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::freefloating_gazebo::ControlType > {
  static const char* value()
  {
    return "52951d9d51995d256d1f3d1a265444f8";
  }

  static const char* value(const ::freefloating_gazebo::ControlType&) { return value(); }
};

template<>
struct DataType< ::freefloating_gazebo::ControlType > {
  static const char* value()
  {
    return "freefloating_gazebo/ControlType";
  }

  static const char* value(const ::freefloating_gazebo::ControlType&) { return value(); }
};


// service_traits::MD5Sum< ::freefloating_gazebo::ControlTypeRequest> should match 
// service_traits::MD5Sum< ::freefloating_gazebo::ControlType > 
template<>
struct MD5Sum< ::freefloating_gazebo::ControlTypeRequest>
{
  static const char* value()
  {
    return MD5Sum< ::freefloating_gazebo::ControlType >::value();
  }
  static const char* value(const ::freefloating_gazebo::ControlTypeRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::freefloating_gazebo::ControlTypeRequest> should match 
// service_traits::DataType< ::freefloating_gazebo::ControlType > 
template<>
struct DataType< ::freefloating_gazebo::ControlTypeRequest>
{
  static const char* value()
  {
    return DataType< ::freefloating_gazebo::ControlType >::value();
  }
  static const char* value(const ::freefloating_gazebo::ControlTypeRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::freefloating_gazebo::ControlTypeResponse> should match 
// service_traits::MD5Sum< ::freefloating_gazebo::ControlType > 
template<>
struct MD5Sum< ::freefloating_gazebo::ControlTypeResponse>
{
  static const char* value()
  {
    return MD5Sum< ::freefloating_gazebo::ControlType >::value();
  }
  static const char* value(const ::freefloating_gazebo::ControlTypeResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::freefloating_gazebo::ControlTypeResponse> should match 
// service_traits::DataType< ::freefloating_gazebo::ControlType > 
template<>
struct DataType< ::freefloating_gazebo::ControlTypeResponse>
{
  static const char* value()
  {
    return DataType< ::freefloating_gazebo::ControlType >::value();
  }
  static const char* value(const ::freefloating_gazebo::ControlTypeResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // FREEFLOATING_GAZEBO_MESSAGE_CONTROLTYPE_H