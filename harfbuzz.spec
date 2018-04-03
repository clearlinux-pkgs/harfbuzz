#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : harfbuzz
Version  : 1.7.5
Release  : 59
URL      : https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-1.7.5.tar.bz2
Source0  : https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-1.7.5.tar.bz2
Summary  : HarfBuzz text shaping library
Group    : Development/Tools
License  : Apache-2.0 HPND MIT OFL-1.1
Requires: harfbuzz-bin
Requires: harfbuzz-lib
Requires: harfbuzz-doc
BuildRequires : cmake
BuildRequires : docbook-xml
BuildRequires : freetype-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32cairo)
BuildRequires : pkgconfig(32cairo-ft)
BuildRequires : pkgconfig(32fontconfig)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gobject-2.0)
BuildRequires : pkgconfig(32icu-uc)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-ft)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(icu-uc)

%description
This is HarfBuzz, a text shaping library.

%package bin
Summary: bin components for the harfbuzz package.
Group: Binaries

%description bin
bin components for the harfbuzz package.


%package dev
Summary: dev components for the harfbuzz package.
Group: Development
Requires: harfbuzz-lib
Requires: harfbuzz-bin
Provides: harfbuzz-devel

%description dev
dev components for the harfbuzz package.


%package dev32
Summary: dev32 components for the harfbuzz package.
Group: Default
Requires: harfbuzz-lib32
Requires: harfbuzz-bin
Requires: harfbuzz-dev

%description dev32
dev32 components for the harfbuzz package.


%package doc
Summary: doc components for the harfbuzz package.
Group: Documentation

%description doc
doc components for the harfbuzz package.


%package lib
Summary: lib components for the harfbuzz package.
Group: Libraries

%description lib
lib components for the harfbuzz package.


%package lib32
Summary: lib32 components for the harfbuzz package.
Group: Default

%description lib32
lib32 components for the harfbuzz package.


%prep
%setup -q -n harfbuzz-1.7.5
pushd ..
cp -a harfbuzz-1.7.5 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522776750
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --with-icu=yes --with-glib --with-freetype --with-cairo --with-icu --enable-introspection
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --with-icu=yes --with-glib --with-freetype --with-cairo --with-icu --enable-introspection   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1522776750
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hb-ot-shape-closure
/usr/bin/hb-shape
/usr/bin/hb-view

