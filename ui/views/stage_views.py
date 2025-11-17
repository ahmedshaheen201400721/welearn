from django.utils.translation import gettext as _

stage_list_view = {
    "key": "courses_stage_list_view",
    "menu_item": "courses_child_menu_stage",
    "name": "courses stage list view",
    "model": "courses.stage",
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
                    'name': 'price',
                    'widget': 'monetary',
                    'string': _('Price'),
                },
                {
                    'name': 'duration',
                    'widget': 'text',
                    'string': _('Duration'),
                },
                # {
                #     'name': 'active',
                #     'widget': 'boolean',
                #     'string': _('Active')
                # },
                # {
                #     'name': 'category',
                #     'widget': 'relation',
                #     'string':'category'
                # },
                # {
                #     'name': 'subcategory',
                #     'widget': 'relation',
                #     'string':'subcategory'
                # },
            ]
        }
    }
}

stage_form_view = {
    "key": "courses_stage_form_view",
    "name": "Courses stage Form",
    "menu_item": "courses_child_menu_stage",
    "model": "courses.stage",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "title": "Basic Information",
                    "groups": [
                        {
                            "title": "stage Details",
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "price", "widget": "number"},
                                # {"name": "duration", "widget": "text"},
                                # {"name": "active", "widget": "switch"}
                            ]
                        },
                        {
                            "title": "Description",
                            "fields": [
                                # {'name': "category", "widget": "relation"},
                                # {'name': "subcategory", "widget": "relation"},
                                {"name": "description", "widget": "textarea"},
                            ]
                        }
                    ]
                }
            ]
        }
    }
}

stage_kanban_view = {
    "key": "courses_stage_kanban_view",
    "menu_item": "courses_child_menu_stage",
    "name": "courses stage kanban view",
    "model": "courses.stage",
    "view_type": "kanban",
    "priority": 22,
    "module": "courses",
    "body": {
        "kanban": {
            "id": "courses-stage-kanban",
            "name": "Courses stage Kanban",
            "description": "Kanban view for courses stages",
            "group_by": {
                "name": "active",
                "tag": "field"
            },
            "card": {
                "header": {
                    "profile": {
                        "title": {"name": "name", "tag": "field", "widget": "text"}
                    },
                    "fields": [
                        {"name": "price", "tag": "field", "widget": "number"},
                        {"name": "duration", "tag": "field", "widget": "text"},
                        {"name": "active", "tag": "field", "widget": "switch"},
                    ],
                    "divider": True,
                },
                "body": {
                    "fields": [
                        {"name": "description", "tag": "field", "widget": "textarea"},
                    ],
                }
            }
        }
    }
}

stage_graph_view = {
    "key": "courses_stage_graph_view",
    "menu_item": "courses_child_menu_stage",
    "name": "courses stage graph view",
    "model": "courses.stage",
    "view_type": "graph",
    "priority": 23,
    'module': 'courses',
    "body": {
        'graph': {
            'fields': [
                {
                    'name': 'name',
                    'string': _('stage'),
                },
                {
                    'name': 'active',
                    'string': _('Active Status'),
                }
            ],
            'measures': [
                {
                    'name': 'price',
                    'string': _('Total Price'),
                    'tag': 'field',
                }
            ],
            'defaults': {
                'view': 'bar',
                'field': 'name',
                'measure': 'sum',
            }
        }
    }
}

stage_search_view = {
    "key": "courses_stage_search_view",
    "menu_item": "courses_child_menu_stage",
    "name": "courses stage search view",
    "model": "courses.stage",
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
                    "name": ["active"],
                    "widget": "boolean",
                    "string": _("Active"),
                }
            ]
        }
    }
}


