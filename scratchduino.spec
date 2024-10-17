Name:           scratchduino
Version:        0.2
Release:        1
Group:          Education
License:        GPLv2
Summary:        Scratch mod to interact with ScratchDuino.Roboplatform
Url:            https://scratchduino.com
Source:         %{name}_%{version}.orig.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  hicolor-icon-theme
Requires:       scratch

%description
This is a Scratch mod for working with ScratchDuino Robotics Framework.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}/
chmod 644 %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/scratchduino
%{_bindir}/%{name}
