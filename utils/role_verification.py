from fastapi import HTTPException


async def role_verification(user, function):
    allowed_functions_for_users = ["get_category", "get_science", 'get_option', "get_question",
                                   "get_answer", 'get_test_f', "add_result", "get_common_result",
                                   "get_file", 'create_file', 'delete_file', 'get_app_about',
                                   "get_me", "update_user", "delete_user",]

    allowed_functions_for_editor = ["get_category", "get_science", 'create_science', 'update_science',
                                    'delete_science', 'create_option', 'update_option', 'delete_option'
                                    'get_option', 'create_question', 'update_question', "get_question",
                                    'delete_question', 'add_answer', 'update_answer', 'delete_answer',
                                    "get_answer", 'add_result', 'get_test_f', "add_result",
                                    "get_common_result", 'get_result', 'get_db_file',
                                    "get_file", 'create_file', 'delete_file',
                                    "get_me", "update_user", "delete_user",]
    # routes dagi funksiyalar nomi beriladi

    if user.role == 'admin':
        return True

    elif user.role == 'editor' and function in allowed_functions_for_editor:
        return True
    elif user.role == "user" and function in allowed_functions_for_users:
        return True
    else:
        raise HTTPException(401, 'Sizga ruhsat berilmagan!')
