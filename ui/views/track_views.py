from django.utils.translation import gettext as _

track_list_view = {
    "key": "courses_track_list_view",
    "menu_item": "courses_child_menu_track",
    "name": "courses track list view",
    "model": "courses.track",
    "view_type": "list",
    "priority": 21,
    'module': 'courses',
    'body': {
        'tree': {
            'fields': [
                {
                    'name': 'name',
                    'widget': 'text',
                    'string': _('Name'),
                },
                {
                    'name': 'description',
                    'widget': 'text',
                    'string': _('Description'),
                }
            ]
        }
    }
}

track_form_view = {
    "key": "courses_track_form_view",
    "name": "Courses track Form",
    "menu_item": "courses_child_menu_track",
    "model": "courses.track",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "groups": [
                        {
                            "fields": [
                                {"name": "name", "widget": "text"}
                            ]
                        },
                        {
                            "fields": [
                                {"name": "description", "widget": "textarea"}
                            ]
                        }
                    ]
                }
            ]
        }
    }
}



