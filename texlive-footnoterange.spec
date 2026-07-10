%global tl_name footnoterange
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1c
Release:	%{tl_revision}.1
Summary:	References to ranges of footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footnoterange
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the environments footnoterange and footnoterange*.
Multiple footnotes inside these environments are not referenced as
(e.g.) "1 2 3" but as "1-3", i.e., the range (from first to last
referred footnote at that place) is given. If the hyperref package is
loaded with enabled hyperfootnotes-option, then the references are
hyperlinked. (References to footnotes in footnoterange* environments are
never hyperlinked.)

