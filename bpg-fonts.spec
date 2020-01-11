%define fontname bpg
%define fontconf 64-%{fontname}.conf
%define common_ver 20120413

%define common_desc BPG Fonts are a set of GPL licensed Georgian Unicode fonts.

Name:		%{fontname}-fonts
Summary: 	Georgian Unicode fonts
Version:	%{common_ver}
Release:	2%{?dist}
# Font exception
# See: http://groups.google.com/group/bpg-fonts/web/gpl-gnu-license
# No version of the GPL is specified.
License:	GPL+ with exceptions
Group:		User Interface/X
# Source was found here:
# http://bpgfonts.wordpress.com/category/gpl-gnu/
# But the link is annoying:
# http://www.box.com/s/1f344f181567cb897395
Source0:	BPG_GPL_GNU_Fonts_2012.zip
Source1:	%{name}-algeti-fontconfig.conf
Source2:	%{name}-chveulebrivi-fontconfig.conf
Source3:	%{name}-courier-fontconfig.conf
Source4:	%{name}-courier-s-fontconfig.conf
Source5:	%{name}-elite-fontconfig.conf
Source6:	%{name}-glaho-fontconfig.conf
Source7:	%{name}-ingiri-fontconfig.conf
Source8:	%{name}-nino-medium-fontconfig.conf
Source9:	%{name}-nino-medium-cond-fontconfig.conf
Source10:	%{name}-sans-fontconfig.conf
Source11:	%{name}-sans-medium-fontconfig.conf
Source12:	%{name}-sans-modern-fontconfig.conf
Source13:	%{name}-sans-regular-fontconfig.conf
Source14:	%{name}-serif-fontconfig.conf
Source15:	%{name}-serif-modern-fontconfig.conf
# The source for this one is buried in javascript garbage:
# http://cid-2b325d7bf5367fe3.skydrive.live.com/self.aspx/Fonts%20%E1%83%A4%E1%83%9D%E1%83%9C%E1%83%A2%E1%83%94%E1%83%91%E1%83%98/GPL%20|0%20GNU%20Fonts/BPG|_Excelsior|_GPL|0GNU.zip
# Also, I renamed it to remove the &
# Now part of the main fontset zip.
# Source16:	BPG_Excelsior_GPL_and_GNU.zip
Source17:	%{name}-excelsior-fontconfig.conf
# New fonts in 2012
Source18:	%{name}-classic-fontconfig.conf
Source19:	%{name}-excelsior-caps-fontconfig.conf
Source20:	%{name}-excelsior-condenced-fontconfig.conf
Source21:	%{name}-gorda-fontconfig.conf
Source22:	%{name}-irubaqidze-fontconfig.conf
Source23:	%{name}-mikhail-stephan-fontconfig.conf
Source24:	%{name}-mrgvlovani-fontconfig.conf
Source25:	%{name}-mrgvlovani-caps-fontconfig.conf
Source26:	%{name}-nateli-fontconfig.conf
Source27:	%{name}-nateli-caps-fontconfig.conf
Source28:	%{name}-nateli-condenced-fontconfig.conf
Source29:	%{name}-ucnobi-fontconfig.conf
Source30:	%{name}-dedaena-block-fontconfig.conf
Source31:	%{name}-dejavu-sans-fontconfig.conf
# Docs
Source100:	README
Source101:	http://www.gnu.org/licenses/gpl-3.0.txt

URL:		http://groups.google.com/group/bpg-fonts
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	fontpackages-devel
BuildArch:	noarch

%description
%common_desc

%package common
Summary:	Common files for BPG Georgian fonts (documentation...)
Group:		User Interface/X
Requires:	fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other BPG font packages.

%package -n %{fontname}-algeti-fonts
Summary:	Algeti Family of BPG Georgian Fonts
Version:	2.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-algeti-fonts
%common_desc

This package contains the Algeti font family.

%_font_pkg -n algeti -f %{fontconf}-algeti.conf "BPG_Algeti*.ttf"

