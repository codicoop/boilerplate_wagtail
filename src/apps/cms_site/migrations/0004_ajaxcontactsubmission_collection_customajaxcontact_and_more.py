# Generated by Django 4.1.7 on 2023-03-02 10:57

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import uuid
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtaildocs", "0012_uploadeddocument"),
        ("wagtailcore", "0083_workflowcontenttype"),
        ("wagtail_ajax_contact_form", "0001_initial"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("cms_site", "0003_aboutuspage"),
    ]

    operations = [
        migrations.CreateModel(
            name="AjaxContactSubmission",
            fields=[
                (
                    "contactsubmission_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtail_ajax_contact_form.contactsubmission",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        blank=True, default="", max_length=120, verbose_name="subject"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, default="", max_length=120, verbose_name="phone"
                    ),
                ),
                (
                    "profile",
                    models.CharField(
                        blank=True, default="", max_length=120, verbose_name="profile"
                    ),
                ),
                (
                    "personal_data_auth",
                    models.BooleanField(
                        verbose_name="Treatment of personal data authorization"
                    ),
                ),
                (
                    "personal_data_comercial_auth",
                    models.BooleanField(
                        verbose_name="Treatment of personal data authorization for comercial purposes"
                    ),
                ),
            ],
            bases=("wagtail_ajax_contact_form.contactsubmission",),
        ),
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", verbose_name="Description"
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
                (
                    "pdf",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtaildocs.document",
                        verbose_name="Catalogue's PDF",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="CustomAjaxContact",
            fields=[
                (
                    "ajaxcontactpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtail_ajax_contact_form.ajaxcontactpage",
                    ),
                ),
                (
                    "menu_label",
                    models.CharField(
                        blank=True,
                        help_text="If not set, the menu title will be the page title.",
                        max_length=15,
                        null=True,
                        verbose_name="Menu title",
                    ),
                ),
                (
                    "subject_label",
                    models.CharField(
                        default="Subject",
                        help_text="Label for the Subject field.",
                        max_length=250,
                        verbose_name="subject",
                    ),
                ),
                (
                    "phone_label",
                    models.CharField(
                        default="Phone",
                        help_text="Label for the Phone field.",
                        max_length=250,
                        verbose_name="phone",
                    ),
                ),
                (
                    "profile_label",
                    models.CharField(
                        default="Profile",
                        help_text="Label for the Profile field.",
                        max_length=250,
                        verbose_name="profile",
                    ),
                ),
                (
                    "personal_data_auth_label",
                    models.CharField(
                        default="Treatment of personal data authorization",
                        help_text="Label for the Personal data treatment checkbox.",
                        max_length=250,
                        verbose_name="personal data treatment",
                    ),
                ),
                (
                    "personal_data_comercial_auth_label",
                    models.CharField(
                        default="Treatment of personal data authorization for comercial purposes",
                        help_text="Label for the Personal data for comercial use treatment checkbox.",
                        max_length=250,
                        verbose_name="personal data for comercial use treatment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact page",
            },
            bases=("wagtail_ajax_contact_form.ajaxcontactpage", models.Model),
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="body",
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_1_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_1_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Collection's page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_1_title",
            field=models.CharField(
                blank=True, default="", max_length=40, verbose_name="Title"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_2_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_2_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Collection's page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_2_title",
            field=models.CharField(
                blank=True, default="", max_length=40, verbose_name="Title"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_3_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_3_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Collection's page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="collection_3_title",
            field=models.CharField(
                blank=True, default="", max_length=40, verbose_name="Title"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="custom_projects_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="custom_projects_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Custom projects' page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="custom_projects_title",
            field=models.CharField(
                blank=True, default="", max_length=40, verbose_name="Title"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="display_header_highlight",
            field=models.BooleanField(
                default=True, verbose_name="Display header highlighted overlay"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="display_instagram_feed",
            field=models.BooleanField(
                default=True, verbose_name="Display Instagram feed section"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="header_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Header image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="overlay_body",
            field=models.TextField(blank=True, default="", verbose_name="Text"),
        ),
        migrations.AddField(
            model_name="homepage",
            name="overlay_button_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailcore.page",
                verbose_name="Linked page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="overlay_button_text",
            field=models.CharField(
                blank=True, default="", max_length=20, verbose_name="Button title"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="overlay_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="overlay_title",
            field=models.CharField(
                blank=True, default="", max_length=80, verbose_name="Title"
            ),
        ),
        migrations.CreateModel(
            name="VideoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(max_length=80, verbose_name="Title")),
                ("embed", models.TextField(verbose_name="Embed code")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_items",
                        to="cms_site.aboutuspage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SocialMediaIconsSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "facebook",
                    models.URLField(
                        blank=True,
                        default="https://www.facebook.com/moblesciurans",
                        help_text="Facebook URL",
                        null=True,
                    ),
                ),
                (
                    "youtube",
                    models.URLField(
                        blank=True,
                        default="http://www.youtube.com/user/ciuransmobles",
                        help_text="Youtube URL",
                        null=True,
                    ),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True,
                        default="https://www.instagram.com/ciuransmobles",
                        help_text="Instagram URL",
                        null=True,
                    ),
                ),
                (
                    "vimeo",
                    models.URLField(
                        blank=True,
                        default="https://vimeo.com/moblesciurans",
                        help_text="Vimeo URL",
                        null=True,
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NewsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="LegalPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("text", wagtail.fields.RichTextField(verbose_name="Text")),
                (
                    "header_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="InstagramPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="Example: https://www.instagram.com/p/CfyTUDfIxeY",
                        max_length=80,
                        verbose_name="Link to post",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="instagram_posts",
                        to="cms_site.newspage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HistoryItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("year", models.IntegerField(verbose_name="Year")),
                ("title", models.CharField(max_length=80, verbose_name="Title")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="history_items",
                        to="cms_site.aboutuspage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DesignersPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "designers_list",
                    wagtail.fields.StreamField(
                        [
                            (
                                "item",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "quote",
                                            wagtail.blocks.CharBlock(label="Quote"),
                                        ),
                                        (
                                            "name",
                                            wagtail.blocks.CharBlock(label="Name"),
                                        ),
                                        (
                                            "role",
                                            wagtail.blocks.CharBlock(
                                                help_text="I.e.: 'Area collection designer'",
                                                label="Role",
                                            ),
                                        ),
                                        (
                                            "description",
                                            wagtail.blocks.CharBlock(
                                                label="Description"
                                            ),
                                        ),
                                        (
                                            "photo",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                label="Photo"
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        use_json_field=True,
                        verbose_name="Compositions, renders and photos",
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="CustomProjectsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "menu_label",
                    models.CharField(
                        blank=True,
                        help_text="If not set, the menu title will be the page title.",
                        max_length=15,
                        null=True,
                        verbose_name="Menu title",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", verbose_name="description"
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="CustomProject",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", verbose_name="description"
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
                (
                    "images_collection",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="wagtailcore.collection",
                    ),
                ),
                (
                    "main_section_image",
                    models.ForeignKey(
                        help_text="This image will be used in the Custom Projects section, when displaying the list of projects.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Main section image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ContactDetailsSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        default="info@moblesciurans.com",
                        help_text="Contact e-mail",
                        max_length=254,
                        null=True,
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        blank=True,
                        default="C/ Priora Xixilona, 14<br>\n        08530 La Garriga<br>\n        Barcelona",
                        help_text="Address",
                        null=True,
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        default="93 871 80 07",
                        help_text="Phone number",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CollectionsPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "menu_label",
                    models.CharField(
                        blank=True,
                        help_text="If not set, the menu title will be the page title.",
                        max_length=15,
                        null=True,
                        verbose_name="Menu title",
                    ),
                ),
                (
                    "header_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Header image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="CollectionItemType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("title", models.CharField(max_length=255, verbose_name="name")),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "verbose_name": "Collection item type",
                "verbose_name_plural": "Collection item types",
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
        migrations.CreateModel(
            name="CollectionItemModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "verbose_name": "Collection item model",
                "verbose_name_plural": "Collection item models",
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
        migrations.CreateModel(
            name="CollectionItemFinishing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("title", models.CharField(max_length=255, verbose_name="name")),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "verbose_name": "Collection item finishing",
                "verbose_name_plural": "Collection item finishings",
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
        migrations.CreateModel(
            name="CollectionItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(max_length=80, verbose_name="Title")),
                (
                    "finishings",
                    modelcluster.fields.ParentalManyToManyField(
                        help_text='The finishing is not in the list? To add more, go to <a href="/cms/cms_site/collectionitemfinishing/" target="_blank">Finishings</a>.',
                        related_name="finishings",
                        to="cms_site.collectionitemfinishing",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Image",
                    ),
                ),
                (
                    "model",
                    models.ForeignKey(
                        help_text='The model is not in the list? To add more, go to <a href="/cms/cms_site/collectionitemmodel/" target="_blank">Models</a>.',
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cms_site.collectionitemmodel",
                        verbose_name="Model",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="collection_items",
                        to="cms_site.collection",
                    ),
                ),
                (
                    "typologies",
                    modelcluster.fields.ParentalManyToManyField(
                        help_text='The type is not in the list? To add more, go to <a href="/cms/cms_site/collectionitemtype/" target="_blank">Typologies</a>.',
                        related_name="typologies",
                        to="cms_site.collectionitemtype",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="aboutuspage",
            name="header_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Header image",
            ),
        ),
    ]
