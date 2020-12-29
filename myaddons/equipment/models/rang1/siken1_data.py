# -*- coding: utf-8 -*-
"""
@Time    : 12/23/2020 10:00 PM
@Author  : yuanlixiang
@description: RANG量程
"""
from odoo import models, fields, api


class Siken1_Data(models.Model):
    _name = 'siken1.data'
    _description = 'Siken Data'

    kiban = fields.Char(string='设备编号')  # 機器番号
    seiban = fields.Char(string='制番/POS')  # 製番／ＰＯＳ
    bodyno = fields.Char(string='bodyno')
    sdata00 = fields.Float(string='测量点1(%值)平台点0～100%')  # 測定点１(%値) ﾃｽﾄ点0～100%
    sdata01 = fields.Float(string='测量点2(%值)平台点0～100%')  # 測定点2(%値) ﾃｽﾄ点0～100%
    sdata02 = fields.Float(string='测量点3(%值)平台点0～100%')  # 測定点3(%値) ﾃｽﾄ点0～100%
    sdata03 = fields.Float(string='测量点4(%值)平台点0～100%')  # 測定点4(%値) ﾃｽﾄ点0～100%
    sdata04 = fields.Float(string='测量点5(%值)平台点0～100%')  # 測定点5(%値) ﾃｽﾄ点0～100%
    sdata05 = fields.Float(string='测量点6(%值)平台点0～100%')  # 測定点6(%値) ﾃｽﾄ点0～100%
    sdata06 = fields.Float(string='测量点7(%值)平台点0～100%')  # 測定点7(%値) ﾃｽﾄ点0～100%
    sdata07 = fields.Float(string='Master输出值1(%值)UP平台点0～100%')  # ﾏｽﾀｰ出力値１(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata08 = fields.Float(string='Master输出值2(%值)UP平台点0～100%')  # ﾏｽﾀｰ出力値2(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata09 = fields.Float(string='Master输出值3(%值)UP平台点0～100%')  # ﾏｽﾀｰ出力値3(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata10 = fields.Float(string='Master输出值4(%值)UP平台点0～100%')  # ﾏｽﾀｰ出力値4(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata11 = fields.Float(string='Master输出值5(%值)UP平台点0～100%')  # ﾏｽﾀｰ出力値5(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata12 = fields.Float(string='Master输出值6(%值)UP平台点0～100%')  # ﾏｽﾀｰ出力値6(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata13 = fields.Float(string='Master输出值7(%值)UP平台点0～100%')  # ﾏｽﾀｰ出力値7(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata14 = fields.Float(string='Master输出值6(%值)DOWN平台点0～100%')  # ﾏｽﾀｰ出力値６(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata15 = fields.Float(string='Master输出值5(%值)DOWN平台点0～100%')  # ﾏｽﾀｰ出力値5(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata16 = fields.Float(string='Master输出值4(%值)DOWN平台点0～100%')  # ﾏｽﾀｰ出力値4(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata17 = fields.Float(string='Master输出值3(%值)DOWN平台点0～100%')  # ﾏｽﾀｰ出力値3(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata18 = fields.Float(string='Master输出值2(%值)DOWN平台点0～100%')  # ﾏｽﾀｰ出力値2(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata19 = fields.Float(string='Master输出值1(%值)DOWN平台点0～100%')  # ﾏｽﾀｰ出力値1(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata20 = fields.Float(string='褶皱输出值1(mA值)UP平台点0～100%')  # ﾜｰｸ出力値１(mA値) ＵＰ ﾃｽﾄ点0～100%
    sdata21 = fields.Float(string='褶皱输出值2(mA值)UP平台点0～100%')  # ﾜｰｸ出力値2(mA値) ＵＰ ﾃｽﾄ点0～100%
    sdata22 = fields.Float(string='褶皱输出值3(mA值)UP平台点0～100%')  # ﾜｰｸ出力値3(mA値) ＵＰ ﾃｽﾄ点0～100%
    sdata23 = fields.Float(string='褶皱输出值4(mA值)UP平台点0～100%')  # ﾜｰｸ出力値4(mA値) ＵＰ ﾃｽﾄ点0～100%
    sdata24 = fields.Float(string='褶皱输出值5(mA值)UP平台点0～100%')  # ﾜｰｸ出力値5(mA値) ＵＰ ﾃｽﾄ点0～100%
    sdata25 = fields.Float(string='褶皱输出值6(mA值)UP平台点0～100%')  # ﾜｰｸ出力値6(mA値) ＵＰ ﾃｽﾄ点0～100%
    sdata26 = fields.Float(string='褶皱输出值7(mA值)UP平台点0～100%')  # ﾜｰｸ出力値7(mA値) ＵＰ ﾃｽﾄ点0～100%
    sdata27 = fields.Float(string='褶皱输出值6(mA值)DOWN平台点0～100%')  # ﾜｰｸ出力値6(mA値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata28 = fields.Float(string='褶皱输出值5(mA值)DOWN平台点0～100%')  # ﾜｰｸ出力値5(mA値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata29 = fields.Float(string='褶皱输出值4(mA值)DOWN平台点0～100%')  # ﾜｰｸ出力値4(mA値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata30 = fields.Float(string='褶皱输出值3(mA值)DOWN平台点0～100%')  # ﾜｰｸ出力値3(mA値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata31 = fields.Float(string='褶皱输出值2(mA值)DOWN平台点0～100%')  # ﾜｰｸ出力値2(mA値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata32 = fields.Float(string='褶皱输出值1(mA值)DOWN平台点0～100%')  # ﾜｰｸ出力値１(mA値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata33 = fields.Float(string='直线值1(%值)UP平台点0～100%')  # 直線性１(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata34 = fields.Float(string='直线值2(%值)UP平台点0～100%')  # 直線性2(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata35 = fields.Float(string='直线值3(%值)UP平台点0～100%')  # 直線性3(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata36 = fields.Float(string='直线值4(%值)UP平台点0～100%')  # 直線性4(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata37 = fields.Float(string='直线值5(%值)UP平台点0～100%')  # 直線性5(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata38 = fields.Float(string='直线值6(%值)UP平台点0～100%')  # 直線性6(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata39 = fields.Float(string='直线值5(%值)DOWN平台点0～100%')  # 直線性５(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata40 = fields.Float(string='直线值4(%值)DOWN平台点0～100%')  # 直線性4(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata41 = fields.Float(string='直线值3(%值)DOWN平台点0～100%')  # 直線性3(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata42 = fields.Float(string='直线值2(%值)DOWN平台点0～100%')  # 直線性2(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata43 = fields.Float(string='直线值1(%值)DOWN平台点0～100%')  # 直線性1(%値) ＤＯＷＮ ﾃｽﾄ点0～100%
    sdata44 = fields.Float(string='HYS1(%值)UP平台点0～100%')  # ＨＹＳ１(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata45 = fields.Float(string='HYS2(%值)UP平台点0～100%')  # ＨＹＳ2(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata46 = fields.Float(string='HYS3(%值)UP平台点0～100%')  # ＨＹＳ3(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata47 = fields.Float(string='HYS4(%值)UP平台点0～100%')  # ＨＹＳ4(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata48 = fields.Float(string='HYS5(%值)UP平台点0～100%')  # ＨＹＳ5(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata49 = fields.Float(string='HYS6(%值)UP平台点0～100%')  # ＨＹＳ6(%値) ＵＰ ﾃｽﾄ点0～100%
    sdata50 = fields.Float(string='MAX线性(%值)错误时+100')  # ＭＡＸ直線性(%値) エラー時 +100
    sdata51 = fields.Float(string='HS值100%错误')  # ＭＡＸＨＹＳ(%値) エラー時 +100
    sdata52 = fields.Float(string='MAX精度(%值)错误时+100')  # ＭＡＸ精度  (%値) エラー時 +100
    sdata53 = fields.Float(string='电源变动11V(mA值)20mA的恒定电流模式')  # 電源変動11V(mA値) 20mAの定電流モード
    sdata54 = fields.Float(string='电源变动45V(mA值)20mA的恒定电流模式')  # 電源変動45V(mA値) 20mAの定電流モード
    sdata55 = fields.Float(string='电源变动误差(%值)判定值：±0.05%÷10V以内')  # 電源変動誤差(%値) 判定値:±0.05%÷10V 以内
    sdata56 = fields.Float(string='负荷变动10Ω(mA值)20mA的恒定电流模式')  # 負荷変動10Ω(mA値) 20mAの定電流モード
    sdata57 = fields.Float(string='负荷变动650Ω(mA值)20mA的恒定电流模式')  # 負荷変動650Ω(mA値) 20mAの定電流モード
    sdata58 = fields.Float(string='负荷变动误差(%值)判定值：±0.065%以内')  # 負荷変動誤差(%値) 判定値:±0.065% 以内
    sdata59 = fields.Selection([('0', '未实验'),
                                ('1', '良品'),
                                ('2', '不良品'),
                                ], string='综合试验结果')  # 総合試験結果 0:未試験 1:良品 2:不良品
    sdata60 = fields.Selection([('0', '无'),
                                ('1', '有'),
                                ('2', '有大气'),
                                ], string='测量点信息1')  # 測定点情報１ 0:無 1:有 2:大気有り
    sdata61 = fields.Selection([('0', '无'),
                                ('1', '有'),
                                ('2', '有大气'),
                                ], string='测量点信息2')  # 測定点情報2 0:無 1:有 2:大気有り
    sdata62 = fields.Selection([('0', '无'),
                                ('1', '有'),
                                ('2', '有大气'),
                                ], string='测量点信息3')  # 測定点情報3 0:無 1:有 2:大気有り
    sdata63 = fields.Selection([('0', '无'),
                                ('1', '有'),
                                ('2', '有大气'),
                                ], string='测量点信息4')  # 測定点情報4 0:無 1:有 2:大気有り
    sdata64 = fields.Selection([('0', '无'),
                                ('1', '有'),
                                ('2', '有大气'),
                                ], string='测量点信息5')  # 測定点情報5 0:無 1:有 2:大気有り
    sdata65 = fields.Selection([('0', '无'),
                                ('1', '有'),
                                ('2', '有大气'),
                                ], string='测量点信息6')  # 測定点情報6 0:無 1:有 2:大気有り
    sdata66 = fields.Selection([('0', '无'),
                                ('1', '有'),
                                ('2', '有大气'),
                                ], string='测量点信息7')  # 測定点情報7 0:無 1:有 2:大気有り
    sdata67 = fields.Float(string='基准比例范围(输入值)')  # ベーススケールレンジ （入力値）
    sdata68 = fields.Float(string='全比例范围(输入值)')  # フルスケールレンジ （入力値）
    sdata69 = fields.Float(string='mmH2O单位换算值')  # mmH2O単位換算値
    sdata70 = fields.Float(string='实际压力值1换算输入值')  # 実際の圧力値１ 入力値を換算
    sdata71 = fields.Float(string='实际压力值2换算输入值')  # 実際の圧力値2 入力値を換算
    sdata72 = fields.Float(string='实际压力值3换算输入值')  # 実際の圧力値3 入力値を換算
    sdata73 = fields.Integer(string='实际压力值4换算输入值')  # 実際の圧力値4 入力値を換算
    sdata74 = fields.Float(string='实际压力值5换算输入值')  # 実際の圧力値5 入力値を換算
    sdata75 = fields.Float(string='实际压力值6换算输入值')  # 実際の圧力値6 入力値を換算
    sdata76 = fields.Float(string='实际压力值7换算输入值')  # 実際の圧力値7 入力値を換算
    sdata77 = fields.Float(string='产品跨度(电缆天台-水平轴)×mmH2O换算值')  # 製品スパン （ﾌﾙｽｹｰﾙﾚﾝｼﾞ－ﾍﾞｰｽｽｹｰﾙﾚﾝｼﾞ）×mmH2O換算値
    sdata78 = fields.Selection([('0', 'KAKB'),
                                ('1', 'KCKD'),
                                ], string='实际刻度标记')  # 実目盛りフラグ 0:KAKB 1:KCKD
    sdata79 = fields.Selection([('0', '1%'),
                                ('1', '1.5%'),
                                ('2', '2%'),
                                ], string='判定值')  # 判定表％値 0:1% 0.5:1.5% 2:2%
    sdata80 = fields.Float(string='产品MAX压力值')  # 製品ＭＡＸ圧力値
    sdata81 = fields.Selection([('0', '压差计'),
                                ('1', '压力计'),
                                ('2', '绝对压力'),
                                ], string='产品种类')  # 製品種別 0:圧差計 1:圧力計 2:絶対圧
    sdata82 = fields.Float(string='')
    sdata83 = fields.Selection([('1', '通常'),
                                ('3', '再实验'),
                                ], string='再次测试信息')  # 製品種別 0:圧差計 1:圧力計 2:絶対圧
    sdata84 = fields.Float(string='')
    sdata85 = fields.Float(string='')
    sdata86 = fields.Selection([('0', '0.1'),
                                ('1', '0.2'),
                                ('2', '流量计')
                                ], string='判定值')  # 判定値 0:0.1 1:0.2 2:流量計
    sdata87 = fields.Float(string='输入较大值(绝对值较大)')  # 入力の大きい値（絶対値の大きい方）
    sdata88 = fields.Float(string='十进制值(&H103→4355)')  # コード％の１０進数値（&H1103→4355）
    sdata89 = fields.Float(string='产品跨度(mA值)')  # 製品スパン（mA値）
    sdata90 = fields.Float(string='D/A：Z(mA值)测量值')  # Ｄ／Ａ：Ｚ（mA値）測定値
    sdata91 = fields.Float(string='D/A：S(mA值)测量值')  # Ｄ／Ａ：S（mA値）測定値
    sdata92 = fields.Float(string='A/D：Z(mA值)测量值')  # Ａ／Ｄ：Ｚ（mA値）測定値
    sdata93 = fields.Float(string='A/D：S(mA值)测量值')  # Ａ／Ｄ：Ｓ（mA値）測定値
    sdata94 = fields.Float(string='A/D：Z(PV值)测量值')  # Ａ／Ｄ：Ｚ（PV値）測定値
    sdata95 = fields.Float(string='A/D：S(PV值)测量值')  # Ａ／Ｄ：Ｓ（PV値）測定値
    sdata96 = fields.Float(string='错误No')  # エラーＮｏ．
    sdata97 = fields.Float(string='错误代码(测试项目)')  # エラーコード（テスト項目）
    sdata98 = fields.Float(string='精度(实际的判断精度)')  # 精度（実際の判定精度）
    sdata99 = fields.Float(string='最终测试项目(0～20的标志)')  # 最終テスト項目（0～20のフラグ）
    udf = fields.Integer()
    lineno = fields.Char()
