Name:		texlive-ltxtools
Version:	24897
Release:	2
Summary:	A collection of LaTeX API macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ltxtools
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxtools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxtools.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
