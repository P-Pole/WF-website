# Generated by Django 3.2.13 on 2022-04-26 08:37

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0002_auto_20220426_0835"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navigationmenusetting",
            name="items",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "internal_page",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("title", wagtail.core.blocks.CharBlock()),
                                ("page", wagtail.core.blocks.PageChooserBlock()),
                                (
                                    "anchor",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "external_link",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("title", wagtail.core.blocks.CharBlock()),
                                ("url", wagtail.core.blocks.URLBlock()),
                                (
                                    "anchor",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "drop_down",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("title", wagtail.core.blocks.CharBlock()),
                                (
                                    "items",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.core.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.core.blocks.PageChooserBlock(),
                                                        ),
                                                        (
                                                            "anchor",
                                                            wagtail.core.blocks.CharBlock(
                                                                help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.core.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "url",
                                                            wagtail.core.blocks.URLBlock(),
                                                        ),
                                                        (
                                                            "anchor",
                                                            wagtail.core.blocks.CharBlock(
                                                                help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]