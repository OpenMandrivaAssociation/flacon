Summary:	Audio file splitter and converter
Name:		flacon
Version:	0.6.0
Release:	1
Group:		Graphical desktop/KDE4
License:	GPL
URL:		http://kde-apps.org/content/show.php/Flacon?content=113388
Source:		%{name}-%{version}.tgz
Requires:	python >= 2.6
Requires:	python-qt4
Requires:	shntool
Requires:	flac
Requires:	mac
Requires:	libwavpack1
Requires:	vorbis-tools
Requires:	lame
Requires:	vorbisgain
Requires:	mp3gain
Obsoletes:	%name < %version

%description
Flacon extracts individual tracks from one big audio file
containing the entire album of music and saves them as
separate audio files. To do this, it uses information
from the appropriate CUE file. Flacon also makes it possible
to conveniently revise or specify tags both for all tracks
at once or for each tag separately.

%prep
%setup -q

%build

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir %{buildroot}%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop


%files 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications
%{_datadir}/icons
