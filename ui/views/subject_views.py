from django.utils.translation import gettext as _
subject_list_view = {
    "key": "courses_subject_list_view",
    "menu_item": "courses_child_menu_subject",
    "name": "courses subject list view",
    "model": "courses.subject",
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
                    'name': 'categories',
                    'widget': 'relation',
                    'string':'categories',
                    'multiSelect': True
                },
                {
                    'name': 'sub_categories',
                    'widget': 'relation',
                    'string':'sub_categories',
                    'multiSelect': True
                },
                
                {
                    'name': 'Stages',
                    'widget': 'relation',
                    'string':'Stages',
                    'multiSelect': True
                },
            ]
        }
    }
}


subject_form_view = {
    "key": "courses_subject_form_view",
    "menu_item": "courses_child_menu_subject",
    "name": "Courses subject Form",
    "model": "courses.subject",
    "view_type": "form",
    "body": {
        "sheet": {
            "sections": [
                {
                    "title": "subject Information",
                    "groups": [
                        {
                            "title": "subject Details",
                            "fullWidth": False,
                            "fields": [
                                {"name": "name", "widget": "text"},
                                {"name": "categories", "widget": "relation"},
                                {"name": "sub_categories", "widget": "relation"},
                                {"name": "Stages", "widget": "relation"}
                            ]
                        },
                        {
                            "title": "Description",
                            "fullWidth": False,
                            "fields": [
                                {"name": "description", "widget": "textarea"},
                                
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
