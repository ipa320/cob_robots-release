Name:           ros-indigo-cob-bringup
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS cob_bringup package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_bringup
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-canopen-chain-node
Requires:       ros-indigo-canopen-motor-node
Requires:       ros-indigo-cob-android-script-server
Requires:       ros-indigo-cob-base-drive-chain
Requires:       ros-indigo-cob-base-velocity-smoother
Requires:       ros-indigo-cob-bms-driver
Requires:       ros-indigo-cob-calibration-data
Requires:       ros-indigo-cob-cam3d-throttle
Requires:       ros-indigo-cob-collision-monitor
Requires:       ros-indigo-cob-collision-velocity-filter
Requires:       ros-indigo-cob-command-gui
Requires:       ros-indigo-cob-control-mode-adapter
Requires:       ros-indigo-cob-dashboard
Requires:       ros-indigo-cob-default-env-config
Requires:       ros-indigo-cob-default-robot-behavior
Requires:       ros-indigo-cob-default-robot-config
Requires:       ros-indigo-cob-docker-control
Requires:       ros-indigo-cob-footprint-observer
Requires:       ros-indigo-cob-frame-tracker
Requires:       ros-indigo-cob-hand-bridge
Requires:       ros-indigo-cob-hardware-config
Requires:       ros-indigo-cob-helper-tools
Requires:       ros-indigo-cob-image-flip
Requires:       ros-indigo-cob-light
Requires:       ros-indigo-cob-linear-nav
Requires:       ros-indigo-cob-mimic
Requires:       ros-indigo-cob-monitoring
Requires:       ros-indigo-cob-moveit-config
Requires:       ros-indigo-cob-obstacle-distance
Requires:       ros-indigo-cob-omni-drive-controller
Requires:       ros-indigo-cob-phidget-em-state
Requires:       ros-indigo-cob-phidget-power-state
Requires:       ros-indigo-cob-phidgets
Requires:       ros-indigo-cob-reflector-referencing
Requires:       ros-indigo-cob-relayboard
Requires:       ros-indigo-cob-safety-controller
Requires:       ros-indigo-cob-scan-unifier
Requires:       ros-indigo-cob-script-server
Requires:       ros-indigo-cob-sick-lms1xx
Requires:       ros-indigo-cob-sick-s300
Requires:       ros-indigo-cob-sound
Requires:       ros-indigo-cob-teleop
Requires:       ros-indigo-cob-trajectory-controller
Requires:       ros-indigo-cob-twist-controller
Requires:       ros-indigo-cob-undercarriage-ctrl
Requires:       ros-indigo-cob-voltage-control
Requires:       ros-indigo-compressed-depth-image-transport
Requires:       ros-indigo-compressed-image-transport
Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-diagnostic-aggregator
Requires:       ros-indigo-image-proc
Requires:       ros-indigo-joint-state-controller
Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-joint-trajectory-controller
Requires:       ros-indigo-joy
Requires:       ros-indigo-laser-filters
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-openni-launch
Requires:       ros-indigo-openni2-launch
Requires:       ros-indigo-position-controllers
Requires:       ros-indigo-realsense-camera
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-rosserial-python
Requires:       ros-indigo-rosserial-server
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-rplidar-ros
Requires:       ros-indigo-rviz
Requires:       ros-indigo-schunk-powercube-chain
Requires:       ros-indigo-sick-visionary-t-driver
Requires:       ros-indigo-spacenav-node
Requires:       ros-indigo-tf2-ros
Requires:       ros-indigo-theora-image-transport
Requires:       ros-indigo-topic-tools
Requires:       ros-indigo-twist-mux
Requires:       ros-indigo-ur-driver
Requires:       ros-indigo-usb-cam
Requires:       ros-indigo-velocity-controllers
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-supported-robots
BuildRequires:  ros-indigo-roslaunch

%description
This package provides launch files for operating Care-O-bot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 31 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Mon Oct 10 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Sat Aug 29 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

