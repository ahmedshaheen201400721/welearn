from django.utils.translation import gettext as _

courses_list_view = {
    "key": "courses_courses_list_view",
    "menu_item": "courses_child_menu_courses",
    "name": "courses courses list view",
    "model": "courses.course",
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
                    'name': 'track',
                    'widget': 'relation',
                    'string': _('track'),
                },
                {
                    'name': 'category',
                    'widget': 'relation',
                    'string': _('category'),
                },
                {
                    'name': 'sub_category',
                    'widget': 'relation',
                    'string': _('sub_category'),
                },
                {
                    'name': 'level',
                    'widget': 'relation',
                    'string': _('Level'),
                },
                {
                    'name': 'stage',
                    'widget': 'relation',
                    'string': _('stage'),
                },
                {
                    'name': 'subject',
                    'widget': 'relation',
                    'string': _('subject'),
                },
                {
                    'name': 'price',
                    'widget': 'monetary',
                    'string': _('Price')
                },
                {
                    'name': 'is_published',
                    'widget': 'boolean',
                    'string': _('Published')
                },
                
            ]
        }
    }
}


courses_form_view = {
    "key": "courses_courses_form_view",
    "menu_item": "courses_child_menu_courses",
    "name": "Courses Form",
    "model": "courses.course",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "title": "Basic Information",
                    "groups": [
                        {
                            "title": "Course Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "track", "widget": "relation"},
                                {"name": "category", "widget": "relation"},
                                {"name": "sub_category", "widget": "relation"},
                                {"name": "level", "widget": "relation"},
                                {"name": "stage", "widget": "relation"},
                                {"name": "subject", "widget": "relation"},
                               

                            ]
                        },
                        {
                            "title": "Pricing & Duration",
                            "fullWidth": False,
                            "fields": [
                                {"name": "price", "widget": "number"},
                                {"name": "duration_hours", "widget": "number"},
                                 {"name": "is_published", "widget": "switch"},
                                {"name": "description", "widget": "textarea"}
                            ]
                        }
                    ]
                },
                # {
                #     "title": "Description",
                #     "groups": [
                #         {
                #             "title": "About Course",
                #             "fullWidth": True,
                #             "fields": [
                #                 {"name": "description", "widget": "textarea"}
                #             ]
                #         }
                #     ]
                # }
            ]
        }
    }
}

courses_kanban_view = {
    "key": "courses_courses_kanban_view",
    "menu_item": "courses_child_menu_courses",
    "name": "courses courses kanban view",
    "model": "courses.course",
    "view_type": "kanban",
    "priority": 22,
    "module": "courses",
    "body": {
        "kanban": {
            "id": "courses-courses-kanban",
            "name": "Courses Kanban",
            "description": "Kanban view for courses",
            "group_by": {
                "name": "level",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"}
                    },
                    "fields": [
                        {"name": "price", "tag": "field", "widget": "number"},
                        {"name": "duration_hours", "tag": "field", "widget": "number"},
                        {"name": "is_published", "tag": "field", "widget": "switch"},
                        {"name": "created_at", "tag": "field", "widget": "datetime"},
                    ],
                    "divider": True,
                },
                "body": {
                    "fields": [
                        {"name": "description", "tag": "field", "widget": "textarea"},
                        {"name": "stage", "tag": "field", "widget": "relation"},
                    ],
                }
            }
        }
    }
}

courses_graph_view = {
    "key": "courses_courses_graph_view",
    "menu_item": "courses_child_menu_courses",
    "name": "courses courses graph view",
    "model": "courses.course",
    "view_type": "graph",
    "priority": 23,
    'module': 'courses',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'level',
                    'string': _('Level'),
                },
                {
                    'name': 'stage',
                    'string': _('stage'),
                },
                {
                    'name': 'is_published',
                    'string': _('Published Status'),
                }
            ],
            'measures': [
                {
                    'name': 'price',
                    'string': _('Total Price'),
                    'tag': 'field',
                },
                {
                    'name': 'duration_hours',
                    'string': _('Total Duration'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'level',
                'measure': 'sum',
            }
        }
    }
}

courses_search_view = {
    "key": "courses_courses_search_view",
    "menu_item": "courses_child_menu_courses",
    "name": "courses courses search view",
    "model": "courses.course",
    "view_type": "search",
    "priority": 24,
    'module': 'courses',
    "body": {
        "search": {
            "search_fields": [
                {
                    "name": ["name"],
                    "widget": "text",
                    "string": _("Name"),
                },
                {
                    "name": ["price"],
                    "widget": "number",
                    "string": _("Price"),
                },
                {
                    "name": ["duration_hours"],
                    "widget": "number",
                    "string": _("Duration Hours"),
                },
                {
                    "name": ["is_published"],
                    "widget": "boolean",
                    "string": _("Published"),
                }
            ]
        }
    }
}