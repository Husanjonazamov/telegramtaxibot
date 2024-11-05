START = \
"""
<b>Assalomu alaykum {}!</b>
"""


def user_message_send(**kwargs):
    info = ''
    
    info += f"<b>{kwargs['text']}</b>\n\n"
    info += f"<b>@{kwargs['username']}</b>\n"
    
    return info
    