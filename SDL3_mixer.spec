%define		apiver    3
%define		major     0
%define		libname   %mklibname SDL%{apiver}_mixer %{major}
%define		develname %mklibname SDL%{apiver}_mixer -d

Summary:		Simple DirectMedia Layer 3 - mixer
Name:		SDL3_mixer
Version:		3.2.4
Release:		1
License:		zlib
Group:	System/Libraries
Url:		https://github.com/libsdl-org/SDL_mixer
Source0:	https://github.com/libsdl-org/SDL_mixer/releases/download/release-%{version}/%{name}-%{version}.tar.gz
BuildRequires:		cmake
BuildRequires:		make
BuildRequires:		perl
BuildRequires:		pkgconfig(flac)
BuildRequires:		pkgconfig(fluidsynth) >= 2.2.0
BuildRequires:		pkgconfig(libgme)
BuildRequires:		pkgconfig(libmpg123)
BuildRequires:		pkgconfig(libxmp)
BuildRequires:		pkgconfig(opusfile)
BuildRequires:		pkgconfig(sdl3) >= 3.4.0
BuildRequires:		pkgconfig(vorbis)
BuildRequires:		pkgconfig(wavpack)

%description
This is an audio management library. It provides decoding of many popular
audio file formats, mixing, various DSP processing effects and positional
audio. Audio data can be preloaded, or streamed on-the-fly into the
multichannel audio mixer.
It supports four channels of 16-bit stereo audio, plus a single channel of
music, mixed by the MikMod MOD, Timidity MIDI, and mpg123 MP3 libraries.

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:		Simple DirectMedia Layer 3 - Sound mixer library
Group:	System/Libraries

%description -n %{libname}
This is an audio management library. It provides decoding of many popular
audio file formats, mixing, various DSP processing effects and positional
audio. Audio data can be preloaded, or streamed on-the-fly into the
multichannel audio mixer.
It supports four channels of 16-bit stereo audio, plus a single channel of
music, mixed by the MikMod MOD, Timidity MIDI, and mpg123 MP3 libraries.

%files -n %{libname}
%license LICENSE.txt
%doc README.md
%{_libdir}/libSDL%{apiver}_mixer.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{develname}
Summary:		 Headers for developing programs using %{name}
Group:	Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the files needed to develop applications which will use
%{name}.

%files -n %{develname}
%doc README.md
%{_libdir}/libSDL%{apiver}_mixer.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/sdl%{apiver}-mixer.pc
%{_libdir}/cmake/%{name}/
%{_mandir}/man3/MIX*.3*
%{_mandir}/man3/SDL_MIXER*.3*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake \
        -DSDLMIXER_STRICT:BOOL=ON            \
        -DSDLMIXER_WERROR:BOOL=ON            \
        -DSDLMIXER_INSTALL_MAN:BOOL=ON       \
        -DSDLMIXER_EXAMPLES_INSTALL:BOOL=OFF \
        -DSDLMIXER_TESTS_INSTALL:BOOL=OFF    \
        -DSDLMIXER_VORBIS_STB:BOOL=OFF       \
        -DSDLMIXER_VORBIS_VORBISFILE:BOOL=ON \
        -DSDLMIXER_VORBIS_TREMOR:BOOL=OFF    \
        -DSDLMIXER_FLAC_LIBFLAC:BOOL=ON      \
        -DSDLMIXER_FLAC_DRFLAC:BOOL=OFF      \
        -DSDLMIXER_MP3_MPG123:BOOL=ON        \
        -DSDLMIXER_MP3_DRMP3:BOOL=OFF        \
        -DSDLMIXER_DEPS_SHARED:BOOL=OFF

%make_build


%install
%make_install -C build

# We pick it with our macro
rm -rf %{buildroot}%{_datadir}/licenses/SDL3_mixer/LICENSE.txt
