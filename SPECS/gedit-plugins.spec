%if 0%{?fedora} > 12
%global with_zeitgeist 1
%else
%global with_zeitgeist 0
%endif

%global __python %{__python3}

Name:           gedit-plugins
Version:        3.28.1
Release:        8%{?dist}
Summary:        Plugins for gedit

License:        GPLv2+
URL:            https://wiki.gnome.org/Apps/Gedit
Source0:        https://download.gnome.org/sources/%{name}/3.28/%{name}-%{version}.tar.xz

BuildRequires:  gedit-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  gettext
BuildRequires:  cairo-devel
BuildRequires:  atk-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  intltool
BuildRequires:  libpeas-devel
BuildRequires:  vala
BuildRequires:  vte291-devel
BuildRequires:  yelp-tools
BuildRequires:  itstool
%if %{with_zeitgeist}
BuildRequires:  zeitgeist-devel
%endif

Obsoletes:      gedit-plugin-synctex < 3.28.1-4%{?dist}
Provides:       gedit-plugin-synctex = 3.28.1-4%{?dist}

# this is a metapackage dragging in all the plugins
Requires:       gedit-plugin-bookmarks
Requires:       gedit-plugin-bracketcompletion
Requires:       gedit-plugin-codecomment
Requires:       gedit-plugin-colorpicker
Requires:       gedit-plugin-colorschemer
Requires:       gedit-plugin-commander
%if %{with_zeitgeist}
Requires:       gedit-plugin-dashboard
%endif
Requires:       gedit-plugin-drawspaces
Requires:       gedit-plugin-findinfiles
Requires:       gedit-plugin-joinlines
Requires:       gedit-plugin-multiedit
Requires:       gedit-plugin-smartspaces
Requires:       gedit-plugin-terminal
Requires:       gedit-plugin-textsize
Requires:       gedit-plugin-translate
Requires:       gedit-plugin-wordcompletion
%if %{with_zeitgeist}
Requires:       gedit-plugin-zeitgeist
%endif

%description
A collection of plugins for gedit.

%package data
Summary:        Common data required by plugins
Requires:       gedit
Requires:       python3-gobject
%description data
Common files required by all plugins.

%package -n     gedit-plugin-bookmarks
Summary:        gedit bookmarks plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-bookmarks
The gedit bookmarks plugin.

%package -n     gedit-plugin-bracketcompletion
Summary:        gedit bracketcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-bracketcompletion
The gedit bracketcompletion plugin.

%package -n     gedit-plugin-codecomment
Summary:        gedit codecomment plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-codecomment
The gedit codecomment plugin.

%package -n     gedit-plugin-colorpicker
Summary:        gedit colorpicker plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-colorpicker
The gedit colorpicker plugin.

%package -n     gedit-plugin-colorschemer
Summary:        gedit colorschemer plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-colorschemer
The gedit colorschemer plugin.

%package -n     gedit-plugin-commander
Summary:        gedit commander plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-commander
The gedit commander plugin.

%if %{with_zeitgeist}
%package -n     gedit-plugin-dashboard
Summary:        gedit dashboard plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-dashboard
The gedit dashboard plugin.
%endif

%package -n     gedit-plugin-drawspaces
Summary:        gedit drawspaces plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-drawspaces
The gedit drawspaces plugin.

%package -n     gedit-plugin-findinfiles
Summary:        gedit findinfiles plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-findinfiles
The gedit findinfiles plugin.

%package -n     gedit-plugin-joinlines
Summary:        gedit joinlines plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-joinlines
The gedit joinlines plugin.

%package -n     gedit-plugin-multiedit
Summary:        gedit multiedit plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-multiedit
The gedit multiedit plugin.

%package -n     gedit-plugin-smartspaces
Summary:        gedit smartspaces plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-smartspaces
The gedit smartspaces plugin.

%package -n     gedit-plugin-terminal
Summary:        gedit terminal plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
Requires:       vte291
%description -n gedit-plugin-terminal
The gedit terminal plugin.

%package -n     gedit-plugin-textsize
Summary:        gedit textsize plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-textsize
The gedit textsize plugin.

%package -n     gedit-plugin-translate
Summary:        gedit translate plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-translate
The gedit translate plugin.

