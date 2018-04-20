# Script generated with Bloom
pkgdesc="ROS - rosrt provides classes for interfacing with ROS from within realtime systems, such as realtime-safe Publisher and Subscriber classes."
url='http://ros.org/wiki/rosrt'

pkgname='ros-kinetic-rosrt'
pkgver='1.0.25_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-allocators'
'ros-kinetic-catkin'
'ros-kinetic-lockfree'
'ros-kinetic-rosatomic'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rosunit'
'ros-kinetic-std-msgs'
)

depends=('ros-kinetic-allocators'
'ros-kinetic-lockfree'
'ros-kinetic-rosatomic'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rosunit'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=rosrt
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosrt $srcdir/rosrt
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

