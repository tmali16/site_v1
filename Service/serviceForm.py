from django import forms

from Service.models import Service


class ServiceForm(forms.ModelForm):
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

    mbr = forms.CharField(required=False,label='Минет без презрватива', widget=forms.CheckboxInput())
    mbr_price = forms.CharField(required=False,label='Минет без презрватива', widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Сумма за услугу'}))
    anal_sex = forms.CharField(required=False,label='Анальный секс', widget=forms.CheckboxInput(attrs={}))
    anal_sex_price = forms.CharField(required=False,label='', widget=forms.TextInput(attrs={'class':'form-control form-control-sm disabled', 'placeholder':'Сумма за услугу'}))

    class Meta:
        model = Service
        fields = [
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