def success_response(data=None):
    return {
        "success": True,
        "data": data
    }


def error_response(msg):
    return {
        "success": False,
        "error": msg
    }