%package -n %{fontname}-chveulebrivi-fonts
Summary:	Chveulebrivi family of BPG Georgian fonts
Version:	3.002
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-chveulebrivi-fonts
%common_desc

This package contains the Chveulebrivi font family.

%_font_pkg -n chveulebrivi -f %{fontconf}-chveulebrivi.conf "BPG_Chveulebrivi_*.ttf"

%package -n %{fontname}-classic-fonts
Summary:	Classic family of BPG Georgian fonts
Version:	8.500
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-classic-fonts
%common_desc

This package contains the Classic font family.

%_font_pkg -n classic -f %{fontconf}-classic.conf "BPG_Classic_*.otf"

%package -n %{fontname}-courier-fonts
Summary:	Courier family of BPG Georgian fonts
Version:	4.002
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-courier-fonts
%common_desc

This package contains the Courier font family.

%_font_pkg -n courier -f %{fontconf}-courier.conf "BPG_Courier_GPL*.ttf"

%package -n %{fontname}-courier-s-fonts
Summary:	Courier S family of BPG Georgian fonts
Version:	4.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-courier-s-fonts
%common_desc

This package contains the Courier S font family.

%_font_pkg -n courier-s -f %{fontconf}-courier-s.conf "BPG_Courier_S*.ttf"

%package -n %{fontname}-dedaena-block-fonts
Summary:	DedaEna Block family of BPG Georgian fonts
Version:	3.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-dedaena-block-fonts
%common_desc

This package contains the DedaEna Block font family.

%_font_pkg -n dedaena-block -f %{fontconf}-dedaena-block.conf "BPG_DedEena_Block*.ttf"

%package -n %{fontname}-dejavu-sans-fonts
Summary:	DejaVu Sans with BPG Georgian changes
Version:	2.28
License:	Bitstream Vera
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-dejavu-sans-fonts
%common_desc

This package contains an improved version of DejaVu Sans with BPG Georgian 
changes.

%_font_pkg -n dejavu-sans -f %{fontconf}-bpg-dejavu-sans.conf "BPG_DejaVu_Sans_*.ttf"

%package -n %{fontname}-elite-fonts
Summary:	Elite family of BPG Georgian fonts
Version:	3.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-elite-fonts
%common_desc

This package contains the Elite font family.

%_font_pkg -n elite -f %{fontconf}-elite.conf "BPG_Elite*.ttf"

%package -n %{fontname}-excelsior-fonts
Summary:	Excelsior family of BPG Georgian fonts
Version:	2.03
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n %{fontname}-excelsior-fonts
%common_desc

This package contains the Excelsior font family.

%_font_pkg -n excelsior -f %{fontconf}-excelsior.conf "BPG_Excelsior_GPL*.ttf"

%package -n %{fontname}-excelsior-caps-fonts
Summary:	Excelsior Caps family of BPG Georgian fonts
Version:	2.003
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n %{fontname}-excelsior-caps-fonts
%common_desc

This package contains the Excelsior Caps font family.

%_font_pkg -n excelsior-caps -f %{fontconf}-excelsior-caps.conf "BPG_Excelsior_Caps*.ttf"

%package -n %{fontname}-excelsior-condenced-fonts
Summary:	Excelsior Condenced family of BPG Georgian fonts
Version:	2.003
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}
License:	Bitstream Vera

%description -n %{fontname}-excelsior-condenced-fonts
%common_desc

This package contains the Excelsior Condenced font family.

%_font_pkg -n excelsior-condenced -f %{fontconf}-excelsior-condenced.conf "BPG_Excelsior_Condenced*.ttf"

%package -n %{fontname}-glaho-fonts
Summary:	Glaho family of BPG Georgian fonts
Version:	9.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-glaho-fonts
%common_desc

This package contains the Glaho font family.
%_font_pkg -n glaho -f %{fontconf}-glaho.conf "BPG_Glaho*.ttf"

