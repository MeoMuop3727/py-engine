_FUNC_NAMES_CLASS_ICONS: list[str] = [
    "register",
    "unregister"
]
_FUNCTOOL_NAMES: list[str] = [
    "svg2png(path: str, /, size: int = 32) -> pygame.Surface: ...",
    "url2png(url: str, /, size: int = 32) -> pygame.Surface: ...",
    'code2png(source: str, /, size: int = 32, fill: str = "#FFFFFF", color: str = "#000000") -> pygame.Surface: ...',
    'icon2png(icon: IconType, /, size: int = 32, fill: str = "#FFFFFF", color: str = "#000000") -> pygame.Surface: ...'
]

"""
A set of approximately 150 common game icons, ready for immediate use with
`code2png` / `icon2png`. Each icon consists of an SVG markup string (24x24 viewBox)
using `stroke="currentColor"` or `fill="currentColor"` to support runtime
color changes (see the `code2png` function).
 
This is a set of simple, hand-drawn SVGs (line-style, approximating real shapes),
suitable for use as placeholders or prototypes during development. If
pixel-perfect icons are required, the `path` should be replaced with actual
SVG data (e.g., downloaded from Material Symbols during development).
"""

from .type import IconType
 
_L = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
_F = 'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" stroke="none"'
 
 
def _l(body: str) -> str:
    return f'<svg {_L}>{body}</svg>'
 
 
def _f(body: str) -> str:
    return f'<svg {_F}>{body}</svg>'
 
 
