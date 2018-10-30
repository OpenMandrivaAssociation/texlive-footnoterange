# revision 25430
# category Package
# catalog-ctan /macros/latex/contrib/footnoterange
# catalog-date 2012-02-19 15:01:00 +0100
# catalog-license lppl1.3
# catalog-version 1.0a
Name:		texlive-footnoterange
Version:	1.0a
Release:	11
Summary:	References to ranges of footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/footnoterange
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnoterange.source.tar.xz
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
%{_texmfdistdir}/tex/latex/footnoterange/footnoterange.sty
%doc %{_texmfdistdir}/doc/latex/footnoterange/README
%doc %{_texmfdistdir}/doc/latex/footnoterange/footnoterange-example.pdf
%doc %{_texmfdistdir}/doc/latex/footnoterange/footnoterange-example.tex
%doc %{_texmfdistdir}/doc/latex/footnoterange/footnoterange.pdf
#- source
%doc %{_texmfdistdir}/source/latex/footnoterange/footnoterange.drv
%doc %{_texmfdistdir}/source/latex/footnoterange/footnoterange.dtx
%doc %{_texmfdistdir}/source/latex/footnoterange/footnoterange.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 779741
- Import texlive-footnoterange
- Import texlive-footnoterange