%package -n %{fontname}-gorda-fonts
Summary:	Gorda family of BPG Georgian fonts
Version:	2.003
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-gorda-fonts
%common_desc

This package contains the Gorda font family.

%_font_pkg -n gorda -f %{fontconf}-gorda.conf "BPG_Gorda*.ttf"

%package -n %{fontname}-ingiri-fonts
Summary:	Ingiri family of BPG Georgian fonts
Version:	4.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-ingiri-fonts
%common_desc

This package contains the Ingiri font family.

%_font_pkg -n ingiri -f %{fontconf}-ingiri.conf "BPG_Ingiri*.ttf"

%package -n %{fontname}-irubaqidze-fonts
Summary:	Irubaqidze family of BPG Georgian fonts
Version:	1.000
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-irubaqidze-fonts
%common_desc

This package contains the Irubaqidze font family. In 1628 Georgian printing 
types were produced for the first time, in Rome. The "Georgian-Italian 
Dictionary"  and "Georgian Prayers" were printed in Rome, 1629, by Stephano 
Paolini and Nikiphore Irbach (Irubakhidze-Cholokashvili). In 1643, in Rome, 
"Georgian Grammar" by Francisco-Maria Majio was printed, using Nuskhuri, 
Asomtavruli and Mkhedruli. Majio spent 7 years in Georgia studying Georgian 
language, scripture and grammar. Font "BPG Irubaqidze" is a modernized 
replica of this casted type. 

%_font_pkg -n irubaqidze -f %{fontconf}-irubaqidze.conf "BPG_Irubaqidze*.otf"

%package -n %{fontname}-mikhail-stephan-fonts
Summary:	Mikhail Stephan family of BPG Georgian fonts
Version:	2.500
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-mikhail-stephan-fonts
%common_desc

This package contains the Mikhail Stephan font family. This type was first 
produced in 1709, by the printing-house of King Vahtang VI. In 1712, it was
used to print "The Knight in the Panther's Skin" by Shota Rustaveli, then 
"New Testament" and "The Bible" were printed using updated types prepared 
in Tbilisi by Hungarian Master Michael Stefan Hungaro-Valakhian.

%_font_pkg -n mikhail-stephan -f %{fontconf}-mikhail-stephan.conf "BPG_Mikhail_Stephan*.otf"

%package -n %{fontname}-mrgvlovani-fonts
Summary:	Mrgvlovani family of BPG Georgian fonts
Version:	1.002
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-mrgvlovani-fonts
%common_desc

This package contains the Mrgvlovani font family.

%_font_pkg -n mrgvlovani -f %{fontconf}-mrgvlovani.conf "BPG_Mrgvlovani_GPL*.ttf"

%package -n %{fontname}-mrgvlovani-caps-fonts
Summary:	Mrgvlovani Caps family of BPG Georgian fonts
Version:	1.002
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n	%{fontname}-mrgvlovani-caps-fonts
%common_desc

This package contains the Mrgvlovani Caps font family.

%_font_pkg -n mrgvlovani-caps -f %{fontconf}-mrgvlovani-caps.conf "BPG_Mrgvlovani_Caps_*.ttf"

%package -n %{fontname}-nateli-fonts
Summary:	Nateli family of BPG Georgian fonts
Version:	2.003
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nateli-fonts
%common_desc

This package contains the Nateli font family.

%_font_pkg -n nateli -f %{fontconf}-nateli.conf "BPG_Nateli_GPL*.ttf"

%package -n %{fontname}-nateli-caps-fonts
Summary:	Nateli Caps family of BPG Georgian fonts
Version:	2.003
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nateli-caps-fonts
%common_desc

This package contains the Nateli Caps font family.

%_font_pkg -n nateli-caps -f %{fontconf}-nateli-caps.conf "BPG_Nateli_Caps*.ttf"

%package -n %{fontname}-nateli-condenced-fonts
Summary:	Nateli Condenced family of BPG Georgian fonts
Version:	2.003
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nateli-condenced-fonts
%common_desc