_ICONS: dict[str, IconType] = {
 
    # ---------- UI Basic ----------
    "MENU": IconType("MENU", _l('<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>')),
    "CLOSE": IconType("CLOSE", _l('<line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/>')),
    "SETTINGS": IconType("SETTINGS", _l('<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 0 1-4 0v-.1a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.9.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.9 1.7 1.7 0 0 0-1.5-1H3a2 2 0 0 1 0-4h.1A1.7 1.7 0 0 0 4.6 9a1.7 1.7 0 0 0-.3-1.9l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.9.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 0 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.9-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.9V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 0 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>')),
    "CHECK": IconType("CHECK", _l('<polyline points="4,12 9,17 20,6"/>')),
    "CHECK_CIRCLE": IconType("CHECK_CIRCLE", _l('<circle cx="12" cy="12" r="9"/><polyline points="7,12.5 10,15.5 17,8.5"/>')),
    "ADD": IconType("ADD", _l('<line x1="12" y1="3" x2="12" y2="21"/><line x1="3" y1="12" x2="21" y2="12"/>')),
    "ADD_CIRCLE": IconType("ADD_CIRCLE", _l('<circle cx="12" cy="12" r="9"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/>')),
    "REMOVE": IconType("REMOVE", _l('<line x1="3" y1="12" x2="21" y2="12"/>')),
    "REMOVE_CIRCLE": IconType("REMOVE_CIRCLE", _l('<circle cx="12" cy="12" r="9"/><line x1="8" y1="12" x2="16" y2="12"/>')),
    "DELETE": IconType("DELETE", _l('<line x1="3" y1="6" x2="21" y2="6"/><path d="M8 6V3h8v3"/><path d="M6 6l1 15h10l1-15"/><line x1="10" y1="10" x2="10" y2="17"/><line x1="14" y1="10" x2="14" y2="17"/>')),
    "EDIT": IconType("EDIT", _l('<path d="M4 20h4l11-11-4-4L4 16z"/><line x1="13.5" y1="6.5" x2="17.5" y2="10.5"/>')),
    "SEARCH": IconType("SEARCH", _l('<circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16" y2="16"/>')),
    "FILTER": IconType("FILTER", _l('<polygon points="4,4 20,4 14,12 14,19 10,21 10,12"/>')),
    "SORT": IconType("SORT", _l('<line x1="4" y1="6" x2="16" y2="6"/><line x1="4" y1="12" x2="12" y2="12"/><line x1="4" y1="18" x2="8" y2="18"/><polyline points="17,15 20,18 20,4"/>')),
    "REFRESH": IconType("REFRESH", _l('<path d="M21 12a9 9 0 1 1-3-6.7"/><polyline points="21,3 21,9 15,9"/>')),
    "HOME": IconType("HOME", _l('<path d="M3 11 12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/>')),
    "BACK": IconType("BACK", _l('<polyline points="15,5 8,12 15,19"/>')),
    "FORWARD": IconType("FORWARD", _l('<polyline points="9,5 16,12 9,19"/>')),
    "UP": IconType("UP", _l('<polyline points="5,15 12,8 19,15"/>')),
    "DOWN": IconType("DOWN", _l('<polyline points="5,9 12,16 19,9"/>')),
 
    # ---------- Arrows / Nav ----------
    "ARROW_LEFT": IconType("ARROW_LEFT", _l('<line x1="20" y1="12" x2="4" y2="12"/><polyline points="10,6 4,12 10,18"/>')),
    "ARROW_RIGHT": IconType("ARROW_RIGHT", _l('<line x1="4" y1="12" x2="20" y2="12"/><polyline points="14,6 20,12 14,18"/>')),
    "ARROW_UP": IconType("ARROW_UP", _l('<line x1="12" y1="20" x2="12" y2="4"/><polyline points="6,10 12,4 18,10"/>')),
    "ARROW_DOWN": IconType("ARROW_DOWN", _l('<line x1="12" y1="4" x2="12" y2="20"/><polyline points="6,14 12,20 18,14"/>')),
    "CHEVRON_LEFT": IconType("CHEVRON_LEFT", _l('<polyline points="15,4 7,12 15,20"/>')),
    "CHEVRON_RIGHT": IconType("CHEVRON_RIGHT", _l('<polyline points="9,4 17,12 9,20"/>')),
    "CHEVRON_UP": IconType("CHEVRON_UP", _l('<polyline points="4,15 12,7 20,15"/>')),
    "CHEVRON_DOWN": IconType("CHEVRON_DOWN", _l('<polyline points="4,9 12,17 20,9"/>')),
    "EXPAND": IconType("EXPAND", _l('<polyline points="8,3 3,3 3,8"/><polyline points="16,3 21,3 21,8"/><polyline points="3,16 3,21 8,21"/><polyline points="21,16 21,21 16,21"/>')),
    "COLLAPSE": IconType("COLLAPSE", _l('<polyline points="3,8 8,8 8,3"/><polyline points="21,8 16,8 16,3"/><polyline points="8,21 8,16 3,16"/><polyline points="16,16 16,21 21,21"/>')),
 
    # ---------- Media / Playback ----------
    "PLAY": IconType("PLAY", _f('<polygon points="6,4 20,12 6,20"/>')),
    "PAUSE": IconType("PAUSE", _f('<rect x="5" y="4" width="5" height="16"/><rect x="14" y="4" width="5" height="16"/>')),
    "STOP": IconType("STOP", _f('<rect x="5" y="5" width="14" height="14"/>')),
    "RESTART": IconType("RESTART", _l('<path d="M3 12a9 9 0 1 0 3-6.7"/><polyline points="3,3 3,9 9,9"/>')),
    "FAST_FORWARD": IconType("FAST_FORWARD", _f('<polygon points="4,4 13,12 4,20"/><polygon points="12,4 21,12 12,20"/>')),
    "REWIND": IconType("REWIND", _f('<polygon points="20,4 11,12 20,20"/><polygon points="12,4 3,12 12,20"/>')),
    "REPEAT": IconType("REPEAT", _l('<path d="M17 2l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>')),
    "SHUFFLE": IconType("SHUFFLE", _l('<polyline points="16,3 21,3 21,8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21,16 21,21 16,21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/>')),
    "VOLUME_UP": IconType("VOLUME_UP", _l('<polygon points="4,9 8,9 13,4 13,20 8,15 4,15"/><path d="M17 8a5 5 0 0 1 0 8"/><path d="M19.5 5.5a9 9 0 0 1 0 13"/>')),
    "VOLUME_MUTE": IconType("VOLUME_MUTE", _l('<polygon points="4,9 8,9 13,4 13,20 8,15 4,15"/><line x1="17" y1="9" x2="22" y2="15"/><line x1="22" y1="9" x2="17" y2="15"/>')),
 
    # ---------- Game Core ----------
    "HEART": IconType("HEART", _f('<path d="M12 21s-7.5-4.8-10-9.5C0.3 7.3 2.5 4 6 4c2.1 0 3.7 1.2 6 3.6C14.3 5.2 15.9 4 18 4c3.5 0 5.7 3.3 4 7.5-2.5 4.7-10 9.5-10 9.5z"/>')),
    "HEART_BROKEN": IconType("HEART_BROKEN", _l('<path d="M12 21s-7.5-4.8-10-9.5C0.3 7.3 2.5 4 6 4c2.1 0 3.7 1.2 6 3.6C14.3 5.2 15.9 4 18 4c3.5 0 5.7 3.3 4 7.5-2.5 4.7-10 9.5-10 9.5z"/><polyline points="13,7 10,12 14,14 11,19"/>')),
    "SHIELD": IconType("SHIELD", _l('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>')),
    "SHIELD_CHECK": IconType("SHIELD_CHECK", _l('<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><polyline points="8.5,12.5 11,15 15.5,9.5"/>')),
    "SWORD": IconType("SWORD", _l('<line x1="4" y1="20" x2="16" y2="8"/><polyline points="14,4 20,4 20,10"/><line x1="10" y1="14" x2="6" y2="18"/><line x1="4" y1="20" x2="6" y2="18"/>')),
    "BOW": IconType("BOW", _l('<path d="M6 3a13 13 0 0 0 0 18"/><line x1="6" y1="3" x2="6" y2="21"/><line x1="6" y1="12" x2="21" y2="12"/><polyline points="17,9 21,12 17,15"/>')),
    "ARROW_WEAPON": IconType("ARROW_WEAPON", _l('<line x1="3" y1="21" x2="21" y2="3"/><polyline points="14,3 21,3 21,10"/><line x1="3" y1="21" x2="7" y2="21"/><line x1="3" y1="21" x2="3" y2="17"/>')),
    "AXE": IconType("AXE", _l('<line x1="9" y1="21" x2="17" y2="5"/><path d="M14 3c3 0 6 2 6 5-3 0-6-1-8-3z"/>')),
    "HAMMER": IconType("HAMMER", _l('<line x1="14" y1="10" x2="5" y2="19"/><path d="M13 4l7 7-3 3-7-7z"/><line x1="17" y1="6" x2="19" y2="4"/>')),
    "GUN": IconType("GUN", _l('<path d="M3 14h10v-3h6v3h2v3h-2v2h-4v-2H9l-2 4H4v-4H3z"/>')),
    "HELMET": IconType("HELMET", _l('<path d="M4 15a8 8 0 0 1 16 0"/><path d="M4 15h16v3H4z"/><path d="M9 15v-3a3 3 0 0 1 6 0v3"/>')),
    "ARMOR": IconType("ARMOR", _l('<path d="M12 3l7 3v5c0 5-3 8-7 10-4-2-7-5-7-10V6z"/><line x1="12" y1="3" x2="12" y2="21"/>')),
    "BOOTS": IconType("BOOTS", _l('<path d="M8 3v10l-5 4v3h9v-5h4v5h-2M8 13h6"/>')),
    "GLOVES": IconType("GLOVES", _l('<path d="M6 12V6a2 2 0 0 1 4 0v4"/><path d="M10 10V5a2 2 0 0 1 4 0v5"/><path d="M14 10V6a2 2 0 0 1 4 0v6c0 4-2 7-6 7H8a3 3 0 0 1-3-3v-4"/>')),
    "RING": IconType("RING", _l('<circle cx="12" cy="15" r="6"/><polygon points="9,9 12,3 15,9"/>')),
    "AMULET": IconType("AMULET", _l('<path d="M8 3l4 3 4-3"/><circle cx="12" cy="15" r="6"/><circle cx="12" cy="15" r="2"/>')),
    "POTION": IconType("POTION", _l('<path d="M10 3h4v4l4 8a3 3 0 0 1-3 6H9a3 3 0 0 1-3-6l4-8z"/><line x1="9" y1="3" x2="15" y2="3"/>')),
    "FLASK": IconType("FLASK", _l('<path d="M9 2h6M10 2v6l-5 10a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-10V2"/><line x1="8" y1="14" x2="16" y2="14"/>')),
    "SKULL": IconType("SKULL", _l('<path d="M12 3a8 8 0 0 0-8 8c0 3 1.5 5 3 6v3h10v-3c1.5-1 3-3 3-6a8 8 0 0 0-8-8z"/><circle cx="9" cy="11" r="1.3"/><circle cx="15" cy="11" r="1.3"/><line x1="10" y1="17" x2="10" y2="20"/><line x1="14" y1="17" x2="14" y2="20"/>')),
    "BOMB": IconType("BOMB", _l('<circle cx="11" cy="14" r="7"/><path d="M15 8l3-3"/><path d="M17 3l3 1-1 3"/>')),
 
    # ---------- Currency / Reward ----------
    "COIN": IconType("COIN", _l('<circle cx="12" cy="12" r="8"/><text x="12" y="16" font-size="10" text-anchor="middle" fill="currentColor" stroke="none">$</text>')),
    "COINS": IconType("COINS", _l('<circle cx="9" cy="9" r="6"/><circle cx="15" cy="15" r="6"/>')),
    "GEM": IconType("GEM", _l('<polygon points="6,9 12,3 18,9 12,21"/><line x1="6" y1="9" x2="18" y2="9"/><line x1="9" y1="9" x2="12" y2="21"/><line x1="15" y1="9" x2="12" y2="21"/>')),
    "DIAMOND": IconType("DIAMOND", _f('<polygon points="12,2 22,9 12,22 2,9"/>')),
    "TROPHY": IconType("TROPHY", _l('<path d="M8 4h8v5a4 4 0 0 1-8 0z"/><path d="M8 5H4v2a4 4 0 0 0 4 4"/><path d="M16 5h4v2a4 4 0 0 1-4 4"/><line x1="12" y1="13" x2="12" y2="17"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="9" y1="17" x2="15" y2="17"/>')),
    "MEDAL": IconType("MEDAL", _l('<circle cx="12" cy="15" r="6"/><polyline points="9,3 9,11 12,9 15,11 15,3"/>')),
    "CROWN": IconType("CROWN", _l('<polyline points="3,8 7,14 12,6 17,14 21,8 19,18 5,18"/>')),
    "STAR": IconType("STAR", _f('<polygon points="12,2 15,9 22,9.5 16.5,14 18.5,21 12,17 5.5,21 7.5,14 2,9.5 9,9"/>')),
    "STAR_HALF": IconType("STAR_HALF", _l('<polygon points="12,2 15,9 22,9.5 16.5,14 18.5,21 12,17 5.5,21 7.5,14 2,9.5 9,9"/><path d="M12 2v15" fill="currentColor" stroke="none"/>')),
    "TREASURE_CHEST": IconType("TREASURE_CHEST", _l('<rect x="3" y="10" width="18" height="10" rx="1"/><path d="M3 10a9 5 0 0 1 18 0"/><line x1="12" y1="13" x2="12" y2="16"/>')),
 
    # ---------- Stats ----------
    "XP": IconType("XP", _l('<polygon points="3,4 9,4 12,9 15,4 21,4 15,12 21,20 15,20 12,15 9,20 3,20 9,12"/>')),
    "MANA": IconType("MANA", _f('<path d="M12 2c3 4 7 8 7 12a7 7 0 0 1-14 0c0-4 4-8 7-12z"/>')),
    "ENERGY": IconType("ENERGY", _f('<polygon points="13,2 4,14 11,14 9,22 20,9 13,9"/>')),
    "LEVEL_UP": IconType("LEVEL_UP", _l('<polyline points="4,16 12,8 20,16"/><line x1="12" y1="8" x2="12" y2="20"/>')),
    "HEALTH_BAR": IconType("HEALTH_BAR", _l('<rect x="2" y="9" width="20" height="6" rx="1"/><line x1="8" y1="9" x2="8" y2="15"/><line x1="14" y1="9" x2="14" y2="15"/>')),
    "TIMER": IconType("TIMER", _l('<circle cx="12" cy="13" r="8"/><line x1="12" y1="13" x2="12" y2="9"/><line x1="12" y1="13" x2="15" y2="14"/><line x1="9" y1="2" x2="15" y2="2"/>')),
    "CLOCK": IconType("CLOCK", _l('<circle cx="12" cy="12" r="9"/><line x1="12" y1="12" x2="12" y2="7"/><line x1="12" y1="12" x2="16" y2="14"/>')),
    "HOURGLASS": IconType("HOURGLASS", _l('<path d="M6 2h12M6 22h12M6 2c0 6 12 8 12 0M6 22c0-6 12-8 12 0" transform="translate(0,0)"/><line x1="6" y1="2" x2="18" y2="2"/><line x1="6" y1="22" x2="18" y2="22"/><path d="M6 2c0 6 6 8 6 10 0-2 6-4 6-10"/><path d="M6 22c0-6 6-8 6-10 0 2 6 4 6 10"/>')),
    "TARGET": IconType("TARGET", _l('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>')),
    "CROSSHAIR": IconType("CROSSHAIR", _l('<circle cx="12" cy="12" r="8"/><line x1="12" y1="2" x2="12" y2="6"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="2" y1="12" x2="6" y2="12"/><line x1="18" y1="12" x2="22" y2="12"/>')),
 
    # ---------- Inventory ----------
    "BACKPACK": IconType("BACKPACK", _l('<path d="M7 9V6a5 5 0 0 1 10 0v3"/><rect x="5" y="9" width="14" height="12" rx="2"/><line x1="9" y1="13" x2="15" y2="13"/>')),
    "KEY": IconType("KEY", _l('<circle cx="7" cy="15" r="4"/><line x1="10" y1="12" x2="21" y2="1" transform="translate(0,4)"/><line x1="16" y1="9" x2="19" y2="9" transform="translate(0,4)"/><line x1="19" y1="6" x2="19" y2="9" transform="translate(0,4)"/>')),
    "LOCK": IconType("LOCK", _l('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')),
    "UNLOCK": IconType("UNLOCK", _l('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 7.6-1.8"/>')),
    "BOOK": IconType("BOOK", _l('<path d="M4 4h9a3 3 0 0 1 3 3v13a3 3 0 0 0-3-2H4z"/><path d="M20 4h-9a3 3 0 0 0-3 3v13a3 3 0 0 1 3-2h9z"/>')),
    "SCROLL": IconType("SCROLL", _l('<path d="M6 3a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2"/><path d="M18 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2"/><line x1="6" y1="3" x2="18" y2="3"/><line x1="6" y1="21" x2="18" y2="21"/><line x1="8" y1="9" x2="16" y2="9"/><line x1="8" y1="13" x2="16" y2="13"/>')),
    "MAP": IconType("MAP", _l('<polygon points="3,5 9,3 15,5 21,3 21,19 15,21 9,19 3,21"/><line x1="9" y1="3" x2="9" y2="19"/><line x1="15" y1="5" x2="15" y2="21"/>')),
    "COMPASS": IconType("COMPASS", _l('<circle cx="12" cy="12" r="9"/><polygon points="15,9 13,13 9,15 11,11"/>')),
    "FLAG": IconType("FLAG", _l('<line x1="5" y1="3" x2="5" y2="21"/><path d="M5 4h13l-3 4 3 4H5z"/>')),
    "BAG": IconType("BAG", _l('<path d="M6 8h12l1 12H5z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>')),
 
    # ---------- Environment ----------
    "TREE": IconType("TREE", _l('<line x1="12" y1="14" x2="12" y2="21"/><polygon points="12,2 6,12 18,12"/><polygon points="12,7 5,16 19,16"/>')),
    "MOUNTAIN": IconType("MOUNTAIN", _l('<polyline points="3,20 9,7 13,14 16,10 21,20"/>')),
    "FIRE": IconType("FIRE", _f('<path d="M12 2c1 4-3 5-3 9a3 3 0 0 0 6 0c0-1-1-2-1-3 2 1 3 3 3 5a5 5 0 0 1-10 0c0-5 4-6 5-11z"/>')),
    "WATER_DROP": IconType("WATER_DROP", _f('<path d="M12 2c4 5 7 9 7 13a7 7 0 0 1-14 0c0-4 3-8 7-13z"/>')),
    "LIGHTNING": IconType("LIGHTNING", _f('<polygon points="13,2 4,14 11,14 9,22 20,9 13,9"/>')),
    "SNOWFLAKE": IconType("SNOWFLAKE", _l('<line x1="12" y1="2" x2="12" y2="22"/><line x1="4" y1="7" x2="20" y2="17"/><line x1="4" y1="17" x2="20" y2="7"/>')),
    "WIND": IconType("WIND", _l('<path d="M3 8h11a3 3 0 1 0-3-3"/><path d="M3 13h15a3 3 0 1 1-3 3"/><path d="M3 18h9"/>')),
    "EARTH": IconType("EARTH", _l('<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 0 1 0 18"/>')),
    "CAVE": IconType("CAVE", _l('<path d="M2 20c2-10 6-16 10-16s8 6 10 16z"/><path d="M8 20c1-5 2-9 4-9s3 4 4 9"/>')),
    "PORTAL": IconType("PORTAL", _l('<ellipse cx="12" cy="12" rx="6" ry="9"/><ellipse cx="12" cy="12" rx="3" ry="9"/>')),
 
    # ---------- Structures ----------
    "HOUSE": IconType("HOUSE", _l('<path d="M3 11 12 3l9 8"/><path d="M5 10v10h14V10"/><rect x="10" y="14" width="4" height="6"/>')),
    "CASTLE": IconType("CASTLE", _l('<path d="M3 21V9h4V6h2v3h2V6h2v3h2V6h2v3h4v12z"/><line x1="3" y1="14" x2="21" y2="14"/>')),
    "TOWER": IconType("TOWER", _l('<polygon points="8,4 16,4 16,8 8,8"/><rect x="9" y="8" width="6" height="13"/><line x1="6" y1="21" x2="18" y2="21"/>')),
    "DOOR": IconType("DOOR", _l('<rect x="6" y="2" width="12" height="20"/><circle cx="14" cy="12" r="0.8" fill="currentColor" stroke="none"/>')),
    "GATE": IconType("GATE", _l('<line x1="4" y1="4" x2="4" y2="20"/><line x1="20" y1="4" x2="20" y2="20"/><line x1="4" y1="4" x2="20" y2="4"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="20" x2="20" y2="20"/>')),
    "LADDER": IconType("LADDER", _l('<line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="7" y1="6" x2="17" y2="6"/><line x1="7" y1="12" x2="17" y2="12"/><line x1="7" y1="18" x2="17" y2="18"/>')),
    "BRIDGE": IconType("BRIDGE", _l('<path d="M2 16a10 6 0 0 1 20 0"/><line x1="5" y1="16" x2="5" y2="20"/><line x1="19" y1="16" x2="19" y2="20"/><line x1="2" y1="20" x2="22" y2="20"/>')),
    "TENT": IconType("TENT", _l('<polygon points="12,3 3,20 21,20"/><line x1="12" y1="3" x2="12" y2="20"/><line x1="8" y1="20" x2="12" y2="12"/><line x1="16" y1="20" x2="12" y2="12"/>')),
    "CAMPFIRE": IconType("CAMPFIRE", _l('<line x1="3" y1="20" x2="10" y2="13"/><line x1="21" y1="20" x2="14" y2="13"/><line x1="3" y1="13" x2="10" y2="20"/><line x1="21" y1="13" x2="14" y2="20"/><path d="M12 6c1 2-1 3-1 5a1.5 1.5 0 0 0 3 0c0-1-1-1.5-1-2 1 .5 2 1.5 2 3a3 3 0 0 1-6 0c0-3 2-4 3-6z"/>')),
    "ANVIL": IconType("ANVIL", _l('<path d="M4 14h6l2-3h6l2 3H8"/><rect x="9" y="14" width="6" height="3"/><line x1="9" y1="17" x2="9" y2="20"/><line x1="15" y1="17" x2="15" y2="20"/><line x1="7" y1="20" x2="17" y2="20"/>')),
 
    # ---------- Devices / Controls ----------
    "GAMEPAD": IconType("GAMEPAD", _l('<rect x="2" y="8" width="20" height="10" rx="4"/><line x1="7" y1="11" x2="7" y2="15"/><line x1="5" y1="13" x2="9" y2="13"/><circle cx="15" cy="12" r="1"/><circle cx="18" cy="14" r="1"/>')),
    "JOYSTICK": IconType("JOYSTICK", _l('<circle cx="12" cy="7" r="3"/><line x1="12" y1="10" x2="12" y2="17"/><ellipse cx="12" cy="19" rx="7" ry="2"/>')),
    "KEYBOARD": IconType("KEYBOARD", _l('<rect x="2" y="6" width="20" height="12" rx="2"/><line x1="6" y1="10" x2="6" y2="10.01"/><line x1="10" y1="10" x2="10" y2="10.01"/><line x1="14" y1="10" x2="14" y2="10.01"/><line x1="18" y1="10" x2="18" y2="10.01"/><line x1="7" y1="14" x2="17" y2="14"/>')),
    "MOUSE_DEVICE": IconType("MOUSE_DEVICE", _l('<rect x="7" y="2" width="10" height="20" rx="5"/><line x1="12" y1="2" x2="12" y2="9"/>')),
    "HEADPHONES": IconType("HEADPHONES", _l('<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="2" y="14" width="4" height="6" rx="1"/><rect x="18" y="14" width="4" height="6" rx="1"/>')),
    "MICROPHONE": IconType("MICROPHONE", _l('<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="8" y1="22" x2="16" y2="22"/>')),
    "SPEAKER": IconType("SPEAKER", _l('<rect x="4" y="2" width="16" height="20" rx="2"/><circle cx="12" cy="8" r="3"/><circle cx="12" cy="16" r="1.5"/>')),
    "WIFI": IconType("WIFI", _l('<path d="M2 8a16 16 0 0 1 20 0"/><path d="M5 12a11 11 0 0 1 14 0"/><path d="M8.5 16a6 6 0 0 1 7 0"/><circle cx="12" cy="19" r="1"/>')),
    "BATTERY": IconType("BATTERY", _l('<rect x="2" y="8" width="17" height="8" rx="2"/><line x1="21" y1="10" x2="21" y2="14"/><line x1="5" y1="10" x2="5" y2="14"/>')),
    "POWER": IconType("POWER", _l('<line x1="12" y1="2" x2="12" y2="11"/><path d="M6.5 6a8 8 0 1 0 11 0"/>')),
 
    # ---------- Social ----------
    "USER": IconType("USER", _l('<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.5 3.5-7 8-7s8 2.5 8 7"/>')),
    "USERS": IconType("USERS", _l('<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3-6 7-6s7 2.5 7 6"/><circle cx="17" cy="9" r="3"/><path d="M15 14c3 0 6 2 6 6"/>')),
    "CHAT": IconType("CHAT", _l('<path d="M4 4h16v12H8l-4 4z"/>')),
    "MESSAGE": IconType("MESSAGE", _l('<rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3,7 12,13 21,7"/>')),
    "MAIL": IconType("MAIL", _l('<rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3,7 12,13 21,7"/>')),
    "BELL": IconType("BELL", _l('<path d="M6 10a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6"/><path d="M10 20a2 2 0 0 0 4 0"/>')),
    "THUMBS_UP": IconType("THUMBS_UP", _l('<path d="M7 11v10H4V11z"/><path d="M7 11l3-8a2 2 0 0 1 2 2v4h6a2 2 0 0 1 2 2l-2 8a2 2 0 0 1-2 2H7"/>')),
    "THUMBS_DOWN": IconType("THUMBS_DOWN", _l('<path d="M7 13V3H4v10z"/><path d="M7 13l3 8a2 2 0 0 0 2-2v-4h6a2 2 0 0 0 2-2l-2-8a2 2 0 0 0-2-2H7"/>')),
    "SHARE": IconType("SHARE", _l('<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="10.5" x2="15.4" y2="6.5"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/>')),
    "FLAG_REPORT": IconType("FLAG_REPORT", _l('<line x1="5" y1="3" x2="5" y2="21"/><path d="M5 4h13l-3 4 3 4H5z"/>')),
 
    # ---------- Misc UI ----------
    "EYE": IconType("EYE", _l('<path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/>')),
    "EYE_OFF": IconType("EYE_OFF", _l('<path d="M1 12s4-7 11-7c2 0 3.7.5 5.1 1.2M23 12s-4 7-11 7c-2 0-3.7-.5-5.1-1.2"/><circle cx="12" cy="12" r="3"/><line x1="2" y1="2" x2="22" y2="22"/>')),
    "PIN": IconType("PIN", _l('<circle cx="12" cy="9" r="5"/><path d="M12 14v7"/><circle cx="12" cy="9" r="1.5"/>')),
    "BOOKMARK": IconType("BOOKMARK", _l('<path d="M6 3h12v18l-6-4-6 4z"/>')),
    "TAG": IconType("TAG", _l('<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7" cy="8" r="1.5"/>')),
    "GRID": IconType("GRID", _l('<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>')),
    "LIST": IconType("LIST", _l('<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/>')),
    "LAYERS": IconType("LAYERS", _l('<polygon points="12,2 22,8 12,14 2,8"/><polyline points="2,14 12,20 22,14"/>')),
    "LINK": IconType("LINK", _l('<path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>')),
    "DOWNLOAD": IconType("DOWNLOAD", _l('<path d="M12 3v13"/><polyline points="6,11 12,17 18,11"/><line x1="4" y1="21" x2="20" y2="21"/>')),
 
    # ---------- Extra (10) ----------
    "UPLOAD": IconType("UPLOAD", _l('<path d="M12 21V8"/><polyline points="6,13 12,7 18,13"/><line x1="4" y1="3" x2="20" y2="3"/>')),
    "SYNC": IconType("SYNC", _l('<path d="M21 12a9 9 0 1 1-3-6.7"/><polyline points="21,3 21,9 15,9"/>')),
    "CLOUD": IconType("CLOUD", _l('<path d="M7 18a4 4 0 0 1 0-8 5.5 5.5 0 0 1 10.7-1.7A4.5 4.5 0 0 1 17 18z"/>')),
    "CLOUD_SAVE": IconType("CLOUD_SAVE", _l('<path d="M7 15a4 4 0 0 1 0-8 5.5 5.5 0 0 1 10.7-1.7A4.5 4.5 0 0 1 17 15z"/><line x1="12" y1="12" x2="12" y2="21"/><polyline points="9,18 12,21 15,18"/>')),
    "DICE": IconType("DICE", _l('<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8" cy="8" r="1" fill="currentColor" stroke="none"/><circle cx="16" cy="8" r="1" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/><circle cx="8" cy="16" r="1" fill="currentColor" stroke="none"/><circle cx="16" cy="16" r="1" fill="currentColor" stroke="none"/>')),
    "CARDS": IconType("CARDS", _l('<rect x="3" y="6" width="12" height="16" rx="2"/><rect x="9" y="2" width="12" height="16" rx="2"/>')),
    "PUZZLE": IconType("PUZZLE", _l('<path d="M6 6h5a2 2 0 1 1 0 4v4a2 2 0 1 0 4 0h4v5h-5a2 2 0 1 1-4 0H6z"/>')),
    "CHESS": IconType("CHESS", _l('<path d="M10 4h4l1 3-2 2 2 2-1 4H9l-1-4 2-2-2-2z"/><line x1="7" y1="20" x2="17" y2="20"/><line x1="8" y1="15" x2="16" y2="15"/>')),
    "TOGGLE_ON": IconType("TOGGLE_ON", _l('<rect x="2" y="7" width="20" height="10" rx="5"/><circle cx="16" cy="12" r="3.5" fill="currentColor" stroke="none"/>')),
    "TOGGLE_OFF": IconType("TOGGLE_OFF", _l('<rect x="2" y="7" width="20" height="10" rx="5"/><circle cx="8" cy="12" r="3.5" fill="currentColor" stroke="none"/>')),
}
