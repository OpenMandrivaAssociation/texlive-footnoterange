Name:		texlive-footnoterange
Version:	52910
Release:	2
Summary:	References to ranges of footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/footnoterange
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides environments footnoterange and
footnoterange*. Multiple footnotes inside these environments
are not referenced as (e.g.) "1 2 3 4" but as "1-4", i.e., the
range (from first to last referred footnote at that place) is
given. If hyperref package and use of its hyperfootnotes-option
the references are hyperlinked. (References to footnotes in the
footnoterange* environment are never hyperlinked.).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/footnoterange
%doc %{_texmfdistdir}/doc/latex/footnoterange
#- source
%doc %{_texmfdistdir}/source/latex/footnoterange

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