This package contains the Nateli Condenced font family.

%_font_pkg -n nateli-condenced -f %{fontconf}-nateli-condenced.conf "BPG_Nateli_Condenced*.ttf"

%package -n %{fontname}-nino-medium-fonts
Summary:	Nino Medium family of BPG Georgian fonts
Version:	4.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n	%{fontname}-nino-medium-fonts
%common_desc

This package contains the Nino Medium font family.

%_font_pkg -n nino-medium -f %{fontconf}-nino-medium.conf "BPG_Nino_Medium_GPL*.ttf"

%package -n %{fontname}-nino-medium-cond-fonts
Summary:	Nino Medium Cond family of BPG Georgian fonts
Version:	4.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-nino-medium-cond-fonts
%common_desc

This package contains the Nino Medium Cond font family.

%_font_pkg -n nino-medium-cond -f %{fontconf}-nino-medium-cond.conf "BPG_Nino_Medium_Cond*.ttf"

%package -n %{fontname}-sans-fonts
Summary:	Sans family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-sans-fonts
%common_desc

This package contains the Sans font family.

%_font_pkg -n sans -f %{fontconf}-sans.conf "BPG_Sans_GPL*.ttf"

%package -n %{fontname}-sans-medium-fonts
Summary:	Sans Medium family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-sans-medium-fonts
%common_desc

This package contains the Sans Medium font family.

%_font_pkg -n sans-medium -f %{fontconf}-sans-medium.conf "BPG_Sans_Medium*.ttf"

%package -n %{fontname}-sans-modern-fonts
Summary:	Sans Modern family of BPG Georgian fonts
Version:	2.025
License:	Bitstream Vera
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n	%{fontname}-sans-modern-fonts
%common_desc

This package contains the Sans Modern font family.

%_font_pkg -n sans-modern -f %{fontconf}-sans-modern.conf "BPG_Sans_Modern*.ttf"

%package -n %{fontname}-sans-regular-fonts
Summary:	Sans Regular family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-sans-regular-fonts
%common_desc

This package contains the Sans Regular font family.

%_font_pkg -n sans-regular -f %{fontconf}-sans-regular.conf "BPG_Sans_Regular*.ttf"

%package -n %{fontname}-serif-fonts
Summary:	Serif family of BPG Georgian fonts
Version:	1.005
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-serif-fonts
%common_desc

This package contains the Serif font family.

%_font_pkg -n serif -f %{fontconf}-serif.conf "BPG_Serif_GPL*.ttf"

%package -n %{fontname}-serif-modern-fonts
Summary:	Serif Modern family of BPG Georgian fonts
Version:	2.028
License:	Bitstream Vera
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-serif-modern-fonts
%common_desc

This package contains the Serif Modern font family.

%_font_pkg -n serif-modern -f %{fontconf}-serif-modern.conf "BPG_Serif_Modern*.ttf"

%package -n %{fontname}-ucnobi-fonts
Summary:	Ucnobi family of BPG Georgian fonts
Version:	3.300
Group:		User Interface/X
Requires:	%{name}-common = %{common_ver}-%{release}

%description -n %{fontname}-ucnobi-fonts
%common_desc

This package contains the Ucnobi font family.

%_font_pkg -n ucnobi -f %{fontconf}-ucnobi.conf "BPG_Ucnobi*.otf"

%prep
%setup -q -c -n %{name}
mkdir -p Docs/
cp %{SOURCE100} %{SOURCE101} Docs/

%build

