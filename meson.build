project('adns', 'c', version: '1.5.0')

src_dir = include_directories('src')
client_dir = include_directories('client')
regress_dir = include_directories('regress')

# Static

sources = [
    'src/types.c',
    'src/event.c',
    'src/query.c',
    'src/reply.c',
    'src/general.c',
    'src/setup.c',
    'src/transmit.c',
    'src/parse.c',
    'src/poll.c',
    'src/check.c',
    'src/addrfam.c',
]

libadns = static_library('adns', sources,
        include_directories: src_dir,
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

# Dynamic

libadns_so = shared_library('adns', sources,
        include_directories: src_dir,
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-fpic',
        ],
    )

# Client

## Static

executable('adnslogres_s', [
            'client/adnslogres.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('adnsheloex_s', [
            'client/adnsheloex.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('adnshost_s', [
            'client/adh-main.c',
            'client/adh-opts.c',
            'client/adh-query.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('adnsresfilter_s', [
            'client/adnsresfilter.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('fanftest_s', [
            'client/fanftest.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('adnstest_s', [
            'client/adnstest.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('addrtext_s', [
            'client/addrtext.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

## Shared

executable('adnslogres', [
            'client/adnslogres.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns_so ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('adnsheloex', [
            'client/adnsheloex.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns_so ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('adnshost', [
            'client/adh-main.c',
            'client/adh-opts.c',
            'client/adh-query.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns_so ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

executable('adnsresfilter', [
            'client/adnsresfilter.c',
        ],
        include_directories: [ src_dir, client_dir ],
        link_with: [ libadns_so ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign',
        ],
    )

# Regress

executable('adnstest_record', [
            'regress/hrecord.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
            'client/adnstest.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )

executable('adnshost_record', [
            'client/adh-main.c',
            'client/adh-opts.c',
            'client/adh-query.c',
            'regress/hrecord.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )

executable('adnslogres_record', [
            'client/adnslogres.c',
            'regress/hrecord.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )


executable('adnsresfilter_record', [
            'client/adnsresfilter.c',
            'regress/hrecord.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )


executable('adnstest_playback', [
            'client/adnstest.c',
            'regress/hplayback.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )

executable('adnshost_playback', [
            'client/adh-main.c',
            'client/adh-opts.c',
            'client/adh-query.c',
            'regress/hplayback.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )

executable('adnslogres_playback', [
            'client/adnslogres.c',
            'regress/hplayback.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )

executable('adnsresfilter_playback', [
            'client/adnsresfilter.c',
            'regress/hplayback.c',
            'regress/hcommon.c',
            'src/types.c',
            'src/event.c',
            'src/query.c',
            'src/reply.c',
            'src/general.c',
            'src/setup.c',
            'src/transmit.c',
            'src/parse.c',
            'src/poll.c',
            'src/check.c',
            'src/addrfam.c',
        ],
        include_directories: [ src_dir, regress_dir ],
        c_args: [
            '-g', '-O2', '-Wall', '-Wmissing-prototypes', '-Wwrite-strings', '-Wstrict-prototypes', '-Wcast-qual', '-Wpointer-arith', '-Wno-pointer-sign', '-DADNS_REGRESS_TEST',
        ],
    )

