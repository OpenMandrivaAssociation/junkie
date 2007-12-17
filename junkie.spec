%define version	0.3.1
%define release	%mkrel 3
%define name junkie

Summary: GTK2 ftp client
Name: %name
Version: %version
Release: %release
License: BSD
Group: Development/Other 
Source: http://prdownloads.sourceforge.net/junkie/%name%{version}.tar.bz2
URL: http://junkie.doomed.org/
BuildRequires: libgtk+-devel libmikmod-devel libvorbis-devel pkgconfig

%description
junkie is a GTK 2 GUI FTP client with a raw FTP library and a 
configuration library. It currently supports pre-caching of FTP 
sites and basic upload and download functions. Support for 
hammering and FXP is in development. 

%prep

%setup -q -n %name%{version}

%configure
#fix vulgarities
echo 'Joel Thomas loves Mandrake' > YoMomma
perl -p -i -e 's/\/YoMomma/\/Important Info/g' src/gui_menu.c

%build

%make

%install

%makeinstall
rm -f $RPM_BUILD_ROOT/%_datadir/%name/YoMamma

# menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}): command="junkie" icon="file_transfer_section.png" needs="X11" section="Networking/File Transfer" title="Junkie" longtitle="GTK2 ftp client"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-, root, root)
%doc LICENSE README
%{_menudir}/%name
%{_bindir}/%name
%{_datadir}/%name

%ChangeLog
* Thu Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 0.3.1-3mdk
- rebuild

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-2mdk
- rebuild

* Fri Apr 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3.1-1mdk
- 0.3.1

* Tue Jan 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.3-2mdk
- rebuild

* Tue Dec 31 2002  Lenny Cartier <lenny@mandrakesoft.com> 0.3-1mdk
- from Austin Acton <aacton@yorku.ca> :
	- bump version
	- add sound support

* Mon Oct 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.2.1-2mdk
- from Austin Acton <aacton@yorku.ca> :
	- remove strange and vulgar jokes section

* Fri Oct 18 2002 Austin Acton <aacton@yorku.ca> 0.2.1-1mdk
- initial package creation for Mandrake 9
