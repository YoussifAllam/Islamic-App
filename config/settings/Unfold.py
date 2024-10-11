# settings.py
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from ..django import ENVIRONMENT


def dashboard_callback(request, context):
    """
    Callback to prepare custom variables for index template which is used as dashboard template.
    """
    context.update({
        "environment": ENVIRONMENT,  # Add the environment variable to the context
    })
    return context


def badge_callback(request):
    return 3


UNFOLD = {
    "SITE_TITLE": "FZAKR",
    "SITE_HEADER": f"FZAKR Admin Panel : {ENVIRONMENT}",
    "SITE_URL": "/",

    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    "SITE_ICON": {
        "light": lambda request: static("icon-light.svg"),  # light mode
        "dark": lambda request: static("icon-light.svg"),  # dark mode
    },

    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("icon-light.svg"),
        },
    ],

    "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
    "ENVIRONMENT": ENVIRONMENT,
    "DASHBOARD_CALLBACK": dashboard_callback,
    "COLORS": {
        "font": {
                "subtle-light": "107 114 128",  # Light grayish color
                "subtle-dark": "51 51 50",       # Dark grayish color
                "default-light": "75 85 99",     # Gray for default text
                "default-dark": "209 213 219",   # Light gray for dark themes
                "important-light": "17 24 39",   # Dark color for important elements
                "important-dark": "243 244 246",  # Light color for important elements dark themes
        },
        "primary": {
            "50": "250 245 255",   # Very light color
            "100": "243 232 255",  # Light pastel color
            "200": "233 213 255",  # Soft purple
            "300": "216 180 254",  # Light purple
            "400": "192 132 252",  # Medium purple
            "500": "168 85 247",   # Bright purple
            "600": "147 51 234",   # Rich purple
            "700": "126 34 206",   # Dark purple
            "800": "107 33 168",   # Darker purple
            "900": "88 28 135",     # Deep purple
            "950": "59 7 100",      # Darkest purple
        },
    },

    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        "badge": badge_callback,
                        "permission": lambda request: request.user.is_superuser,
                    },
                ],
            },
        ],
    },

}
