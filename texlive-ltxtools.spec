%global tl_name ltxtools
%global tl_revision 24897

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1a
Release:	%{tl_revision}.1
Summary:	A collection of LaTeX API macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ltxtools
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxtools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxtools.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a bundle of macros that the author uses in the coding of others
of his macro files.

