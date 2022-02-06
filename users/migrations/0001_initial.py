# Generated by Django 3.2.8 on 2022-02-06 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tasks_api.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('profile', models.ImageField(blank=True, upload_to=tasks_api.utils.upload_file)),
                ('inviteSlug', models.SlugField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_owner', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(default='profile.jpg', upload_to=tasks_api.utils.upload_file)),
                ('header', models.ImageField(default='header.jpg', upload_to=tasks_api.utils.upload_file)),
                ('timezone', models.CharField(choices=[('0', 'Africa/Abidjan'), ('1', 'Africa/Accra'), ('2', 'Africa/Addis_Ababa'), ('3', 'Africa/Algiers'), ('4', 'Africa/Asmara'), ('5', 'Africa/Asmera'), ('6', 'Africa/Bamako'), ('7', 'Africa/Bangui'), ('8', 'Africa/Banjul'), ('9', 'Africa/Bissau'), ('10', 'Africa/Blantyre'), ('11', 'Africa/Brazzaville'), ('12', 'Africa/Bujumbura'), ('13', 'Africa/Cairo'), ('14', 'Africa/Casablanca'), ('15', 'Africa/Ceuta'), ('16', 'Africa/Conakry'), ('17', 'Africa/Dakar'), ('18', 'Africa/Dar_es_Salaam'), ('19', 'Africa/Djibouti'), ('20', 'Africa/Douala'), ('21', 'Africa/El_Aaiun'), ('22', 'Africa/Freetown'), ('23', 'Africa/Gaborone'), ('24', 'Africa/Harare'), ('25', 'Africa/Johannesburg'), ('26', 'Africa/Juba'), ('27', 'Africa/Kampala'), ('28', 'Africa/Khartoum'), ('29', 'Africa/Kigali'), ('30', 'Africa/Kinshasa'), ('31', 'Africa/Lagos'), ('32', 'Africa/Libreville'), ('33', 'Africa/Lome'), ('34', 'Africa/Luanda'), ('35', 'Africa/Lubumbashi'), ('36', 'Africa/Lusaka'), ('37', 'Africa/Malabo'), ('38', 'Africa/Maputo'), ('39', 'Africa/Maseru'), ('40', 'Africa/Mbabane'), ('41', 'Africa/Mogadishu'), ('42', 'Africa/Monrovia'), ('43', 'Africa/Nairobi'), ('44', 'Africa/Ndjamena'), ('45', 'Africa/Niamey'), ('46', 'Africa/Nouakchott'), ('47', 'Africa/Ouagadougou'), ('48', 'Africa/Porto-Novo'), ('49', 'Africa/Sao_Tome'), ('50', 'Africa/Timbuktu'), ('51', 'Africa/Tripoli'), ('52', 'Africa/Tunis'), ('53', 'Africa/Windhoek'), ('54', 'America/Adak'), ('55', 'America/Anchorage'), ('56', 'America/Anguilla'), ('57', 'America/Antigua'), ('58', 'America/Araguaina'), ('59', 'America/Argentina/Buenos_Aires'), ('60', 'America/Argentina/Catamarca'), ('61', 'America/Argentina/ComodRivadavia'), ('62', 'America/Argentina/Cordoba'), ('63', 'America/Argentina/Jujuy'), ('64', 'America/Argentina/La_Rioja'), ('65', 'America/Argentina/Mendoza'), ('66', 'America/Argentina/Rio_Gallegos'), ('67', 'America/Argentina/Salta'), ('68', 'America/Argentina/San_Juan'), ('69', 'America/Argentina/San_Luis'), ('70', 'America/Argentina/Tucuman'), ('71', 'America/Argentina/Ushuaia'), ('72', 'America/Aruba'), ('73', 'America/Asuncion'), ('74', 'America/Atikokan'), ('75', 'America/Atka'), ('76', 'America/Bahia'), ('77', 'America/Bahia_Banderas'), ('78', 'America/Barbados'), ('79', 'America/Belem'), ('80', 'America/Belize'), ('81', 'America/Blanc-Sablon'), ('82', 'America/Boa_Vista'), ('83', 'America/Bogota'), ('84', 'America/Boise'), ('85', 'America/Buenos_Aires'), ('86', 'America/Cambridge_Bay'), ('87', 'America/Campo_Grande'), ('88', 'America/Cancun'), ('89', 'America/Caracas'), ('90', 'America/Catamarca'), ('91', 'America/Cayenne'), ('92', 'America/Cayman'), ('93', 'America/Chicago'), ('94', 'America/Chihuahua'), ('95', 'America/Coral_Harbour'), ('96', 'America/Cordoba'), ('97', 'America/Costa_Rica'), ('98', 'America/Creston'), ('99', 'America/Cuiaba'), ('100', 'America/Curacao'), ('101', 'America/Danmarkshavn'), ('102', 'America/Dawson'), ('103', 'America/Dawson_Creek'), ('104', 'America/Denver'), ('105', 'America/Detroit'), ('106', 'America/Dominica'), ('107', 'America/Edmonton'), ('108', 'America/Eirunepe'), ('109', 'America/El_Salvador'), ('110', 'America/Ensenada'), ('111', 'America/Fort_Nelson'), ('112', 'America/Fort_Wayne'), ('113', 'America/Fortaleza'), ('114', 'America/Glace_Bay'), ('115', 'America/Godthab'), ('116', 'America/Goose_Bay'), ('117', 'America/Grand_Turk'), ('118', 'America/Grenada'), ('119', 'America/Guadeloupe'), ('120', 'America/Guatemala'), ('121', 'America/Guayaquil'), ('122', 'America/Guyana'), ('123', 'America/Halifax'), ('124', 'America/Havana'), ('125', 'America/Hermosillo'), ('126', 'America/Indiana/Indianapolis'), ('127', 'America/Indiana/Knox'), ('128', 'America/Indiana/Marengo'), ('129', 'America/Indiana/Petersburg'), ('130', 'America/Indiana/Tell_City'), ('131', 'America/Indiana/Vevay'), ('132', 'America/Indiana/Vincennes'), ('133', 'America/Indiana/Winamac'), ('134', 'America/Indianapolis'), ('135', 'America/Inuvik'), ('136', 'America/Iqaluit'), ('137', 'America/Jamaica'), ('138', 'America/Jujuy'), ('139', 'America/Juneau'), ('140', 'America/Kentucky/Louisville'), ('141', 'America/Kentucky/Monticello'), ('142', 'America/Knox_IN'), ('143', 'America/Kralendijk'), ('144', 'America/La_Paz'), ('145', 'America/Lima'), ('146', 'America/Los_Angeles'), ('147', 'America/Louisville'), ('148', 'America/Lower_Princes'), ('149', 'America/Maceio'), ('150', 'America/Managua'), ('151', 'America/Manaus'), ('152', 'America/Marigot'), ('153', 'America/Martinique'), ('154', 'America/Matamoros'), ('155', 'America/Mazatlan'), ('156', 'America/Mendoza'), ('157', 'America/Menominee'), ('158', 'America/Merida'), ('159', 'America/Metlakatla'), ('160', 'America/Mexico_City'), ('161', 'America/Miquelon'), ('162', 'America/Moncton'), ('163', 'America/Monterrey'), ('164', 'America/Montevideo'), ('165', 'America/Montreal'), ('166', 'America/Montserrat'), ('167', 'America/Nassau'), ('168', 'America/New_York'), ('169', 'America/Nipigon'), ('170', 'America/Nome'), ('171', 'America/Noronha'), ('172', 'America/North_Dakota/Beulah'), ('173', 'America/North_Dakota/Center'), ('174', 'America/North_Dakota/New_Salem'), ('175', 'America/Nuuk'), ('176', 'America/Ojinaga'), ('177', 'America/Panama'), ('178', 'America/Pangnirtung'), ('179', 'America/Paramaribo'), ('180', 'America/Phoenix'), ('181', 'America/Port-au-Prince'), ('182', 'America/Port_of_Spain'), ('183', 'America/Porto_Acre'), ('184', 'America/Porto_Velho'), ('185', 'America/Puerto_Rico'), ('186', 'America/Punta_Arenas'), ('187', 'America/Rainy_River'), ('188', 'America/Rankin_Inlet'), ('189', 'America/Recife'), ('190', 'America/Regina'), ('191', 'America/Resolute'), ('192', 'America/Rio_Branco'), ('193', 'America/Rosario'), ('194', 'America/Santa_Isabel'), ('195', 'America/Santarem'), ('196', 'America/Santiago'), ('197', 'America/Santo_Domingo'), ('198', 'America/Sao_Paulo'), ('199', 'America/Scoresbysund'), ('200', 'America/Shiprock'), ('201', 'America/Sitka'), ('202', 'America/St_Barthelemy'), ('203', 'America/St_Johns'), ('204', 'America/St_Kitts'), ('205', 'America/St_Lucia'), ('206', 'America/St_Thomas'), ('207', 'America/St_Vincent'), ('208', 'America/Swift_Current'), ('209', 'America/Tegucigalpa'), ('210', 'America/Thule'), ('211', 'America/Thunder_Bay'), ('212', 'America/Tijuana'), ('213', 'America/Toronto'), ('214', 'America/Tortola'), ('215', 'America/Vancouver'), ('216', 'America/Virgin'), ('217', 'America/Whitehorse'), ('218', 'America/Winnipeg'), ('219', 'America/Yakutat'), ('220', 'America/Yellowknife'), ('221', 'Antarctica/Casey'), ('222', 'Antarctica/Davis'), ('223', 'Antarctica/DumontDUrville'), ('224', 'Antarctica/Macquarie'), ('225', 'Antarctica/Mawson'), ('226', 'Antarctica/McMurdo'), ('227', 'Antarctica/Palmer'), ('228', 'Antarctica/Rothera'), ('229', 'Antarctica/South_Pole'), ('230', 'Antarctica/Syowa'), ('231', 'Antarctica/Troll'), ('232', 'Antarctica/Vostok'), ('233', 'Arctic/Longyearbyen'), ('234', 'Asia/Aden'), ('235', 'Asia/Almaty'), ('236', 'Asia/Amman'), ('237', 'Asia/Anadyr'), ('238', 'Asia/Aqtau'), ('239', 'Asia/Aqtobe'), ('240', 'Asia/Ashgabat'), ('241', 'Asia/Ashkhabad'), ('242', 'Asia/Atyrau'), ('243', 'Asia/Baghdad'), ('244', 'Asia/Bahrain'), ('245', 'Asia/Baku'), ('246', 'Asia/Bangkok'), ('247', 'Asia/Barnaul'), ('248', 'Asia/Beirut'), ('249', 'Asia/Bishkek'), ('250', 'Asia/Brunei'), ('251', 'Asia/Calcutta'), ('252', 'Asia/Chita'), ('253', 'Asia/Choibalsan'), ('254', 'Asia/Chongqing'), ('255', 'Asia/Chungking'), ('256', 'Asia/Colombo'), ('257', 'Asia/Dacca'), ('258', 'Asia/Damascus'), ('259', 'Asia/Dhaka'), ('260', 'Asia/Dili'), ('261', 'Asia/Dubai'), ('262', 'Asia/Dushanbe'), ('263', 'Asia/Famagusta'), ('264', 'Asia/Gaza'), ('265', 'Asia/Harbin'), ('266', 'Asia/Hebron'), ('267', 'Asia/Ho_Chi_Minh'), ('268', 'Asia/Hong_Kong'), ('269', 'Asia/Hovd'), ('270', 'Asia/Irkutsk'), ('271', 'Asia/Istanbul'), ('272', 'Asia/Jakarta'), ('273', 'Asia/Jayapura'), ('274', 'Asia/Jerusalem'), ('275', 'Asia/Kabul'), ('276', 'Asia/Kamchatka'), ('277', 'Asia/Karachi'), ('278', 'Asia/Kashgar'), ('279', 'Asia/Kathmandu'), ('280', 'Asia/Katmandu'), ('281', 'Asia/Khandyga'), ('282', 'Asia/Kolkata'), ('283', 'Asia/Krasnoyarsk'), ('284', 'Asia/Kuala_Lumpur'), ('285', 'Asia/Kuching'), ('286', 'Asia/Kuwait'), ('287', 'Asia/Macao'), ('288', 'Asia/Macau'), ('289', 'Asia/Magadan'), ('290', 'Asia/Makassar'), ('291', 'Asia/Manila'), ('292', 'Asia/Muscat'), ('293', 'Asia/Nicosia'), ('294', 'Asia/Novokuznetsk'), ('295', 'Asia/Novosibirsk'), ('296', 'Asia/Omsk'), ('297', 'Asia/Oral'), ('298', 'Asia/Phnom_Penh'), ('299', 'Asia/Pontianak'), ('300', 'Asia/Pyongyang'), ('301', 'Asia/Qatar'), ('302', 'Asia/Qostanay'), ('303', 'Asia/Qyzylorda'), ('304', 'Asia/Rangoon'), ('305', 'Asia/Riyadh'), ('306', 'Asia/Saigon'), ('307', 'Asia/Sakhalin'), ('308', 'Asia/Samarkand'), ('309', 'Asia/Seoul'), ('310', 'Asia/Shanghai'), ('311', 'Asia/Singapore'), ('312', 'Asia/Srednekolymsk'), ('313', 'Asia/Taipei'), ('314', 'Asia/Tashkent'), ('315', 'Asia/Tbilisi'), ('316', 'Asia/Tehran'), ('317', 'Asia/Tel_Aviv'), ('318', 'Asia/Thimbu'), ('319', 'Asia/Thimphu'), ('320', 'Asia/Tokyo'), ('321', 'Asia/Tomsk'), ('322', 'Asia/Ujung_Pandang'), ('323', 'Asia/Ulaanbaatar'), ('324', 'Asia/Ulan_Bator'), ('325', 'Asia/Urumqi'), ('326', 'Asia/Ust-Nera'), ('327', 'Asia/Vientiane'), ('328', 'Asia/Vladivostok'), ('329', 'Asia/Yakutsk'), ('330', 'Asia/Yangon'), ('331', 'Asia/Yekaterinburg'), ('332', 'Asia/Yerevan'), ('333', 'Atlantic/Azores'), ('334', 'Atlantic/Bermuda'), ('335', 'Atlantic/Canary'), ('336', 'Atlantic/Cape_Verde'), ('337', 'Atlantic/Faeroe'), ('338', 'Atlantic/Faroe'), ('339', 'Atlantic/Jan_Mayen'), ('340', 'Atlantic/Madeira'), ('341', 'Atlantic/Reykjavik'), ('342', 'Atlantic/South_Georgia'), ('343', 'Atlantic/St_Helena'), ('344', 'Atlantic/Stanley'), ('345', 'Australia/ACT'), ('346', 'Australia/Adelaide'), ('347', 'Australia/Brisbane'), ('348', 'Australia/Broken_Hill'), ('349', 'Australia/Canberra'), ('350', 'Australia/Currie'), ('351', 'Australia/Darwin'), ('352', 'Australia/Eucla'), ('353', 'Australia/Hobart'), ('354', 'Australia/LHI'), ('355', 'Australia/Lindeman'), ('356', 'Australia/Lord_Howe'), ('357', 'Australia/Melbourne'), ('358', 'Australia/NSW'), ('359', 'Australia/North'), ('360', 'Australia/Perth'), ('361', 'Australia/Queensland'), ('362', 'Australia/South'), ('363', 'Australia/Sydney'), ('364', 'Australia/Tasmania'), ('365', 'Australia/Victoria'), ('366', 'Australia/West'), ('367', 'Australia/Yancowinna'), ('368', 'Brazil/Acre'), ('369', 'Brazil/DeNoronha'), ('370', 'Brazil/East'), ('371', 'Brazil/West'), ('372', 'CET'), ('373', 'CST6CDT'), ('374', 'Canada/Atlantic'), ('375', 'Canada/Central'), ('376', 'Canada/Eastern'), ('377', 'Canada/Mountain'), ('378', 'Canada/Newfoundland'), ('379', 'Canada/Pacific'), ('380', 'Canada/Saskatchewan'), ('381', 'Canada/Yukon'), ('382', 'Chile/Continental'), ('383', 'Chile/EasterIsland'), ('384', 'Cuba'), ('385', 'EET'), ('386', 'EST'), ('387', 'EST5EDT'), ('388', 'Egypt'), ('389', 'Eire'), ('390', 'Etc/GMT'), ('391', 'Etc/GMT+0'), ('392', 'Etc/GMT+1'), ('393', 'Etc/GMT+10'), ('394', 'Etc/GMT+11'), ('395', 'Etc/GMT+12'), ('396', 'Etc/GMT+2'), ('397', 'Etc/GMT+3'), ('398', 'Etc/GMT+4'), ('399', 'Etc/GMT+5'), ('400', 'Etc/GMT+6'), ('401', 'Etc/GMT+7'), ('402', 'Etc/GMT+8'), ('403', 'Etc/GMT+9'), ('404', 'Etc/GMT-0'), ('405', 'Etc/GMT-1'), ('406', 'Etc/GMT-10'), ('407', 'Etc/GMT-11'), ('408', 'Etc/GMT-12'), ('409', 'Etc/GMT-13'), ('410', 'Etc/GMT-14'), ('411', 'Etc/GMT-2'), ('412', 'Etc/GMT-3'), ('413', 'Etc/GMT-4'), ('414', 'Etc/GMT-5'), ('415', 'Etc/GMT-6'), ('416', 'Etc/GMT-7'), ('417', 'Etc/GMT-8'), ('418', 'Etc/GMT-9'), ('419', 'Etc/GMT0'), ('420', 'Etc/Greenwich'), ('421', 'Etc/UCT'), ('422', 'Etc/UTC'), ('423', 'Etc/Universal'), ('424', 'Etc/Zulu'), ('425', 'Europe/Amsterdam'), ('426', 'Europe/Andorra'), ('427', 'Europe/Astrakhan'), ('428', 'Europe/Athens'), ('429', 'Europe/Belfast'), ('430', 'Europe/Belgrade'), ('431', 'Europe/Berlin'), ('432', 'Europe/Bratislava'), ('433', 'Europe/Brussels'), ('434', 'Europe/Bucharest'), ('435', 'Europe/Budapest'), ('436', 'Europe/Busingen'), ('437', 'Europe/Chisinau'), ('438', 'Europe/Copenhagen'), ('439', 'Europe/Dublin'), ('440', 'Europe/Gibraltar'), ('441', 'Europe/Guernsey'), ('442', 'Europe/Helsinki'), ('443', 'Europe/Isle_of_Man'), ('444', 'Europe/Istanbul'), ('445', 'Europe/Jersey'), ('446', 'Europe/Kaliningrad'), ('447', 'Europe/Kiev'), ('448', 'Europe/Kirov'), ('449', 'Europe/Lisbon'), ('450', 'Europe/Ljubljana'), ('451', 'Europe/London'), ('452', 'Europe/Luxembourg'), ('453', 'Europe/Madrid'), ('454', 'Europe/Malta'), ('455', 'Europe/Mariehamn'), ('456', 'Europe/Minsk'), ('457', 'Europe/Monaco'), ('458', 'Europe/Moscow'), ('459', 'Europe/Nicosia'), ('460', 'Europe/Oslo'), ('461', 'Europe/Paris'), ('462', 'Europe/Podgorica'), ('463', 'Europe/Prague'), ('464', 'Europe/Riga'), ('465', 'Europe/Rome'), ('466', 'Europe/Samara'), ('467', 'Europe/San_Marino'), ('468', 'Europe/Sarajevo'), ('469', 'Europe/Saratov'), ('470', 'Europe/Simferopol'), ('471', 'Europe/Skopje'), ('472', 'Europe/Sofia'), ('473', 'Europe/Stockholm'), ('474', 'Europe/Tallinn'), ('475', 'Europe/Tirane'), ('476', 'Europe/Tiraspol'), ('477', 'Europe/Ulyanovsk'), ('478', 'Europe/Uzhgorod'), ('479', 'Europe/Vaduz'), ('480', 'Europe/Vatican'), ('481', 'Europe/Vienna'), ('482', 'Europe/Vilnius'), ('483', 'Europe/Volgograd'), ('484', 'Europe/Warsaw'), ('485', 'Europe/Zagreb'), ('486', 'Europe/Zaporozhye'), ('487', 'Europe/Zurich'), ('488', 'GB'), ('489', 'GB-Eire'), ('490', 'GMT'), ('491', 'GMT+0'), ('492', 'GMT-0'), ('493', 'GMT0'), ('494', 'Greenwich'), ('495', 'HST'), ('496', 'Hongkong'), ('497', 'Iceland'), ('498', 'Indian/Antananarivo'), ('499', 'Indian/Chagos'), ('500', 'Indian/Christmas'), ('501', 'Indian/Cocos'), ('502', 'Indian/Comoro'), ('503', 'Indian/Kerguelen'), ('504', 'Indian/Mahe'), ('505', 'Indian/Maldives'), ('506', 'Indian/Mauritius'), ('507', 'Indian/Mayotte'), ('508', 'Indian/Reunion'), ('509', 'Iran'), ('510', 'Israel'), ('511', 'Jamaica'), ('512', 'Japan'), ('513', 'Kwajalein'), ('514', 'Libya'), ('515', 'MET'), ('516', 'MST'), ('517', 'MST7MDT'), ('518', 'Mexico/BajaNorte'), ('519', 'Mexico/BajaSur'), ('520', 'Mexico/General'), ('521', 'NZ'), ('522', 'NZ-CHAT'), ('523', 'Navajo'), ('524', 'PRC'), ('525', 'PST8PDT'), ('526', 'Pacific/Apia'), ('527', 'Pacific/Auckland'), ('528', 'Pacific/Bougainville'), ('529', 'Pacific/Chatham'), ('530', 'Pacific/Chuuk'), ('531', 'Pacific/Easter'), ('532', 'Pacific/Efate'), ('533', 'Pacific/Enderbury'), ('534', 'Pacific/Fakaofo'), ('535', 'Pacific/Fiji'), ('536', 'Pacific/Funafuti'), ('537', 'Pacific/Galapagos'), ('538', 'Pacific/Gambier'), ('539', 'Pacific/Guadalcanal'), ('540', 'Pacific/Guam'), ('541', 'Pacific/Honolulu'), ('542', 'Pacific/Johnston'), ('543', 'Pacific/Kanton'), ('544', 'Pacific/Kiritimati'), ('545', 'Pacific/Kosrae'), ('546', 'Pacific/Kwajalein'), ('547', 'Pacific/Majuro'), ('548', 'Pacific/Marquesas'), ('549', 'Pacific/Midway'), ('550', 'Pacific/Nauru'), ('551', 'Pacific/Niue'), ('552', 'Pacific/Norfolk'), ('553', 'Pacific/Noumea'), ('554', 'Pacific/Pago_Pago'), ('555', 'Pacific/Palau'), ('556', 'Pacific/Pitcairn'), ('557', 'Pacific/Pohnpei'), ('558', 'Pacific/Ponape'), ('559', 'Pacific/Port_Moresby'), ('560', 'Pacific/Rarotonga'), ('561', 'Pacific/Saipan'), ('562', 'Pacific/Samoa'), ('563', 'Pacific/Tahiti'), ('564', 'Pacific/Tarawa'), ('565', 'Pacific/Tongatapu'), ('566', 'Pacific/Truk'), ('567', 'Pacific/Wake'), ('568', 'Pacific/Wallis'), ('569', 'Pacific/Yap'), ('570', 'Poland'), ('571', 'Portugal'), ('572', 'ROC'), ('573', 'ROK'), ('574', 'Singapore'), ('575', 'Turkey'), ('576', 'UCT'), ('577', 'US/Alaska'), ('578', 'US/Aleutian'), ('579', 'US/Arizona'), ('580', 'US/Central'), ('581', 'US/East-Indiana'), ('582', 'US/Eastern'), ('583', 'US/Hawaii'), ('584', 'US/Indiana-Starke'), ('585', 'US/Michigan'), ('586', 'US/Mountain'), ('587', 'US/Pacific'), ('588', 'US/Samoa'), ('589', 'UTC'), ('590', 'Universal'), ('591', 'W-SU'), ('592', 'WET'), ('593', 'Zulu')], default='589', max_length=3)),
                ('setting', models.JSONField(blank=True, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='setting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
