# revision 24897
# category Package
# catalog-ctan /macros/latex/contrib/ltxtools
# catalog-date 2011-12-19 23:56:31 +0100
# catalog-license lppl1.3
# catalog-version 0.0.1a
Name:		texlive-ltxtools
Version:	0.0.1a
Release:	3
Summary:	A collection of LaTeX API macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxtools
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxtools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxtools.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a bundle of macros that the author uses in the coding
of others of his macro files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-base.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-doc.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-environ.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-incluput.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-index.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-review.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-trace.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools.sty
%doc %{_texmfdistdir}/doc/latex/ltxtools/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.0.1a-2
+ Revision: 753578
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.0.1a-1
+ Revision: 745300
- texlive-ltxtools

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.0.1-1
+ Revision: 718917
- texlive-ltxtools
- texlive-ltxtools
- texlive-ltxtools
- texlive-ltxtools

