# Script generated with Bloom
pkgdesc="ROS - The lockfree package contains lock-free data structures for use in multithreaded programming. These kinds of data structures are generally not as easy to use as single-threaded equivalents, and are not always faster. If you don't know you need to use one, try another structure with a lock around it first."
url='http://ros.org/wiki/lockfree'

pkgname='ros-kinetic-lockfree'
pkgver='1.0.25_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-allocators'
'ros-kinetic-catkin'
'ros-kinetic-rosatomic'
'ros-kinetic-rosconsole'
'ros-kinetic-roslib'
)

depends=('ros-kinetic-allocators'
'ros-kinetic-rosatomic'
'ros-kinetic-rosconsole'
'ros-kinetic-roslib'
)

conflicts=()
replaces=()

_dir=lockfree
source=()
md5sums=()

prepare() {
    cp -R $startdir/lockfree $srcdir/lockfree
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

