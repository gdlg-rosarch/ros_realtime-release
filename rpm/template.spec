Name:           ros-kinetic-rosrt
Version:        1.0.25
Release:        0%{?dist}
Summary:        ROS rosrt package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosrt
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-allocators
Requires:       ros-kinetic-lockfree
Requires:       ros-kinetic-rosatomic
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rosunit
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-allocators
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-lockfree
BuildRequires:  ros-kinetic-rosatomic
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-std-msgs

%description
rosrt provides classes for interfacing with ROS from within realtime systems,
such as realtime-safe Publisher and Subscriber classes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 12 2018 Devon Ash <dash@clearpathrobotics.com> - 1.0.25-0
- Autogenerated by Bloom

