# revision 17556
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-dbicons
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license lppl
# catalog-version 0.16
Name:		texlive-pst-dbicons
Version:	0.16
Release:	12
Summary:	Support for drawing ER diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-dbicons
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-dbicons.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-dbicons.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-dbicons.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides some useful macros in the database area.
The package focusses on typesetting ER-Diagrams in a
declarative style, i.e., by positioning some nodes and defining
the position of all other nodes relative to them by using the
standard database terminology. The PSTricks package is required
for using pst-dbicons, but no deep knowledge of PSTricks
commands is required (although such knowledge is useful for
exploiting the full functionality of the package).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-dbicons/pst-dbicons.sty
%doc %{_texmfdistdir}/doc/generic/pst-dbicons/README
%doc %{_texmfdistdir}/doc/generic/pst-dbicons/mondial-ER.tex
%doc %{_texmfdistdir}/doc/generic/pst-dbicons/pst-dbicons.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-dbicons/pst-dbicons.drv
%doc %{_texmfdistdir}/source/generic/pst-dbicons/pst-dbicons.dtx
%doc %{_texmfdistdir}/source/generic/pst-dbicons/pst-dbicons.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.16-2
+ Revision: 755230
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.16-1
+ Revision: 719342
- texlive-pst-dbicons
- texlive-pst-dbicons
- texlive-pst-dbicons
- texlive-pst-dbicons

