%define version	0.3.1
%define release	%mkrel 8
%define name junkie

Summary: GTK2 ftp client
Name: %name
Version: %version
Release: %release
License: BSD
Group: Development/Other 
Source: http://prdownloads.sourceforge.net/junkie/%name%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://junkie.doomed.org/
BuildRequires: gtk+2-devel libmikmod-devel libvorbis-devel pkgconfig

%description
junkie is a GTK 2 GUI FTP client with a raw FTP library and a 
configuration library. It currently supports pre-caching of FTP 
sites and basic upload and download functions. Support for 
hammering and FXP is in development. 

%prep

%setup -q -n %name%{version}

%configure2_5x
#fix vulgarities
echo 'Joel Thomas loves Mandrake' > YoMomma
perl -p -i -e 's/\/YoMomma/\/Important Info/g' src/gui_menu.c

%build

%make

%install

%makeinstall
rm -f $RPM_BUILD_ROOT/%_datadir/%name/YoMamma

# menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=junkie
Icon=file_transfer_section
Categories=Network;FileTransfer;
Name=Junkie
Comment=GTK2 ftp client
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-, root, root)
%doc LICENSE README
%{_datadir}/applications/mandriva-%name.desktop
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-8mdv2011.0
+ Revision: 619871
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-7mdv2010.0
+ Revision: 429652
- rebuild

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 0.3.1-6mdv2009.0
+ Revision: 271849
- use the right configure macro

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-5mdv2009.0
+ Revision: 247429
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.3.1-3mdv2008.1
+ Revision: 132295
- auto-convert XDG menu entry
- fix gtk+ BR
- kill re-definition of %%buildroot on Pixel's request
- import junkie


