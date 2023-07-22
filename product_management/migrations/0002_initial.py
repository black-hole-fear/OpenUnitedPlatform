# Generated by Django 4.2.2 on 2023-07-22 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("talent", "0001_initial"),
        ("security", "0001_initial"),
        ("product_management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productrole",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.person"
            ),
        ),
        migrations.AddField(
            model_name="productrole",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="productchallenge",
            name="challenge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.challenge",
            ),
        ),
        migrations.AddField(
            model_name="productchallenge",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="attachment",
            field=models.ManyToManyField(
                blank=True,
                related_name="product_attachments",
                to="product_management.attachment",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="capability_start",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.capability",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="security.productowner",
            ),
        ),
        migrations.AddField(
            model_name="initiative",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="contributorguide",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_contributor_guide",
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="contributorguide",
            name="skill",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category_contributor_guide",
                to="talent.skill",
            ),
        ),
        migrations.AddField(
            model_name="contributoragreementacceptance",
            name="agreement",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.contributoragreement",
            ),
        ),
        migrations.AddField(
            model_name="contributoragreementacceptance",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="person_contributor_agreement_acceptance",
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="contributoragreement",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_contributor_agreement",
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="challengelisting",
            name="assigned_to_person",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="challenge_listing",
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="challengelisting",
            name="capability",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product_management.capability",
            ),
        ),
        migrations.AddField(
            model_name="challengelisting",
            name="challenge",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.challenge",
            ),
        ),
        migrations.AddField(
            model_name="challengelisting",
            name="initiative",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product_management.initiative",
            ),
        ),
        migrations.AddField(
            model_name="challengelisting",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="challengelisting",
            name="task_creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="creator",
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="challengedependency",
            name="preceding_challenge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.challenge",
            ),
        ),
        migrations.AddField(
            model_name="challengedependency",
            name="subsequent_challenge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Challenge",
                to="product_management.challenge",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="attachment",
            field=models.ManyToManyField(
                blank=True,
                related_name="challenge_attachements",
                to="product_management.attachment",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="capability",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product_management.capability",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="comments_start",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="talent.challengecomment",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="contribution_guide",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product_management.contributorguide",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_by",
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="expertise",
            field=models.ManyToManyField(
                related_name="challenge_expertise", to="talent.expertise"
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="initiative",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product_management.initiative",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="reviewer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="skill",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="challenge",
                to="talent.skill",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="tag",
            field=models.ManyToManyField(
                blank=True, related_name="challenge_tags", to="product_management.tag"
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="updated_by",
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="capabilityattachment",
            name="attachment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.attachment",
            ),
        ),
        migrations.AddField(
            model_name="capabilityattachment",
            name="capability",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.capability",
            ),
        ),
        migrations.AddField(
            model_name="capability",
            name="comments_start",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="talent.capabilitycomment",
            ),
        ),
        migrations.AddField(
            model_name="bounty",
            name="challenge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.challenge",
            ),
        ),
        migrations.AddField(
            model_name="bounty",
            name="expertise",
            field=models.ManyToManyField(
                related_name="bounty_expertise", to="talent.expertise"
            ),
        ),
        migrations.AddField(
            model_name="bounty",
            name="skill",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bounty_skill",
                to="talent.skill",
            ),
        ),
    ]
