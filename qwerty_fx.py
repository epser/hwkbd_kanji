
from consts import *

REMAP_FX_TO_RALT = r"""
# Remap FxTec Home Key
map key 172 ALT_RIGHT
"""

REMAP_FX_TO_LMETA = r"""
# Remap FxTec Home Key and Meta binding
map key 172 META_LEFT
map key 75 SLASH
"""

REPLACE_FX_QWERTY = [
    {
        REPL_KEYCODE: "1",
        REPLACE: [
            (RALT, r"replace F1"),
        ]
    },
    {
        REPL_KEYCODE: "2",
        REPLACE: [
            (RALT, r"replace F2"),
        ]
    },
    {
        REPL_KEYCODE: "3",
        REPLACE: [
            (RALT, r"replace F3"),
        ]
    },
    {
        REPL_KEYCODE: "4",
        REPLACE: [
            (RALT, r"replace F4"),
        ]
    },
    {
        REPL_KEYCODE: "5",
        REPLACE: [
            (RALT, r"replace F5"),
        ]
    },
    {
        REPL_KEYCODE: "6",
        REPLACE: [
            (RALT, r"replace F6"),
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            (RALT, r"replace F7"),
        ]
    },
    {
        REPL_KEYCODE: "8",
        REPLACE: [
            (RALT, r"replace F8"),
        ]
    },
    {
        REPL_KEYCODE: "9",
        REPLACE: [
            (RALT, r"replace F9"),
        ]
    },
    {
        REPL_KEYCODE: "0",
        REPLACE: [
            (RALT, r"replace F10"),
        ]
    },
    {
        REPL_KEYCODE: "MINUS",
        REPLACE: [
            (RALT, r"replace F11"),
        ]
    },
    {
        REPL_KEYCODE: "EQUALS",
        REPLACE: [
            (RALT, r"replace F12"),
        ]
    },
    # ROW 2 ###############################################################
    {    
        REPL_KEYCODE: "TAB",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPLACE: [
            (RALT, r"'\u0303'"), # ~ dead key
        ]
    },
    {
        REPL_KEYCODE: "Q",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "W",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "E",
        REPLACE: [
            (RALT, r"replace ENVELOPE"),
        ]
    },
    {
        REPL_KEYCODE: "R",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "T",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "Y",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "U",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "I",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "O",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "P",
        REPLACE: [
            (RALT, r"replace CONTACTS"),
        ]
    },
    {
        REPL_KEYCODE: "SEMICOLON",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    # ROW 3 ###############################################################
    {    
        REPL_KEYCODE: "BACKSLASH",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "A",
        REPLACE: [
            (RALT, r"replace CALENDAR"),
        ]
    },
    {
        REPL_KEYCODE: "S",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "D",
        REPLACE: [
            (RALT, r"replace HOME"),
        ]
    },
    {
        REPL_KEYCODE: "F",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "G",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "H",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "J",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "K",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "L",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "SLASH", # APOS
        REPLACE: [
            (BASE, r"','"),
            (SHIFT, r"'\"'"),
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "ENTER",
        REPLACE: [
            (RALT, r"replace MEDIA_PLAY_PAUSE"),
        ]
    },
    # ROW 4 ###############################################################
    {    
        REPL_KEYCODE: "LEFT_BRACKET",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "RIGHT_BRACKET",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "Z",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "C",
        REPLACE: [
            (RALT, r"replace CALCULATOR"),
        ]
    },
    {
        REPL_KEYCODE: "V",
        REPLACE: [
            (RALT, r"replace VOICE_ASSIST"),
        ]
    },
    {
        REPL_KEYCODE: "B",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "N",
        REPLACE: [
            (RALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "M",
        REPLACE: [
            (RALT, r"replace MUSIC"),
        ]
    },
    {
        REPL_KEYCODE: "COMMA",
        REPLACE: [
            (RALT, r"replace MEDIA_REWIND"),
        ]
    },
    {
        REPL_KEYCODE: "PERIOD",
        REPLACE: [
            (RALT, r"replace MEDIA_FAST_FORWARD"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_UP",
        REPLACE: [
            (RALT, r"replace VOLUME_UP"),
        ]
    },
    # ROW 5 ###############################################################
    {    
        REPL_KEYCODE: "ZENKAKU_HANKAKU", #SYM
        REPLACE: [
            (RALT, r"replace POWER"),
            (LALT, r"replace POWER"), #Normal ALT
        ]
    },    
    {    
        REPL_KEYCODE: "SPACE",
        REPLACE: [
            # Fx + SPACE launch Web Browser
            (RALT, r"replace EXPLORER"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_LEFT",
        REPLACE: [
            (RALT, r"replace MEDIA_PREVIOUS"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_DOWN",
        REPLACE: [
            (RALT, r"replace VOLUME_DOWN"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_RIGHT",
        REPLACE: [
            (RALT, r"replace MEDIA_NEXT"),
        ]
    }
]

REPLACE_FX_META_QWERTY = [
    {
        REPL_KEYCODE: "1",
        REPLACE: [
            (FN_CTRL, r"replace F1"),
        ]
    },
    {
        REPL_KEYCODE: "2",
        REPLACE: [
            (FN_CTRL, r"replace F2"),
        ]
    },
    {
        REPL_KEYCODE: "3",
        REPLACE: [
            (FN_CTRL, r"replace F3"),
        ]
    },
    {
        REPL_KEYCODE: "4",
        REPLACE: [
            (FN_CTRL, r"replace F4"),
        ]
    },
    {
        REPL_KEYCODE: "5",
        REPLACE: [
            (LMETA, r"replace F5"),
            (FN_CTRL, r"replace F5"),
        ]
    },
    {
        REPL_KEYCODE: "6",
        REPLACE: [
            (LMETA, r"replace F6"),
            (FN_CTRL, r"replace F6"),
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            (FN_CTRL, r"replace F7"),
        ]
    },
    {
        REPL_KEYCODE: "8",
        REPLACE: [
            (FN_CTRL, r"replace F8"),
        ]
    },
    {
        REPL_KEYCODE: "9",
        REPLACE: [
            (FN_CTRL, r"replace F9"),
        ]
    },
    {
        REPL_KEYCODE: "0",
        REPLACE: [
            (FN_CTRL, r"replace F10"),
        ]
    },
    {
        REPL_KEYCODE: "MINUS",
        REPLACE: [
            (FN_CTRL, r"replace F11"),
        ]
    },
    {
        REPL_KEYCODE: "EQUALS",
        REPLACE: [
            (FN_CTRL, r"replace F12"),
        ]
    },
    # ROW 2 ###############################################################
    # ROW 3 ###############################################################
    {
        REPL_KEYCODE: "SLASH", # APOS
        REPLACE: [
            (BASE, r"','"),
            (SHIFT, r"'\"'"),
        ]
    },
    {
        REPL_KEYCODE: "ENTER",
        REPLACE: [
            (FN_CTRL, r"replace MEDIA_PLAY_PAUSE"),
        ]
    },
    # ROW 4 ###############################################################
    {
        REPL_KEYCODE: "COMMA",
        REPLACE: [
            (FN_CTRL, r"replace MEDIA_REWIND"),
        ]
    },
    {
        REPL_KEYCODE: "PERIOD",
        REPLACE: [
            (FN_CTRL, r"replace MEDIA_FAST_FORWARD"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_UP",
        REPLACE: [
            (FN_CTRL, r"replace VOLUME_UP"),
        ]
    },
    # ROW 5 ###############################################################
    {
        REPL_KEYCODE: "ZENKAKU_HANKAKU", #SYM
        REPLACE: [
            (LALT, r"replace POWER"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_LEFT",
        REPLACE: [
            (FN_CTRL, r"replace MEDIA_PREVIOUS"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_DOWN",
        REPLACE: [
            (FN_CTRL, r"replace VOLUME_DOWN"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_RIGHT",
        REPLACE: [
            (FN_CTRL, r"replace MEDIA_NEXT"),
        ]
    }
]
