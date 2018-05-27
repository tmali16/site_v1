from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from Posts.models import *
from Service.models import Service


class pForm(forms.ModelForm):
    name = forms.CharField(required=True, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm inline', 'placeholder': 'Имя'}))
    phone = forms.CharField(required=True, label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Номер телефона'}))
    age = forms.CharField(required=True, label='Возраст', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Возраст'}))
    height = forms.CharField(required=True, label='Рост', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Рост'}))
    weight = forms.CharField(required=True, label='Вес', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Вес'}))
    boob = forms.CharField(required=True, label='Грудь', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Грудь'}))
    note = forms.CharField(required=False, label='описание', widget=forms.Textarea( attrs={'class': 'form-control form-control-sm', 'rows': '4', 'placeholder': 'описание'}))
    eye = forms.ModelChoiceField(queryset=eyes.objects.all(), required=False, label='глаза', widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    types = forms.ModelChoiceField(queryset=types.objects.all(), required=False, label='Тип', widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    hair = forms.ModelChoiceField(queryset=haire.objects.all(), required=False, label='Волосы', widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    image_1 = forms.ImageField(required=True, label='Фото 1')
    image_2 = forms.ImageField(required=False, label='Фото 2')
    image_3 = forms.ImageField(required=False, label='Фото 3')
    image_4 = forms.ImageField(required=False, label='Фото 4')
    image_5 = forms.ImageField(required=False, label='Фото 5')

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(pForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = [
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
            'image_5'
        ]


class ServiceForm(forms.ModelForm):
    appart_1 = forms.CharField(label='1-Час',required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    appart_2 = forms.CharField(label='2-Часа',required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    appart_naigth = forms.CharField(label='Ночь',required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    outside_1 = forms.CharField(label='1-Час',required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    outside_2 = forms.CharField(label='2-аса',required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    outside_nigth = forms.CharField(label='Ноь',required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))

    main_classic = forms.CharField(required=False,label='Класический ', widget=forms.CheckboxInput())
    main_blowJob_w_condom = forms.CharField(required=False,label='Минет с презирвативом', widget=forms.CheckboxInput())
    main_cunni = forms.CharField(required=False,label='Кунилингус', widget=forms.CheckboxInput())
    main_group_sex = forms.CharField(required=False,label='Групповой секс', widget=forms.CheckboxInput())
    main_lesbi_lesbi = forms.CharField(required=False,label='Лесбийский секс', widget=forms.CheckboxInput(attrs={'class':''}))

    dop_end_mouth = forms.CharField(required=False,label='Кончить в рот', widget=forms.CheckboxInput())
    dop_end_face = forms.CharField(required=False,label='Кончить на лицо', widget=forms.CheckboxInput())
    dop_glub_minet = forms.CharField(required=False,label='Глубокий минет', widget=forms.CheckboxInput())
    dop_toys = forms.CharField(required=False,label='Игрушки', widget=forms.CheckboxInput())
    dop_role_game = forms.CharField(required=False,label='Ролевые игры', widget=forms.CheckboxInput())
    dop_couple_service = forms.CharField(required=False,label='Услиги супружиским парам', widget=forms.CheckboxInput())
    dop_video = forms.CharField(required=False,label='Фото/Видео съемки', widget=forms.CheckboxInput())
    dop_company = forms.CharField(required=False,label='Сопровождение', widget=forms.CheckboxInput())

    massage_relax = forms.CharField(required=False,label='Раслобляющий массаж', widget=forms.CheckboxInput())
    massage_classic = forms.CharField(required=False,label='Классический массаж', widget=forms.CheckboxInput())
    massage_profi = forms.CharField(required=False,label='Проффесиональный массаж', widget=forms.CheckboxInput())
    massage_tiski = forms.CharField(required=False,label='Тайский массаж', widget=forms.CheckboxInput())
    massage_prostat = forms.CharField(required=False,label='Массаж простаты', widget=forms.CheckboxInput())
    massage_erotic = forms.CharField(required=False,label='Эротический массаж', widget=forms.CheckboxInput())
    massage_sakura = forms.CharField(required=False,label='Ветка сакуры', widget=forms.CheckboxInput())

    dance_profi = forms.CharField(required=False,label='Стритиз проффесиональный', widget=forms.CheckboxInput())
    dance_NoProfi = forms.CharField(required=False,label='Стриптиз не профи', widget=forms.CheckboxInput())
    dance_lesbi_show = forms.CharField(required=False,label='Откровенное лесби-шоу', widget=forms.CheckboxInput())
    dance_lisbi = forms.CharField(required=False,label='Легкое лесби шоу', widget=forms.CheckboxInput())

    sado_bandaj = forms.CharField(required=False,label='Бандаж', widget=forms.CheckboxInput())
    sado_gospoja = forms.CharField(required=False,label='Госпожа', widget=forms.CheckboxInput())
    sado_rabyn = forms.CharField(required=False,label='Рабыня', widget=forms.CheckboxInput())
    sado_dominant = forms.CharField(required=False,label='Лекая доминация', widget=forms.CheckboxInput())
    sado_porka = forms.CharField(required=False,label='Порка', widget=forms.CheckboxInput())
    sado_fetish = forms.CharField(required=False,label='Фетиш', widget=forms.CheckboxInput())
    sado_trampling = forms.CharField(required=False,label='Трамплинг', widget=forms.CheckboxInput())

    extrim_anilingus = forms.CharField(required=False,label='Анилингус', widget=forms.CheckboxInput())
    extrim_dojd_out = forms.CharField(required=False,label='Золой дождь выдача', widget=forms.CheckboxInput())
    extrim_dojd_in = forms.CharField(required=False,label='Золотой дождь прием', widget=forms.CheckboxInput())
    extrim_strapon = forms.CharField(required=False,label='Страпон', widget=forms.CheckboxInput())
    extrim_fisting_anal = forms.CharField(required=False,label='Фистинг анальный', widget=forms.CheckboxInput())
    extrim_fisting_vagin = forms.CharField(required=False,label='Фистинг вагинальный', widget=forms.CheckboxInput())

    mbr = forms.CharField(required=False,label='Миньет без призерватива', widget=forms.CheckboxInput())
    mbr_price = forms.CharField(required=False,label='', widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Сумма за услугу'}))
    anal_sex = forms.CharField(required=False,label='Анальный секс', widget=forms.CheckboxInput(attrs={'onclick':''}))
    anal_sex_price = forms.CharField(required=False,label='', widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Сумма за услугу'}))

    class Meta:
        model = Service
        fields = [
            'appart_1',
            'appart_2',
            'appart_naigth',
            'outside_1',
            'outside_2',
            'outside_nigth',
            # -----------------------------
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