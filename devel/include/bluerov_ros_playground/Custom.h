// Generated by gencpp from file bluerov_ros_playground/Custom.msg
// DO NOT EDIT!


#ifndef BLUEROV_ROS_PLAYGROUND_MESSAGE_CUSTOM_H
#define BLUEROV_ROS_PLAYGROUND_MESSAGE_CUSTOM_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace bluerov_ros_playground
{
template <class ContainerAllocator>
struct Custom_
{
  typedef Custom_<ContainerAllocator> Type;

  Custom_()
    : id()
    , data()  {
    }
  Custom_(const ContainerAllocator& _alloc)
    : id(_alloc)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _id_type;
  _id_type id;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::bluerov_ros_playground::Custom_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bluerov_ros_playground::Custom_<ContainerAllocator> const> ConstPtr;

}; // struct Custom_

typedef ::bluerov_ros_playground::Custom_<std::allocator<void> > Custom;

typedef boost::shared_ptr< ::bluerov_ros_playground::Custom > CustomPtr;
typedef boost::shared_ptr< ::bluerov_ros_playground::Custom const> CustomConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bluerov_ros_playground::Custom_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bluerov_ros_playground::Custom_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace bluerov_ros_playground

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'bluerov_ros_playground': ['/home/levy/Schreibtisch/bluerov_auto/src/bluerov_ros_playground/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bluerov_ros_playground::Custom_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bluerov_ros_playground::Custom_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bluerov_ros_playground::Custom_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fedf71ab0b24ef8723140dca2d5458bc";
  }

  static const char* value(const ::bluerov_ros_playground::Custom_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfedf71ab0b24ef87ULL;
  static const uint64_t static_value2 = 0x23140dca2d5458bcULL;
};

template<class ContainerAllocator>
struct DataType< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bluerov_ros_playground/Custom";
  }

  static const char* value(const ::bluerov_ros_playground::Custom_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string id\n"
"float32[] data\n"
"\n"
;
  }

  static const char* value(const ::bluerov_ros_playground::Custom_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Custom_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bluerov_ros_playground::Custom_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bluerov_ros_playground::Custom_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.id);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // BLUEROV_ROS_PLAYGROUND_MESSAGE_CUSTOM_H
