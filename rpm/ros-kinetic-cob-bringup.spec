Name:           ros-kinetic-cob-bringup
Version:        0.6.7
Release:        1%{?dist}
Summary:        ROS cob_bringup package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-canopen-chain-node
Requires:       ros-kinetic-canopen-motor-node
Requires:       ros-kinetic-cob-android-script-server
Requires:       ros-kinetic-cob-base-drive-chain
Requires:       ros-kinetic-cob-base-velocity-smoother
Requires:       ros-kinetic-cob-bms-driver
Requires:       ros-kinetic-cob-calibration-data
Requires:       ros-kinetic-cob-cam3d-throttle
Requires:       ros-kinetic-cob-collision-monitor
Requires:       ros-kinetic-cob-collision-velocity-filter
Requires:       ros-kinetic-cob-command-gui
Requires:       ros-kinetic-cob-control-mode-adapter
Requires:       ros-kinetic-cob-dashboard
Requires:       ros-kinetic-cob-default-env-config
Requires:       ros-kinetic-cob-default-robot-behavior
Requires:       ros-kinetic-cob-default-robot-config
Requires:       ros-kinetic-cob-docker-control
Requires:       ros-kinetic-cob-footprint-observer
Requires:       ros-kinetic-cob-frame-tracker
Requires:       ros-kinetic-cob-hand-bridge
Requires:       ros-kinetic-cob-hardware-config
Requires:       ros-kinetic-cob-helper-tools
Requires:       ros-kinetic-cob-image-flip
Requires:       ros-kinetic-cob-light
Requires:       ros-kinetic-cob-linear-nav
Requires:       ros-kinetic-cob-mimic
Requires:       ros-kinetic-cob-monitoring
Requires:       ros-kinetic-cob-moveit-config
Requires:       ros-kinetic-cob-obstacle-distance
Requires:       ros-kinetic-cob-omni-drive-controller
Requires:       ros-kinetic-cob-phidget-em-state
Requires:       ros-kinetic-cob-phidget-power-state
Requires:       ros-kinetic-cob-phidgets
Requires:       ros-kinetic-cob-reflector-referencing
Requires:       ros-kinetic-cob-relayboard
Requires:       ros-kinetic-cob-safety-controller
Requires:       ros-kinetic-cob-scan-unifier
Requires:       ros-kinetic-cob-script-server
Requires:       ros-kinetic-cob-sick-lms1xx
Requires:       ros-kinetic-cob-sick-s300
Requires:       ros-kinetic-cob-sound
Requires:       ros-kinetic-cob-teleop
Requires:       ros-kinetic-cob-trajectory-controller
Requires:       ros-kinetic-cob-twist-controller
Requires:       ros-kinetic-cob-undercarriage-ctrl
Requires:       ros-kinetic-cob-voltage-control
Requires:       ros-kinetic-compressed-depth-image-transport
Requires:       ros-kinetic-compressed-image-transport
Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-costmap-2d
Requires:       ros-kinetic-diagnostic-aggregator
Requires:       ros-kinetic-image-proc
Requires:       ros-kinetic-joint-state-controller
Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-joint-trajectory-controller
Requires:       ros-kinetic-joy
Requires:       ros-kinetic-laser-filters
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-openni-launch
Requires:       ros-kinetic-openni2-launch
Requires:       ros-kinetic-position-controllers
Requires:       ros-kinetic-realsense-camera
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-roslaunch
Requires:       ros-kinetic-rosserial-python
Requires:       ros-kinetic-rosserial-server
Requires:       ros-kinetic-rostopic
Requires:       ros-kinetic-rplidar-ros
Requires:       ros-kinetic-rviz
Requires:       ros-kinetic-schunk-powercube-chain
Requires:       ros-kinetic-sick-visionary-t-driver
Requires:       ros-kinetic-spacenav-node
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-theora-image-transport
Requires:       ros-kinetic-topic-tools
Requires:       ros-kinetic-twist-mux
Requires:       ros-kinetic-ur-driver
Requires:       ros-kinetic-usb-cam
Requires:       ros-kinetic-velocity-controllers
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cob-supported-robots
BuildRequires:  ros-kinetic-roslaunch

%description
This package provides launch files for operating Care-O-bot.

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
* Sat Aug 05 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.7-1
- Autogenerated by Bloom

