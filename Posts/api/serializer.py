from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Posts.models import Post
from Service.models import Service


class PostSerializer(ModelSerializer):
    status = serializers.StringRelatedField()
    types = serializers.StringRelatedField()
    eye = serializers.StringRelatedField()
    hair = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = [
            "id",
            'name',
            'phone',
            'age',
            'height',
            'weight',
            'boob',
            'note',
            'eye',
            'types',
            'hair',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'image_5',
            'appart_1',
            'appart_2',
            'appart_naigth',
            'outside_1',
            'outside_2',
            'outside_nigth',
            'update',
            'status',
        ]


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "main_classic", "main_blowJob_w_condom", "main_cunni", "main_group_sex", "main_lesbi_lesbi",
            "mbr", "mbr_price", "anal_sex", "anal_sex_price",
            "dop_end_mouth", "dop_end_face", "dop_glub_minet", "dop_toys", "dop_role_game", "dop_couple_service",
            "dop_video", "dop_company",
            "massage_relax",
            "massage_classic",
            "massage_profi",
            "massage_tiski",
            "massage_prostat",
            "massage_erotic",
            "massage_sakura",
            "dance_profi",
            "dance_NoProfi",
            "dance_lesbi_show",
            "dance_lisbi",
            "sado_bandaj",
            "sado_gospoja",
            "sado_rabyn",
            "sado_dominant",
            "sado_porka",
            "sado_fetish",
            "sado_trampling",
            "extrim_anilingus",
            "extrim_dojd_out",
            "extrim_dojd_in",
            "extrim_strapon",
            "extrim_fisting_anal",
            "extrim_fisting_vagin",
                ]