%package -n     gedit-plugin-wordcompletion
Summary:        gedit wordcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-wordcompletion
The gedit wordcompletion plugin.

%if %{with_zeitgeist}
%package -n     gedit-plugin-zeitgeist
Summary:        gedit zeitgeist plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       zeitgeist
Obsoletes:      gedit-zeitgeist < 2:3.13.0
%description -n gedit-plugin-zeitgeist
The gedit zeitgeist plugin.
%endif

%prep
%setup -q

%build
%if %{with_zeitgeist}
%configure --enable-python
%else
%configure --enable-python --disable-zeitgeist
%endif
make %{?_smp_mflags}


%install
%make_install
%find_lang %{name} --with-gnome
%find_lang gedit --with-gnome
find $RPM_BUILD_ROOT/%{_libdir}/gedit/plugins -name "*.la" -exec rm {} \;


%check
[ -f ${RPM_BUILD_ROOT}%{_libdir}/gedit/plugins/terminal.py ]


%postun -n gedit-plugin-drawspaces
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans -n gedit-plugin-drawspaces
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :


%postun -n gedit-plugin-terminal
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans -n gedit-plugin-terminal
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :


%postun -n gedit-plugin-wordcompletion
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans -n gedit-plugin-wordcompletion
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :


# Empty files section for the metapackage to make sure it's created
%files

%files data -f %{name}.lang -f gedit.lang
%license COPYING
%doc README NEWS AUTHORS
%dir %{_libdir}/gedit/plugins/
%dir %{_libdir}/gedit/plugins/__pycache__/
%dir %{_datadir}/gedit/plugins/
%{_libdir}/gedit/plugins/gpdefs.*
%{_libdir}/gedit/plugins/__pycache__/gpdefs.*

%files -n gedit-plugin-bookmarks
%{_libdir}/gedit/plugins/bookmarks.plugin
%{_libdir}/gedit/plugins/libbookmarks.so
%{_datadir}/appdata/gedit-bookmarks.metainfo.xml

%files -n gedit-plugin-bracketcompletion
%{_libdir}/gedit/plugins/bracketcompletion.*
%{_libdir}/gedit/plugins/__pycache__/bracketcompletion.*
%{_datadir}/appdata/gedit-bracketcompletion.metainfo.xml

%files -n gedit-plugin-codecomment
%{_libdir}/gedit/plugins/codecomment.*
%{_libdir}/gedit/plugins/__pycache__/codecomment.*
%{_datadir}/appdata/gedit-codecomment.metainfo.xml

%files -n gedit-plugin-colorpicker
%{_libdir}/gedit/plugins/colorpicker.*
%{_libdir}/gedit/plugins/__pycache__/colorpicker.*
%{_datadir}/appdata/gedit-colorpicker.metainfo.xml

%files -n gedit-plugin-colorschemer
%{_datadir}/gedit/plugins/colorschemer/ui/schemer.ui
%{_libdir}/gedit/plugins/colorschemer
%{_libdir}/gedit/plugins/colorschemer.plugin
%{_datadir}/appdata/gedit-colorschemer.metainfo.xml

%files -n gedit-plugin-commander
%{_datadir}/gedit/plugins/commander
%{_libdir}/gedit/plugins/commander
%{_libdir}/gedit/plugins/commander.plugin
%{_datadir}/appdata/gedit-commander.metainfo.xml

%if %{with_zeitgeist}
%files -n gedit-plugin-dashboard
%{_libdir}/gedit/plugins/dashboard
%{_libdir}/gedit/plugins/dashboard.plugin
%{_datadir}/appdata/gedit-dashboard.metainfo.xml
%endif

%files -n gedit-plugin-drawspaces
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%{_libdir}/gedit/plugins/drawspaces.plugin
%{_libdir}/gedit/plugins/libdrawspaces.so
%{_datadir}/appdata/gedit-drawspaces.metainfo.xml

%files -n gedit-plugin-findinfiles
%{_libdir}/gedit/plugins/findinfiles.plugin
%{_libdir}/gedit/plugins/libfindinfiles.so
%{_datadir}/appdata/gedit-findinfiles.metainfo.xml

