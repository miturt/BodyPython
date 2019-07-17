# BodyPython
iPhone で作成した　ｃｓｖファイルを解析、処理するための Python コードです。
Jupyter notebook (または jupyterlab)を使いました。
## bodycsv.py
モジュールファイルです。
## Graph1.ipnb
csvファイルを読み込み基本的なグラフを描画するcellを集めました。

1. ジャイロスコープ　３軸　gyroX , gyroY , gyroZ
1. 加速度の各軸方向のグラフ　accelX accelY accselZ
1. 単位重力ベクトルのｘｙｚ方向の値　gravX gravY gravZ
1. 姿勢＝各軸周りの角度　attrPitch attrRoll attrYaw
1. 時間軸の拡大
1. さらに拡大
1. 時間をつなげる

## 周波数分析
高速フーリエ変換（FFT)による周波数分析です。

窓関数としてハニング窓を適用したれいです。
実行する前に　８，９行目のデータファイルの指定、および４１，４２行目の区間の指定を変更してください。