%files dev
%defattr(-,root,root,-)
/usr/include/harfbuzz/hb-blob.h
/usr/include/harfbuzz/hb-buffer.h
/usr/include/harfbuzz/hb-common.h
/usr/include/harfbuzz/hb-deprecated.h
/usr/include/harfbuzz/hb-face.h
/usr/include/harfbuzz/hb-font.h
/usr/include/harfbuzz/hb-ft.h
/usr/include/harfbuzz/hb-glib.h
/usr/include/harfbuzz/hb-icu.h
/usr/include/harfbuzz/hb-ot-font.h
/usr/include/harfbuzz/hb-ot-layout.h
/usr/include/harfbuzz/hb-ot-math.h
/usr/include/harfbuzz/hb-ot-shape.h
/usr/include/harfbuzz/hb-ot-tag.h
/usr/include/harfbuzz/hb-ot-var.h
/usr/include/harfbuzz/hb-ot.h
/usr/include/harfbuzz/hb-set.h
/usr/include/harfbuzz/hb-shape-plan.h
/usr/include/harfbuzz/hb-shape.h
/usr/include/harfbuzz/hb-unicode.h
/usr/include/harfbuzz/hb-version.h
/usr/include/harfbuzz/hb.h
/usr/lib64/libharfbuzz-icu.so
/usr/lib64/libharfbuzz.so
/usr/lib64/pkgconfig/harfbuzz-icu.pc
/usr/lib64/pkgconfig/harfbuzz.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libharfbuzz-icu.so
/usr/lib32/libharfbuzz.so
/usr/lib32/pkgconfig/32harfbuzz-icu.pc
/usr/lib32/pkgconfig/32harfbuzz.pc
/usr/lib32/pkgconfig/harfbuzz-icu.pc
/usr/lib32/pkgconfig/harfbuzz.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.png
/usr/share/gtk-doc/html/harfbuzz/HarfBuzz.svg
/usr/share/gtk-doc/html/harfbuzz/a-clustering-example-for-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/adding-text-to-the-buffer.html
/usr/share/gtk-doc/html/harfbuzz/annotation-glossary.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-10.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-11.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-20.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-22.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-28.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-30.html
/usr/share/gtk-doc/html/harfbuzz/api-index-0-9-31.html
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
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-2.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-4-3.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-5-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-1-6-0.html
/usr/share/gtk-doc/html/harfbuzz/api-index-full.html
/usr/share/gtk-doc/html/harfbuzz/buffers-language-script-and-direction.html
/usr/share/gtk-doc/html/harfbuzz/building.html
/usr/share/gtk-doc/html/harfbuzz/ch08.html
/usr/share/gtk-doc/html/harfbuzz/clusters.html
/usr/share/gtk-doc/html/harfbuzz/customizing-unicode-functions.html
/usr/share/gtk-doc/html/harfbuzz/deprecated-api-index.html
/usr/share/gtk-doc/html/harfbuzz/fonts-and-faces.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-Buffers.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-Shaping.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-blob.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-common.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-coretext.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-deprecated.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-face.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ft.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-glib.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-gobject.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-graphite2.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-icu.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-font.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-layout.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-math.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-shape.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot-tag.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-ot.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-set.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-shape-plan.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-unicode.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-uniscribe.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb-version.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz-hb.html
/usr/share/gtk-doc/html/harfbuzz/harfbuzz.devhelp2
/usr/share/gtk-doc/html/harfbuzz/hello-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/home.png
/usr/share/gtk-doc/html/harfbuzz/index.html
/usr/share/gtk-doc/html/harfbuzz/install-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/left-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/left.png
/usr/share/gtk-doc/html/harfbuzz/level-2.html
/usr/share/gtk-doc/html/harfbuzz/object-tree.html
/usr/share/gtk-doc/html/harfbuzz/plans-and-caching.html
/usr/share/gtk-doc/html/harfbuzz/pt01.html
/usr/share/gtk-doc/html/harfbuzz/pt02.html
/usr/share/gtk-doc/html/harfbuzz/reordering-in-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/right-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/right.png
/usr/share/gtk-doc/html/harfbuzz/setting-buffer-properties.html
/usr/share/gtk-doc/html/harfbuzz/shaping-and-shape-plans.html
/usr/share/gtk-doc/html/harfbuzz/style.css
/usr/share/gtk-doc/html/harfbuzz/the-distinction-between-levels-0-and-1.html
/usr/share/gtk-doc/html/harfbuzz/up-insensitive.png
/usr/share/gtk-doc/html/harfbuzz/up.png
/usr/share/gtk-doc/html/harfbuzz/using-harfbuzzs-native-opentype-implementation.html
/usr/share/gtk-doc/html/harfbuzz/using-your-own-font-functions.html
/usr/share/gtk-doc/html/harfbuzz/what-about-the-other-scripts.html
/usr/share/gtk-doc/html/harfbuzz/what-is-harfbuzz.html
/usr/share/gtk-doc/html/harfbuzz/why-is-it-called-harfbuzz.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libharfbuzz-icu.so.0
/usr/lib64/libharfbuzz-icu.so.0.10705.0
/usr/lib64/libharfbuzz.so.0
/usr/lib64/libharfbuzz.so.0.10705.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libharfbuzz-icu.so.0
/usr/lib32/libharfbuzz-icu.so.0.10705.0
/usr/lib32/libharfbuzz.so.0
/usr/lib32/libharfbuzz.so.0.10705.0
