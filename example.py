# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from draftjs_exporter.html import HTML

from draftjs_exporter_markdown import BLOCK_MAP, ENGINE, ENTITY_DECORATORS, STYLE_MAP

if __name__ == '__main__':
    config = {
        'block_map': BLOCK_MAP,
        'style_map': STYLE_MAP,
        'entity_decorators': ENTITY_DECORATORS,
        'engine': ENGINE,
    }

    exporter = HTML(config)

    content_state = {
        "entityMap": {
            "0": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://github.com/facebook/draft-js"
                }
            },
            "1": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://facebook.github.io/react/docs/top-level-api.html#react.createelement"
                }
            },
            "2": {
                "type": "HORIZONTAL_RULE",
                "mutability": "IMMUTABLE",
                "data": {}
            },
            "3": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://facebook.github.io/react/docs/jsx-in-depth.html"
                }
            },
            "4": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "https://github.com/springload/draftjs_exporter/pull/17"
                }
            },
            "5": {
                "type": "IMAGE",
                "mutability": "IMMUTABLE",
                "data": {
                    "alt": "Test image alt text",
                    "src": "https://placekitten.com/g/300/200",
                    "width": 300,
                    "height": 200
                }
            },
            "6": {
                "type": "LINK",
                "mutability": "MUTABLE",
                "data": {
                    "url": "http://embed.ly/"
                }
            },
            "8": {
                "type": "EXAMPLE_MISSING",
                "mutability": "MUTABLE",
                "data": {
                    "url": "http://www.youtube.com/watch?v=feUYwoLhE_4",
                }
            },
        },
        "blocks": [{
            "key": "b0ei9",
            "text": "draftjs_exporter is an HTML exporter for Draft.js content",
            "type": "header-two",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 41,
                "length": 8,
                "key": 0
            }],
            "data": {}
        }, {
            "key": "74al",
            "text": "Try it out by running this file!",
            "type": "blockquote",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {
                "cite": "http://example.com/"
            }
        }, {
            "key": "7htbd",
            "text": "Features 📝🍸",
            "type": "header-three",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "32lnv",
            "text": "The exporter aims to provide sensible defaults from basic block types and inline styles to HTML, that can easily be customised when required. For more advanced scenarios, an API is provided (mimicking React's createElement) to create custom rendering components of arbitrary complexity.",
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 209,
                "length": 13,
                "style": "CODE"
            }],
            "entityRanges": [{
                "offset": 209,
                "length": 13,
                "key": 1
            }],
            "data": {}
        }, {
            "key": "eqjvu",
            "text": " ",
            "type": "atomic",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 0,
                "length": 1,
                "key": 2
            }],
            "data": {}
        }, {
            "key": "9fr0j",
            "text": "Here are some features worth highlighting:",
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2mhgt",
            "text": "Convert line breaks to <br>\nelements.",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 23,
                "length": 4,
                "style": "CODE"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "f4gp0",
            "text": "Automatic conversion of entity data to HTML attributes (int & boolean to string, style object to style string).",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 81,
                "length": 12,
                "style": "CODE"
            }, {
                "offset": 97,
                "length": 12,
                "style": "CODE"
            }],
            "entityRanges": [{
                "offset": 81,
                "length": 28,
                "key": 3
            }],
            "data": {}
        }, {
            "key": "3cnm0",
            "text": "Wrapped blocks (<li> elements go inside <ul> or <ol>).",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [{
                "offset": 16,
                "length": 5,
                "style": "CODE"
            }, {
                "offset": 40,
                "length": 4,
                "style": "CODE"
            }, {
                "offset": 48,
                "length": 4,
                "style": "CODE"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "h5rn",
            "text": "With arbitrary nesting.",
            "type": "unordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "5qfeb",
            "text": "Common text styles: Bold, Italic, Underline, Monospace, Strikethrough. cmd + b",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [{
                "offset": 20,
                "length": 4,
                "style": "BOLD"
            }, {
                "offset": 26,
                "length": 6,
                "style": "ITALIC"
            }, {
                "offset": 34,
                "length": 9,
                "style": "UNDERLINE"
            }, {
                "offset": 45,
                "length": 9,
                "style": "CODE"
            }, {
                "offset": 56,
                "length": 14,
                "style": "STRIKETHROUGH"
            }, {
                "offset": 71,
                "length": 7,
                "style": "KEYBOARD"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2ol8n",
            "text": "Overlapping text styles. Custom styles too!",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [{
                "offset": 0,
                "length": 14,
                "style": "STRIKETHROUGH"
            }, {
                "offset": 12,
                "length": 4,
                "style": "BOLD"
            }, {
                "offset": 14,
                "length": 11,
                "style": "ITALIC"
            }],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2lno0",
            "text": "#hashtag support via #CompositeDecorators.",
            "type": "unordered-list-item",
            "depth": 3,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 21,
                "length": 20,
                "key": 4
            }],
            "data": {}
        }, {
            "key": "37n0m",
            "text": "Linkify URLs too! http://example.com/",
            "type": "unordered-list-item",
            "depth": 4,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n01",
            "text": "Depth can go back and forth, it works fiiine (1) - 2",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n02",
            "text": "Depth can go back and forth, it works fiiine (2) - 1",
            "type": "unordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n03",
            "text": "Depth can go back and forth, it works fiiine (3) - 2",
            "type": "unordered-list-item",
            "depth": 2,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n04",
            "text": "Depth can go back and forth, it works fiiine (4) - 1",
            "type": "unordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "37n05",
            "text": "Depth can go back and forth, it works fiiine (5) - 0",
            "type": "unordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "3tbpg",
            "text": " ",
            "type": "atomic",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [{
                "offset": 0,
                "length": 1,
                "key": 5
            }],
            "data": {}
        }, {
            "key": "5t6c9",
            "text": "For developers 🚀",
            "type": "header-three",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "2nb2a",
            "text": "Import the library",
            "type": "ordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "cfom5",
            "text": "Define your configuration",
            "type": "ordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "e2114",
            "text": "Go!",
            "type": "ordered-list-item",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "adt4j",
            "text": "Optionally, define your custom components.",
            "type": "ordered-list-item",
            "depth": 1,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }, {
            "key": "ed7hu",
            "text": "def blockquote(props):\n    block_data = props['block']['data']\n    return DOM.create_element('blockquote', {\n        'cite': block_data.get('cite')\n    }, props['children'])",
            "type": "code-block",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {
                "language": "python"
            }
        }, {
            "key": "1nols",
            "text": "Voilà!",
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }]
    }
    markup = exporter.render(content_state)

    print(markup)
