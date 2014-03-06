Name:           scratchduino
Version:        0.1
Release:        6.1
Group:          Education
License:        GPLv2
Summary:        Scratch mod to interact with ScratchDuino.Roboplatform
Url:            http://scratchduino.com
Source0:        scratchduino-0.1.tar.bz2
BuildArch:      noarch
Requires:       scratch

%description
This is a Scratch mod for working with ScratchDuino Robotics Framework.

%prep
%setup -q

%build
echo "empty"

%install
cp -a usr %{buildroot}/

%files
%{_datadir}/applications/*.desktop
%{_datadir}/scratchduino
