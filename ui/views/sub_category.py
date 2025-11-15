from django.utils.translation import gettext as _

subcategory_list_view = {
    "key": "courses_subcategory_list_view",
    "menu_item": "courses_child_menu_subcategory",
    "name": "courses subcategory list view",
    "model": "courses.subcategory",
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
                    'name': 'category',
                    'widget': 'relation',
                    'string': _('category'),
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

subcategory_form_view = {
    "key": "courses_subcategory_form_view",
    "name": "Courses subcategory Form",
    "menu_item": "courses_child_menu_subcategory",
    "model": "courses.subcategory",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "groups": [
                        {
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "category", "widget": "relation"},
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



