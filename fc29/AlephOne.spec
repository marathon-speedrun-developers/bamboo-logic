%define name AlephOne
%define version 1.3
%define release 1

Summary: 3D first-person shooter game
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL3
Group: Amusements/Games
Source: release-20181006.tar.gz
URL: http://alephone.cebix.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# not relocatable because the data file packages depend upon the location
# of the data files in this package

Requires: SDL2 >= 1.2.0 SDL2_image >= 1.2.0 SDL2_net 
BuildRequires: SDL2-devel SDL2_image-devel SDL2_net-devel boost-devel 

%description
Aleph One is an Open Source 3D first-person shooter game, based on the game
Marathon 2 by Bungie Software. It is set in a Sci-Fi universe dominated by
deviant computer AIs and features a well thought-out plot. Aleph One
supports, but doesn't require, OpenGL for rendering.

Aleph One requires additional data -- shape, sound, and map
information -- in order to run. The easiest way to get this is to go
to http://source.bungie.org/get/, and download one of the scenario zip
files there. Unzip it, and pass the resulting directory as an argument
to alephone. For example:

alephone "~/Marathon Infinity"

%prep
%setup -q

%build
bash autogen.sh
make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL.Unix README docs/MML.html docs/Lua.html
%{_bindir}/alephone
%{_datadir}/icons
%{_datadir}/mime
%{_datadir}/AlephOne/MML
%{_datadir}/AlephOne/Plugins
%{_mandir}/man6/alephone.6.gz

%changelog
* Tue Feb 26 2019 Aleph One Developers <example@example.com>
- For the latest information on Aleph One, check the changelog
- at github.com/Aleph-One-Marathon/alephone/commits/master
