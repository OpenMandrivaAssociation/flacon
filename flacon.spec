# Disabled tests as tag related tests are not working with taglib >= 2.0
%bcond_with tests

Summary:	Audio file splitter and converter
Name:	flacon
Version:	13.0.2
Release:	1
License:	LGPL-2.1-or-later
Group:	Sound
Url:		https://flacon.github.io/
Source0:	https://github.com/flacon/flacon/archive/v%{version}/%{name}-%{version}.tar.gz
# dropped (no longer applies): Patch0:	flacon-13.0.2-use-qt5-style.patch
# dropped (no longer applies): Patch1:	flacon-13.0.2-fix-tab-order-for-tag-fields.patch
# For check
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	opus-tools
#BuildRequires:	gcc-c++
BuildRequires:	hicolor-icon-theme
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	qt6-qttools
%if %{with tests}
BuildRequires:	alacenc
BuildRequires:	cmake(yaml-cpp)
BuildRequires:	faac
BuildRequires:	flac
BuildRequires:	lame
BuildRequires:	mac
BuildRequires:	mp3gain
BuildRequires:	opus-tools
BuildRequires:	sox
BuildRequires:	ttaenc
BuildRequires:	vorbisgain
BuildRequires:	vorbis-tools
BuildRequires:	wavpack
%endif
BuildRequires:	cmake(utf8cpp)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Linguist)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Tools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(zlib-ng)
BuildRequires:	pkgconfig(libopusenc)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(uchardet)
BuildRequires:	pkgconfig(zlib)
# A general purpose sound file conversion tool
Recommends:	sox
# formats/alac.h (encoder)
Recommends:	alacenc
# formats/aac.h (encoder)
Recommends:	faac
# formats/flac.h (encoder, decoder)
Recommends:	flac
# formats/mp3.h (encoder)
Recommends:	lame
# formats/ape.h (encoder, decoder)
Recommends:	mac
# mp3 gain correction utility
Recommends:	mp3gain
# formats/ogg.h (encoder, decoder)
Recommends:	opus-tools
# formats/tta.h (encoder)
Recommends:	ttaenc
# formats/wv.h (encoder, decoder)
Recommends:	vorbis-tools
# ogg-vorbis gain correction utility
Recommends:	vorbisgain
# formats/opus.h (encoder, decoder)
Recommends:	wavpack

%description
Flacon extracts individual tracks from one big audio file containing the
entire album of music and saves them as separate audio files. To do this, it
uses information from the appropriate CUE file. Flacon also makes it possible
to conveniently revise or specify tags both for all tracks at once or for each
tag separately.

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version} -p1


%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_CXX_FLAGS="%{optflags}" \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_TESTS=%{?with_tests:Yes}%{!?with_tests:No} \
    -DUSE_QT6=On \
    -DUSE_QT5=Off \
    -G Ninja
%ninja_build


%install
%ninja_install -C build

%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.Flacon.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%if %{with tests}
cd build
%ninja_test
#cd build && ./tests/flacon_test
%endif
