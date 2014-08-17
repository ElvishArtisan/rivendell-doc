Summary: Rivendell Operations Guide 
Name: rog
Version: 1.3.0
Release: 1
License: CC-BY-SA
Group: Documentation
URL: http://www.rivendellaudio.org/ftpdocs/rivendell/docs/%{name}-%{version}-%{release}.pdf
Source0: %{name}-%{version}-%{release}.pdf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A manual covering operations of the Rivendell Radio Autmation System.

#%prep
#%setup -q

#%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/rog
cp %{_sourcedir}/%{name}-%{version}-%{release}.pdf $RPM_BUILD_ROOT/usr/share/rog/
mkdir -p $RPM_BUILD_ROOT/etc/skel/Desktop
ln -s /usr/share/rog/%{name}-%{version}-%{release}.pdf $RPM_BUILD_ROOT/etc/skel/Desktop/Rivendell\ Ops\ Guide.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
find /home/* -maxdepth 0 -type d -exec ln -s /usr/share/rog/%{name}-%{version}-%{release}.pdf \{\}/Desktop/Rivendell\ Ops\ Guide.pdf \;

%preun
find /home/* -maxdepth 0 -type d -exec rm -f \{\}/Desktop/Rivendell\ Ops\ Guide.pdf \;

%files
%defattr(-,root,root,-)
/usr/share/rog/%{name}-%{version}-%{release}.pdf
"/etc/skel/Desktop/Rivendell Ops Guide.pdf"


%changelog
* Mon Feb  7 2011 Fred Gleason <fredg@paravelsystems.com> - 
- Initial build.

