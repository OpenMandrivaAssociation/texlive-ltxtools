# revision 24148
# category Package
# catalog-ctan /macros/latex/contrib/ltxtools
# catalog-date 2011-09-29 18:14:46 +0200
# catalog-license lppl1.3
# catalog-version 0.0.1
Name:		texlive-ltxtools
Version:	0.0.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3

%description
This is a preliminary release of a bundle of macros that the
author uses in the coding of others of his macro bundles.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools.sty
%doc %{_texmfdistdir}/doc/latex/ltxtools/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
