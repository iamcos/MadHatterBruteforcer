// This provides the frozen (compiled bytecode) files that are included if
// any.
#include <Python.h>

#include "nuitka/constants_blob.h"

// Blob from which modules are unstreamed.
#define stream_data constant_bin

// These modules should be loaded as bytecode. They may e.g. have to be loadable
// during "Py_Initialize" already, or for irrelevance, they are only included
// in this un-optimized form. These are not compiled by Nuitka, and therefore
// are not accelerated at all, merely bundled with the binary or module, so
// that CPython library can start out finding them.

struct frozen_desc {
    char const *name;
    ssize_t start;
    int size;
};

void copyFrozenModulesTo( struct _frozen *destination )
{
    struct frozen_desc frozen_modules[] = {
        { "_collections_abc", 5600485, 28942 },
        { "_compression", 5629427, 4135 },
        { "_weakrefset", 5633562, 7462 },
        { "abc", 5641024, 6458 },
        { "base64", 5647482, 16988 },
        { "bz2", 5664470, 11192 },
        { "codecs", 5675662, 33905 },
        { "collections", 5709567, -46610 },
        { "collections.abc", 5600485, 28942 },
        { "copyreg", 5756177, 4244 },
        { "dis", 5760421, 15216 },
        { "encodings", 5775637, -3954 },
        { "encodings.aliases", 5779591, 6303 },
        { "encodings.ascii", 5785894, 1891 },
        { "encodings.base64_codec", 5787785, 2430 },
        { "encodings.big5", 5790215, 1451 },
        { "encodings.big5hkscs", 5791666, 1461 },
        { "encodings.bz2_codec", 5793127, 3292 },
        { "encodings.charmap", 5796419, 2944 },
        { "encodings.cp037", 5799363, 2436 },
        { "encodings.cp1006", 5801799, 2512 },
        { "encodings.cp1026", 5804311, 2440 },
        { "encodings.cp1125", 5806751, 8133 },
        { "encodings.cp1140", 5814884, 2426 },
        { "encodings.cp1250", 5817310, 2463 },
        { "encodings.cp1251", 5819773, 2460 },
        { "encodings.cp1252", 5822233, 2463 },
        { "encodings.cp1253", 5824696, 2476 },
        { "encodings.cp1254", 5827172, 2465 },
        { "encodings.cp1255", 5829637, 2484 },
        { "encodings.cp1256", 5832121, 2462 },
        { "encodings.cp1257", 5834583, 2470 },
        { "encodings.cp1258", 5837053, 2468 },
        { "encodings.cp273", 5839521, 2422 },
        { "encodings.cp424", 5841943, 2466 },
        { "encodings.cp437", 5844409, 7850 },
        { "encodings.cp500", 5852259, 2436 },
        { "encodings.cp720", 5854695, 2533 },
        { "encodings.cp737", 5857228, 8172 },
        { "encodings.cp775", 5865400, 7880 },
        { "encodings.cp850", 5873280, 7511 },
        { "encodings.cp852", 5880791, 7888 },
        { "encodings.cp855", 5888679, 8141 },
        { "encodings.cp856", 5896820, 2498 },
        { "encodings.cp857", 5899318, 7493 },
        { "encodings.cp858", 5906811, 7481 },
        { "encodings.cp860", 5914292, 7829 },
        { "encodings.cp861", 5922121, 7844 },
        { "encodings.cp862", 5929965, 8033 },
        { "encodings.cp863", 5937998, 7844 },
        { "encodings.cp864", 5945842, 7990 },
        { "encodings.cp865", 5953832, 7844 },
        { "encodings.cp866", 5961676, 8177 },
        { "encodings.cp869", 5969853, 7870 },
        { "encodings.cp874", 5977723, 2564 },
        { "encodings.cp875", 5980287, 2433 },
        { "encodings.cp932", 5982720, 1453 },
        { "encodings.cp949", 5984173, 1453 },
        { "encodings.cp950", 5985626, 1453 },
        { "encodings.euc_jis_2004", 5987079, 1467 },
        { "encodings.euc_jisx0213", 5988546, 1467 },
        { "encodings.euc_jp", 5990013, 1455 },
        { "encodings.euc_kr", 5991468, 1455 },
        { "encodings.gb18030", 5992923, 1457 },
        { "encodings.gb2312", 5994380, 1455 },
        { "encodings.gbk", 5995835, 1449 },
        { "encodings.hex_codec", 5997284, 2417 },
        { "encodings.hp_roman8", 5999701, 2637 },
        { "encodings.hz", 6002338, 1447 },
        { "encodings.idna", 6003785, 5731 },
        { "encodings.iso2022_jp", 6009516, 1468 },
        { "encodings.iso2022_jp_1", 6010984, 1472 },
        { "encodings.iso2022_jp_2", 6012456, 1472 },
        { "encodings.iso2022_jp_2004", 6013928, 1478 },
        { "encodings.iso2022_jp_3", 6015406, 1472 },
        { "encodings.iso2022_jp_ext", 6016878, 1476 },
        { "encodings.iso2022_kr", 6018354, 1468 },
        { "encodings.iso8859_1", 6019822, 2435 },
        { "encodings.iso8859_10", 6022257, 2440 },
        { "encodings.iso8859_11", 6024697, 2534 },
        { "encodings.iso8859_13", 6027231, 2443 },
        { "encodings.iso8859_14", 6029674, 2461 },
        { "encodings.iso8859_15", 6032135, 2440 },
        { "encodings.iso8859_16", 6034575, 2442 },
        { "encodings.iso8859_2", 6037017, 2435 },
        { "encodings.iso8859_3", 6039452, 2442 },
        { "encodings.iso8859_4", 6041894, 2435 },
        { "encodings.iso8859_5", 6044329, 2436 },
        { "encodings.iso8859_6", 6046765, 2480 },
        { "encodings.iso8859_7", 6049245, 2443 },
        { "encodings.iso8859_8", 6051688, 2474 },
        { "encodings.iso8859_9", 6054162, 2435 },
        { "encodings.johab", 6056597, 1453 },
        { "encodings.koi8_r", 6058050, 2487 },
        { "encodings.koi8_t", 6060537, 2398 },
        { "encodings.koi8_u", 6062935, 2473 },
        { "encodings.kz1048", 6065408, 2450 },
        { "encodings.latin_1", 6067858, 1903 },
        { "encodings.mac_arabic", 6069761, 7744 },
        { "encodings.mac_centeuro", 6077505, 2474 },
        { "encodings.mac_croatian", 6079979, 2482 },
        { "encodings.mac_cyrillic", 6082461, 2472 },
        { "encodings.mac_farsi", 6084933, 2416 },
        { "encodings.mac_greek", 6087349, 2456 },
        { "encodings.mac_iceland", 6089805, 2475 },
        { "encodings.mac_latin2", 6092280, 2616 },
        { "encodings.mac_roman", 6094896, 2473 },
        { "encodings.mac_romanian", 6097369, 2483 },
        { "encodings.mac_turkish", 6099852, 2476 },
        { "encodings.palmos", 6102328, 2463 },
        { "encodings.ptcp154", 6104791, 2557 },
        { "encodings.punycode", 6107348, 6424 },
        { "encodings.quopri_codec", 6113772, 2450 },
        { "encodings.raw_unicode_escape", 6116222, 1776 },
        { "encodings.rot_13", 6117998, 3036 },
        { "encodings.shift_jis", 6121034, 1461 },
        { "encodings.shift_jis_2004", 6122495, 1471 },
        { "encodings.shift_jisx0213", 6123966, 1471 },
        { "encodings.tis_620", 6125437, 2525 },
        { "encodings.undefined", 6127962, 2170 },
        { "encodings.unicode_escape", 6130132, 1756 },
        { "encodings.unicode_internal", 6131888, 1766 },
        { "encodings.utf_16", 6133654, 4840 },
        { "encodings.utf_16_be", 6138494, 1641 },
        { "encodings.utf_16_le", 6140135, 1641 },
        { "encodings.utf_32", 6141776, 4733 },
        { "encodings.utf_32_be", 6146509, 1534 },
        { "encodings.utf_32_le", 6148043, 1534 },
        { "encodings.utf_7", 6149577, 1562 },
        { "encodings.utf_8", 6151139, 1621 },
        { "encodings.utf_8_sig", 6152760, 4523 },
        { "encodings.uu_codec", 6157283, 3232 },
        { "encodings.zlib_codec", 6160515, 3130 },
        { "enum", 6163645, 23938 },
        { "functools", 6187583, 23949 },
        { "genericpath", 6211532, 3748 },
        { "heapq", 6215280, 14362 },
        { "importlib", 6229642, -3732 },
        { "importlib._bootstrap", 6233374, 29178 },
        { "importlib._bootstrap_external", 6262552, 41818 },
        { "importlib.machinery", 6304370, 972 },
        { "inspect", 6305342, 79766 },
        { "io", 6385108, 3416 },
        { "keyword", 6388524, 1809 },
        { "linecache", 6390333, 3789 },
        { "locale", 6394122, 34555 },
        { "opcode", 6428677, 5389 },
        { "operator", 6434066, 13900 },
        { "os", 6447966, 29693 },
        { "posixpath", 6477659, 10396 },
        { "quopri", 6488055, 5782 },
        { "re", 6493837, 13804 },
        { "reprlib", 6507641, 5350 },
        { "sre_compile", 6512991, 15203 },
        { "sre_constants", 6528194, 6291 },
        { "sre_parse", 6534485, 21357 },
        { "stat", 6555842, 3873 },
        { "stringprep", 6559715, 10043 },
        { "struct", 6569758, 334 },
        { "threading", 6570092, 37346 },
        { "token", 6607438, 3599 },
        { "tokenize", 6611037, 17831 },
        { "traceback", 6628868, 19634 },
        { "types", 6648502, 8974 },
        { "warnings", 6657476, 13766 },
        { NULL, 0, 0 }
    };

    struct frozen_desc *current = frozen_modules;

    for(;;)
    {
        destination->name = (char *)current->name;
        destination->code = (unsigned char *)&constant_bin[ current->start ];
        destination->size = current->size;

        if (destination->name == NULL) break;

        current += 1;
        destination += 1;
    };
}
