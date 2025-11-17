# -*- coding: utf-8 -*-
# Menu items for courses module

{
    "courses_main_menu": {
        "name": "courses",
        "icon": "BookOpen",
        "module": "courses",
        "sequence": 44,
        "allowed_groups": ["courses.admins",],
        'children': {                       #1st gen
            
            "courses_child_menu_courses": {
                "name": "Courses",
                "icon": "Book",
                "module": "courses",
                "sequence": 1,
                "view_types": "list,form,kanban,graph,search",
                "model": "courses.course",
            },
            "courses_menu_track": {
                "name": "Track",
                "icon": "TrainTrack",
                "module": "courses",
                
                "sequence": 2,
                "children": {           #2nd gen
                    "courses_child_menu_track": {
                        "name": "Track",
                        "icon": "TrainTrack",
                        "view_types": "list,form",
                        "model": "courses.track",
                        "module": "courses",
                        "sequence": 1,
                        'actions' : [],
                    },
                    "courses_child_menu_category": {
                        "name": "Category",
                        "icon": "Layers",
                        "module": "courses",
                        "model": "courses.category",
                        "view_types": "list,form,kanban,graph,search",
                        "sequence": 2,
                    },
                    "courses_child_menu_subcategory": {
                        "name": "Sub Category",
                        "icon": "Layers",
                        "module": "courses",
                        "model": "courses.subcategory",
                        "view_types": "list,form,kanban,graph,search",
                        "sequence": 3,
                    },
                   
                }
            },
           

            "courses_child_menu_stage_menu": {
                "name": "stage",
                "icon": "Calendar",
                "module": "courses",
                # "model": "courses.stage",
                # "view_types": "list,form,kanban,graph,search",
                "sequence": 3,
                'actions' : [],
                "children": { 
                    "courses_child_menu_stage": {
                        "name": "stage",
                        "icon": "Calendar",
                        "module": "courses",
                        "model": "courses.stage",
                        "view_types": "list,form,kanban,graph,search",
                        "sequence": 1,
                        'actions' : [],
                    
                    },
                    "courses_child_menu_level": {
                        "name": "Level",
                        "icon": "TrendingUp",
                        "module": "courses",
                        "view_types": "list,form,kanban,graph,search",
                        "model": "courses.level",
                        "sequence": 2,
                    },
                    "courses_child_menu_subject": {
                        "name": "Subject",
                        "icon": "Target",
                        "module": "courses",
                        "model": "courses.subject",
                        "view_types": "list,form",
                        "sequence": 3,
                    },
                }
               
            },
           
            
        }
    }
}