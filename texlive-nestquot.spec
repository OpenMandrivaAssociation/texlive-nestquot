Name:		texlive-nestquot
Version:	27323
Release:	1
Summary:	Alternate quotes between double and single with nesting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nestquot
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nestquot.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides two new commands: \nlq and \nrq for nesting left and
right quotes that properly change between double and single
quotes according to their nesting level. For example, the input
\nlq Foo \nlq bar\nrq\ bletch\nrq will be typeset as if it had
been entered as "Foo 'bar' bletch".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nestquot/nestquot.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
