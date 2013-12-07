# revision 27323
# category Package
# catalog-ctan /macros/latex/contrib/nestquot
# catalog-date 2012-06-06 18:43:10 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-nestquot
Version:	20120606
Release:	5
Summary:	Alternate quotes between double and single with nesting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nestquot
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nestquot.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Mon Aug 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120606-1
+ Revision: 814495
- Import texlive-nestquot
- Import texlive-nestquot