%install
rm -rf %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0644 -p BPG_Classic_*.otf BPG_Irubaqidze*.otf BPG_Mikhail_Stephan*.otf BPG_Ucnobi*.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-algeti.conf
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-chveulebrivi.conf
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-courier.conf
install -m 0644 -p %{SOURCE4} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-courier-s.conf
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-elite.conf
install -m 0644 -p %{SOURCE6} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-glaho.conf
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ingiri.conf
install -m 0644 -p %{SOURCE8} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nino-medium.conf
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nino-medium-cond.conf
install -m 0644 -p %{SOURCE10} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-medium.conf
install -m 0644 -p %{SOURCE12} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-modern.conf
install -m 0644 -p %{SOURCE13} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-regular.conf
install -m 0644 -p %{SOURCE14} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE15} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-modern.conf
install -m 0644 -p %{SOURCE17} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-excelsior.conf
install -m 0644 -p %{SOURCE18} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-classic.conf
install -m 0644 -p %{SOURCE19} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-excelsior-caps.conf
install -m 0644 -p %{SOURCE20} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-excelsior-condenced.conf
install -m 0644 -p %{SOURCE21} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gorda.conf
install -m 0644 -p %{SOURCE22} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-irubaqidze.conf
install -m 0644 -p %{SOURCE23} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mikhail-stephan.conf
install -m 0644 -p %{SOURCE24} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani.conf
install	-m 0644	-p %{SOURCE25} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mrgvlovani-caps.conf
install -m 0644 -p %{SOURCE26} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nateli.conf
install -m 0644 -p %{SOURCE27} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nateli-caps.conf
install -m 0644 -p %{SOURCE28} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nateli-condenced.conf
install -m 0644 -p %{SOURCE29} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ucnobi.conf
install	-m 0644 -p %{SOURCE30} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dedaena-block.conf
install -m 0644 -p %{SOURCE31} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bpg-dejavu-sans.conf

for fontconf in %{fontconf}-algeti.conf %{fontconf}-chveulebrivi.conf %{fontconf}-courier.conf %{fontconf}-courier-s.conf\
		%{fontconf}-elite.conf %{fontconf}-glaho.conf %{fontconf}-ingiri.conf %{fontconf}-nino-medium.conf\
		%{fontconf}-nino-medium-cond.conf %{fontconf}-sans.conf %{fontconf}-sans-medium.conf %{fontconf}-sans-modern.conf\
		%{fontconf}-sans-regular.conf %{fontconf}-serif.conf %{fontconf}-serif-modern.conf %{fontconf}-excelsior.conf\
		%{fontconf}-classic.conf %{fontconf}-excelsior-caps.conf %{fontconf}-excelsior-condenced.conf \
		%{fontconf}-gorda.conf %{fontconf}-irubaqidze.conf %{fontconf}-mikhail-stephan.conf %{fontconf}-mrgvlovani.conf \
		%{fontconf}-mrgvlovani-caps.conf %{fontconf}-nateli.conf %{fontconf}-nateli-caps.conf %{fontconf}-nateli-condenced.conf \
		%{fontconf}-ucnobi.conf %{fontconf}-dedaena-block.conf %{fontconf}-bpg-dejavu-sans.conf
do
	ln -s %{_fontconfig_templatedir}/$fontconf %{buildroot}%{_fontconfig_confdir}/$fontconf
done

%clean
rm -rf %{buildroot}

%files common
%defattr(0644,root,root,0755)
%doc Docs/*
%dir %{_fontdir}

%changelog
* Thu Jan 31 2013 Tom Callaway <spot@fedoraproject.org> - 20120413-2
- add missing docs

* Fri Sep 14 2012 Tom Callaway <spot@fedoraproject.org> - 20120413-1
- update to the 2012 fonts

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090205-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090205-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090205-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-7
- add Excelsior font

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090205-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-5
- take & out of filename

* Tue Feb 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-4
- missing semicolon in fontconfig files

* Tue Feb 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-3
- fix fontconfig files to not use reserved character, alias for fonts with old names

* Thu Feb 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-2
- update fontconfig files, change priority to 64
- don't need to own fontdir in -common, but we'll leave it in for good measure.

* Thu Feb 5 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090205-1
- update to 20090205 source with proper licensing

* Tue Feb 3 2009 Tom "spot" Callaway <tcallawa@redhat.com> 20090203-1
- Initial package for Fedora
