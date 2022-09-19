#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : harfbuzz
Version  : 5.2.0
Release  : 115
URL      : https://github.com/harfbuzz/harfbuzz/archive/refs/tags/5.2.0.tar.gz
Source0  : https://github.com/harfbuzz/harfbuzz/archive/refs/tags/5.2.0.tar.gz
Summary  : HarfBuzz text shaping library
Group    : Development/Tools
License  : Apache-2.0 MIT OFL-1.1
Requires: harfbuzz-bin = %{version}-%{release}
Requires: harfbuzz-data = %{version}-%{release}
Requires: harfbuzz-filemap = %{version}-%{release}
Requires: harfbuzz-lib = %{version}-%{release}
Requires: harfbuzz-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gcc-staticdev
BuildRequires : glibc-staticdev
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : graphite-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(icu-uc)
Patch1: backport-meson.patch

%description
This is HarfBuzz, a text shaping library.

%package bin
Summary: bin components for the harfbuzz package.
Group: Binaries
Requires: harfbuzz-data = %{version}-%{release}
Requires: harfbuzz-license = %{version}-%{release}
Requires: harfbuzz-filemap = %{version}-%{release}

%description bin
bin components for the harfbuzz package.


%package data
Summary: data components for the harfbuzz package.
Group: Data

%description data
data components for the harfbuzz package.


%package dev
Summary: dev components for the harfbuzz package.
Group: Development
Requires: harfbuzz-lib = %{version}-%{release}
Requires: harfbuzz-bin = %{version}-%{release}
Requires: harfbuzz-data = %{version}-%{release}
Provides: harfbuzz-devel = %{version}-%{release}
Requires: harfbuzz = %{version}-%{release}

%description dev
dev components for the harfbuzz package.


%package doc
Summary: doc components for the harfbuzz package.
Group: Documentation

%description doc
doc components for the harfbuzz package.


%package filemap
Summary: filemap components for the harfbuzz package.
Group: Default

%description filemap
filemap components for the harfbuzz package.


%package lib
Summary: lib components for the harfbuzz package.
Group: Libraries
Requires: harfbuzz-data = %{version}-%{release}
Requires: harfbuzz-license = %{version}-%{release}
Requires: harfbuzz-filemap = %{version}-%{release}

%description lib
lib components for the harfbuzz package.


%package license
Summary: license components for the harfbuzz package.
Group: Default

%description license
license components for the harfbuzz package.


