from .utils import send_email

def send_verification_email(email, auth_token, domain_name):
    subject = "Confirm password"
    # Objet: Confirmation de votre inscription sur AutoPrep
    # Cher/Chère [user name],
    message = f'''
{domain_name}/accounts/verify_email/{auth_token}/


'''
    send_email(subject=subject, message=message, email=email)


def send_change_password_email(email, auth_token, domain_name):
    subject = "Change password"
    message = f'''
{domain_name}/accounts/change_password/{email}/{auth_token}/

'''
    send_email(subject=subject, message=message, email=email)