%files -n gedit-plugin-joinlines
%{_libdir}/gedit/plugins/joinlines.*
%{_libdir}/gedit/plugins/__pycache__/joinlines.*
%{_datadir}/appdata/gedit-joinlines.metainfo.xml

%files -n gedit-plugin-multiedit
%{_libdir}/gedit/plugins/multiedit
%{_libdir}/gedit/plugins/multiedit.plugin
%{_datadir}/appdata/gedit-multiedit.metainfo.xml

%files -n gedit-plugin-smartspaces
%{_libdir}/gedit/plugins/__pycache__/smartspaces.*
%{_libdir}/gedit/plugins/smartspaces.*
%{_datadir}/appdata/gedit-smartspaces.metainfo.xml

%files -n gedit-plugin-terminal
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml
%{_libdir}/gedit/plugins/__pycache__/terminal.*
%{_libdir}/gedit/plugins/terminal.*
%{_datadir}/appdata/gedit-terminal.metainfo.xml

%files -n gedit-plugin-textsize
%{_libdir}/gedit/plugins/textsize
%{_libdir}/gedit/plugins/textsize.plugin
%{_datadir}/appdata/gedit-textsize.metainfo.xml

%files -n gedit-plugin-translate
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.translate.gschema.xml
%{_libdir}/gedit/plugins/translate/
%{_libdir}/gedit/plugins/translate.plugin
%{_datadir}/appdata/gedit-translate.metainfo.xml
%{_datadir}/gedit/plugins/translate/

%files -n gedit-plugin-wordcompletion
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
%{_libdir}/gedit/plugins/libwordcompletion.so
%{_libdir}/gedit/plugins/wordcompletion.plugin
%{_datadir}/appdata/gedit-wordcompletion.metainfo.xml

%if %{with_zeitgeist}
%files -n gedit-plugin-zeitgeist
%{_libdir}/gedit/plugins/libzeitgeist.so
%{_libdir}/gedit/plugins/zeitgeist.plugin
%{_datadir}/appdata/gedit-zeitgeist.metainfo.xml
%endif

%changelog
* Wed May 01 2019 Ray Strode <rstrode@redhat.com> - 3.28.1-8
- bump release for correctly start gating process
  Related: #1698642


* Wed May 01 2019 Ray Strode <rstrode@redhat.com> - 3.28.1-7
- Add obsoletes/provides for dropped plugin
  Related: #1698642

* Mon Oct 15 2018 Ray Strode <rstrode@redhat.com> - 3.28.1-4
- Drop unused dependencies
  Resolves: #1599393

* Wed Jul 11 2018 Charalampos Stratakis <cstratak@redhat.com> - 3.28.1-3
- Remove gnome-doc-utils dependency

* Thu May 10 2018 Ray Strode <rstrode@redhat.com> - 3.28.1-2
- Drop gucharmap plugin
  Resolves: #1576731
- Drop libgit plugin too

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.1-1
- Update to 3.27.1
- Add new translate plugin

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Ray Strode <rstrode@redhat.com> - 3.22.0-5
- Drop non-functional python2 support

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags
- Use make_install macro
- Update project URLs

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.1-1
- Update to 3.17.1
- Require gucharmap-libs instead of gucharmap

* Fri Jul 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.17.0-4
- Rebuilt for libgit2-0.23.0 and libgit2-glib-0.23

