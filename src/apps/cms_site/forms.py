from apps.cms_site.models.contact import AjaxContactSubmission
from apps.wagtail_ajax_contact_form.forms import ContactUsForm


class ContactFormAjax(ContactUsForm):
    class Meta:
        model = AjaxContactSubmission
        fields = [
            "name",
            "email",
            "message",
            "subject",
            "phone",
            "profile",
            "personal_data_auth",
            "personal_data_comercial_auth",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["personal_data_auth"].required = True

    @staticmethod
    def get_body(post_data):
        body = f"""
        Nou e-mail de contacte rebut al formulari <br><br>
        Nom: {post_data['name']}<br>
        E-mail: {post_data['email']}<br>
        Telèfon: {post_data['phone']}<br>
        Perfil: {post_data['profile']}<br>
        Assumpte: {post_data['subject']}<br>
        Missatge:<br>
        {post_data['message']}<br><br>
        """
        return body