%prep
%setup -q -n harfbuzz-5.2.0
cd %{_builddir}/harfbuzz-5.2.0
%patch1 -p1
pushd ..
cp -a harfbuzz-5.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663622250
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgraphite2=enabled  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dgraphite2=enabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/harfbuzz
cp %{_builddir}/harfbuzz-%{version}/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/07f9ad4e387c060c0032e3d02e9ac287ea720785 || :
cp %{_builddir}/harfbuzz-%{version}/src/ms-use/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/689ec0681815ecc32bee639c68e7740add7bd301 || :
cp %{_builddir}/harfbuzz-%{version}/test/shape/data/aots/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/f8c8a69b50f2eb0c11c277dfff1f4c69a014a24a || :
cp %{_builddir}/harfbuzz-%{version}/test/shape/data/in-house/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/6ee2d8efdf85d9dba10ec1d9f4fb821baf2db4f4 || :
cp %{_builddir}/harfbuzz-%{version}/test/shape/data/text-rendering-tests/COPYING %{buildroot}/usr/share/package-licenses/harfbuzz/2f52d0b1bf8ddf82117ba37aefc4d5945392c005 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hb-ot-shape-closure
/usr/bin/hb-shape
/usr/bin/hb-subset
/usr/bin/hb-view
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/HarfBuzz-0.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/harfbuzz/hb-aat-layout.h
/usr/include/harfbuzz/hb-aat.h
/usr/include/harfbuzz/hb-blob.h
/usr/include/harfbuzz/hb-buffer.h
/usr/include/harfbuzz/hb-common.h
/usr/include/harfbuzz/hb-cplusplus.hh
/usr/include/harfbuzz/hb-deprecated.h
/usr/include/harfbuzz/hb-draw.h
/usr/include/harfbuzz/hb-face.h
/usr/include/harfbuzz/hb-font.h
/usr/include/harfbuzz/hb-ft.h
/usr/include/harfbuzz/hb-glib.h
/usr/include/harfbuzz/hb-gobject-enums.h
/usr/include/harfbuzz/hb-gobject-structs.h
/usr/include/harfbuzz/hb-gobject.h
/usr/include/harfbuzz/hb-graphite2.h
/usr/include/harfbuzz/hb-icu.h
/usr/include/harfbuzz/hb-map.h
/usr/include/harfbuzz/hb-ot-color.h
/usr/include/harfbuzz/hb-ot-deprecated.h
/usr/include/harfbuzz/hb-ot-font.h
/usr/include/harfbuzz/hb-ot-layout.h
/usr/include/harfbuzz/hb-ot-math.h
/usr/include/harfbuzz/hb-ot-meta.h
/usr/include/harfbuzz/hb-ot-metrics.h
/usr/include/harfbuzz/hb-ot-name.h
/usr/include/harfbuzz/hb-ot-shape.h
/usr/include/harfbuzz/hb-ot-var.h
/usr/include/harfbuzz/hb-ot.h
/usr/include/harfbuzz/hb-set.h
/usr/include/harfbuzz/hb-shape-plan.h
/usr/include/harfbuzz/hb-shape.h
/usr/include/harfbuzz/hb-style.h
/usr/include/harfbuzz/hb-subset-repacker.h
/usr/include/harfbuzz/hb-subset.h
/usr/include/harfbuzz/hb-unicode.h
/usr/include/harfbuzz/hb-version.h
/usr/include/harfbuzz/hb.h
/usr/lib64/cmake/harfbuzz/harfbuzz-config.cmake
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-gobject.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-icu.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-subset.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz.so
/usr/lib64/libharfbuzz-gobject.so
/usr/lib64/libharfbuzz-icu.so
/usr/lib64/libharfbuzz-subset.so
/usr/lib64/libharfbuzz.so
/usr/lib64/pkgconfig/harfbuzz-gobject.pc
/usr/lib64/pkgconfig/harfbuzz-icu.pc
/usr/lib64/pkgconfig/harfbuzz-subset.pc
/usr/lib64/pkgconfig/harfbuzz.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.png
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.svg
/usr/share/gtk-doc/html/harfbuzz/a-clustering-example-for-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/a-simple-shaping-example.html
/usr/share/gtk-doc/html/harfbuzz/aat-shaping.html
/usr/share/gtk-doc/html/harfbuzz/adding-text-to-the-buffer.html
/usr/share/gtk-doc/html/harfbuzz/annotation-glossary.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-6-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-10.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-11.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-20.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-21.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-22.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-26.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-28.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-30.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-31.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-33.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-38.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-39.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-41.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-42.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-7.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-8.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-0-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-1-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-1-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-2-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-3-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-5-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-6-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-7-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-7-7.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-1.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-8-6.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-9-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-0-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-1-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-2-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-3-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-4-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-5-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-6-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-6-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-6-5.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-6-8.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-7-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-8-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-9-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-2-9-1.html
/usr/share/gtk-doc/html/harfbuzz/api-index-3-0-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-3-1-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-3-3-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-3-4-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-4-0-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-4-1-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-4-2-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-4-3-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-4-4-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-5-0-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-full.html
/usr/share/gtk-doc/html/harfbuzz/apple-advanced-typography-api.html
/usr/share/gtk-doc/html/harfbuzz/buffers-language-script-and-direction.html
/usr/share/gtk-doc/html/harfbuzz/building.html
/usr/share/gtk-doc/html/harfbuzz/clusters.html
/usr/share/gtk-doc/html/harfbuzz/core-api.html
/usr/share/gtk-doc/html/harfbuzz/customizing-unicode-functions.html
/usr/share/gtk-doc/html/harfbuzz/deprecated-api-index.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces-custom-functions.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces-native-opentype.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces-variable.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces.html
/usr/share/gtk-doc/html/harfbuzz/getting-started.html
/usr/share/gtk-doc/html/harfbuzz/graphite-shaping.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-aat-layout.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-blob.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-buffer.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-common.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-coretext.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-deprecated.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-directwrite.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-draw.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-face.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ft.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-gdi.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-glib.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-graphite2.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-icu.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-map.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-color.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-layout.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-math.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-meta.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-metrics.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-name.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-shape.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-var.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-set.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-shape-plan.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-shape.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-style.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-subset.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-unicode.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-uniscribe.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-version.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz.devhelp2
/usr/share/gtk-doc/html/harfbuzz/home.png
/usr/share/gtk-doc/html/harfbuzz/index.html
/usr/share/gtk-doc/html/harfbuzz/install-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/integration-api.html
/usr/share/gtk-doc/html/harfbuzz/integration-coretext.html
/usr/share/gtk-doc/html/harfbuzz/integration-freetype.html
/usr/share/gtk-doc/html/harfbuzz/integration-icu.html
/usr/share/gtk-doc/html/harfbuzz/integration-python.html
/usr/share/gtk-doc/html/harfbuzz/integration-uniscribe.html
/usr/share/gtk-doc/html/harfbuzz/integration.html
/usr/share/gtk-doc/html/harfbuzz/left-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/left.png
/usr/share/gtk-doc/html/harfbuzz/level-2.html
/usr/share/gtk-doc/html/harfbuzz/object-model-blobs.html
/usr/share/gtk-doc/html/harfbuzz/object-model-lifecycle.html
/usr/share/gtk-doc/html/harfbuzz/object-model-object-types.html
/usr/share/gtk-doc/html/harfbuzz/object-model-user-data.html
/usr/share/gtk-doc/html/harfbuzz/object-model.html
/usr/share/gtk-doc/html/harfbuzz/opentype-api.html
/usr/share/gtk-doc/html/harfbuzz/opentype-shaping-models.html
/usr/share/gtk-doc/html/harfbuzz/reference-manual.html
/usr/share/gtk-doc/html/harfbuzz/reordering-in-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/right-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/right.png
/usr/share/gtk-doc/html/harfbuzz/script-specific-shaping.html
/usr/share/gtk-doc/html/harfbuzz/setting-buffer-properties.html
/usr/share/gtk-doc/html/harfbuzz/shaping-and-shape-plans.html
/usr/share/gtk-doc/html/harfbuzz/shaping-concepts.html
/usr/share/gtk-doc/html/harfbuzz/shaping-opentype-features.html
/usr/share/gtk-doc/html/harfbuzz/shaping-operations.html
/usr/share/gtk-doc/html/harfbuzz/shaping-plans-and-caching.html
/usr/share/gtk-doc/html/harfbuzz/shaping-shaper-selection.html
/usr/share/gtk-doc/html/harfbuzz/style-api.html
/usr/share/gtk-doc/html/harfbuzz/style.css
/usr/share/gtk-doc/html/harfbuzz/subset-api.html
/usr/share/gtk-doc/html/harfbuzz/terminology.html
/usr/share/gtk-doc/html/harfbuzz/text-runs.html
/usr/share/gtk-doc/html/harfbuzz/the-distinction-between-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/unicode-character-categories.html
/usr/share/gtk-doc/html/harfbuzz/up-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/up.png
/usr/share/gtk-doc/html/harfbuzz/user-manual.html
/usr/share/gtk-doc/html/harfbuzz/utilities-common-types-apis.html
/usr/share/gtk-doc/html/harfbuzz/utilities.html
/usr/share/gtk-doc/html/harfbuzz/what-does-harfbuzz-do.html
/usr/share/gtk-doc/html/harfbuzz/what-harfbuzz-doesnt-do.html
/usr/share/gtk-doc/html/harfbuzz/what-is-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/why-do-i-need-a-shaping-engine.html
/usr/share/gtk-doc/html/harfbuzz/why-is-it-called-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/working-with-harfbuzz-clusters.html

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-harfbuzz

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-gobject.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-gobject.so.0.50200.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-icu.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-icu.so.0.50200.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-subset.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz-subset.so.0.50200.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libharfbuzz.so.0.50200.0
/usr/lib64/libharfbuzz-gobject.so.0
/usr/lib64/libharfbuzz-gobject.so.0.50200.0
/usr/lib64/libharfbuzz-icu.so.0
/usr/lib64/libharfbuzz-icu.so.0.50200.0
/usr/lib64/libharfbuzz-subset.so.0
/usr/lib64/libharfbuzz-subset.so.0.50200.0
/usr/lib64/libharfbuzz.so.0
/usr/lib64/libharfbuzz.so.0.50200.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/harfbuzz/07f9ad4e387c060c0032e3d02e9ac287ea720785
/usr/share/package-licenses/harfbuzz/2f52d0b1bf8ddf82117ba37aefc4d5945392c005
/usr/share/package-licenses/harfbuzz/689ec0681815ecc32bee639c68e7740add7bd301
/usr/share/package-licenses/harfbuzz/6ee2d8efdf85d9dba10ec1d9f4fb821baf2db4f4
/usr/share/package-licenses/harfbuzz/f8c8a69b50f2eb0c11c277dfff1f4c69a014a24a