* Sat Jul 04 2015 Kalev Lember <klember@redhat.com> - 3.17.0-3
- Require libpeas-loader-python3 for Python 3 plugin support (#1226879)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.0-1
- Update to 3.17.0
- Include new findinfiles plugin

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1
- Use %%license macro for the COPYING file

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.0-1
- Update to 3.15.0

* Wed Nov 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Wed Nov 05 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.14.0-2
- We need the new VTE API/ABI to run
- Carry an upstream patch to pick up a last-minute VTE API break

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu Jul 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Wed Jun 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.0-2
- Ship gpdefs in the -data package
- Build the zeitgeist plugin

* Wed Jun 25 2014 Richard Hughes <rhughes@redhat.com> - 3.13.0-1
- Update to 3.13.0

* Fri Jun 13 2014 Richard Hughes <rhughes@redhat.com> - 3.12.1-3
- Split out the plugins into subpackages
- This allows us to add and remove them separately in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Fri Feb 14 2014 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Fri Dec 27 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.10.1-1
- Update to 3.10.1

* Tue Sep 24 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.10.0-1
- Update to 3.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.3-1
- Update to 3.8.3

* Sun May 26 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.2-1
- Update to 3.8.2

* Mon May  6 2013 Marek Kasik <mkasik@redhat.com> - 3.8.1-2
- Make building of Zeitgeist plugins and usage of python3 conditional

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-2
- Rebuilt for gtksourceview3 soname bump

* Mon Mar 25 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.0-1
- Update to 3.8.0

* Sun Jan 27 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.7.1-1
- Update to 3.7.1

* Tue Oct 16 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.6.1-1
- Update to 3.6.1

* Mon Sep 24 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.5.2-1
- Update to 3.5.2

* Sat Aug 18 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.5.1-1
- Update to 3.5.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-2
- Silence rpm scriptlet output

* Mon Mar 26 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 07 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.4-1
- Update to 3.3.4

* Sat Feb 25 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.3-1
- Update to 3.3.3

* Tue Feb 07 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.2-1
- Update to 3.3.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 03 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.1-1
- Update to 3.3.1

* Sun Oct 16 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.1-1
- Update to 3.2.1

* Mon Sep 26 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.0-1
- Update to 3.2.0
- Bump pygobject to 3.0

* Tue Sep 20 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.5-1
- Update to 3.1.5

* Tue Sep 06 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.4-1
- Update to 3.1.4

* Thu Sep 01 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.3-1
- Update to 3.1.3

* Tue Jul 05 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.2-1
- Update to 3.1.2

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Wed May 18 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.0.2-2
- Remove useless deps

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Wed Apr 13 2011 Christopher Aillon <caillon@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Wed Apr  6 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Sun Mar 27 2011 Christopher Aillon <caillon@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.1-1
- Update to 2.91.1

* Mon Feb 28 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-3
- Rebuild against newer libpeas

* Thu Feb 24 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-2
- Add runtime dependencies to make introspection work

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct  7 2010 Matthias Clasen <mclasen@redhat.com> 2.31.6-1
- Rebuild against newer gucharmap

* Thu Sep 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.31.6-1
- Updated to 2.31.6
- FTBFS 599912

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.31.1-2
- recompiling .py files against Python 2.7 (rhbz#623308)

* Wed May 19 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.31.1-1
- Updated to 2.31.1

* Fri Apr 23 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.30.0-1
- Updated to 2.30.0

* Wed Jan 27 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.29.4-1
- Updated to 2.29.4

* Wed Dec 02 2009 Rakesh Pandit <rakesh@fedoraproject.org> 2.29.3-1
- Updated to 2.29.3

* Mon Nov 09 2009 Rakesh Pandit <rakesh@fedoraproject.org> 2.28.0-1
- Updated to 2.28.0

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.26.1-3
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Dodji Seketeli <dodji@redhat.org> - 2.26.1-1
- Update to upstream release 2..26.1
- Fixes GNOME bugzilla bug #576766 - Crash when Configuring "Draw Spaces"
- Make sure to remove all *.la files
- Remove BuildRequire libgnomeui-devel as needless now

* Fri Apr 10 2009 Dodji Seketeli <dodji@redhat.org> - 2.26.0-1
- Update to upstream release (2.26.1)
- Add plugin files from %%{_datadir}
- Don't check for vte anymore, the package checks it pkg-config
- Add 'bookmarks' to the plugin set

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.22.3-3
- Rebuild for Python 2.6

* Mon Sep 29 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.22.3-2
- Fixed buildrequires

* Mon Sep 29 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.22.3-1
- Updated to 2.22.3

* Mon Sep 29 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.22.0-2
- rebuild to pick latest gucharmap

* Tue Mar 18 2008 Trond Danielsen <trond.danielsen@gmail.com> - 2.22.0-1
- Updated.

* Mon Apr 30 2007 Trond Danielsen <trond.danielsen@gmail.com> - 2.18.0-2
- Disable buggy session saver plugin.
- Removed static libraries.

* Sun Apr 01 2007 Trond Danielsen <trond.danielsen@gmail.com> - 2.18.0-1
- Initial version.
