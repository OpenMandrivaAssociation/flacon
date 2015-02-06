Summary:	Audio file splitter and converter
Name:		flacon
Version:	1.0.1
Release:	2
Group:		Sound
License:	GPLv3
URL:		http://flacon.github.io/
# https://github.com/flacon/flacon/archive/v%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:	desktop-file-utils
BuildRequires:  qt4-devel
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  cmake

Requires:	shntool
Requires:	flac
Requires:	wavpack
Requires:	vorbis-tools
Requires:	vorbisgain
Requires:	mp3gain
Requires:	ttaenc

Suggests:       faac
Suggests:       lame
Suggests:	mac


%description
Flacon extracts individual tracks from one big audio file containing the
entire album of music and saves them as separate audio files. To do this, it
uses information from the appropriate CUE file. Flacon also makes it possible
to conveniently revise or specify tags both for all tracks at once or for each
tag separately.


%prep
%setup -q


%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}"
%make VERBOSE=1


%install
%makeinstall_std -C build

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man?/*
