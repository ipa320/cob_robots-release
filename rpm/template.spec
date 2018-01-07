Name:           ros-indigo-cob-default-robot-config
Version:        0.6.8
Release:        0%{?dist}
Summary:        ROS cob_default_robot_config package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_default_robot_config
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-roslaunch
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-supported-robots
BuildRequires:  ros-indigo-roslaunch

%description
Default configuration of the different robots supported by the Care-O-bot
stacks. Configuration is e.g. preconfigured joint positions.

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
* Sun Jan 07 2018 Felix Messmer <fxm@ipa.fhg.de> - 0.6.8-0
- Autogenerated by Bloom

* Mon Jul 31 2017 Nadia Hammoudeh Garcia <nhg@ipa.fhg.de> - 0.6.7-1
- Autogenerated by Bloom

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

