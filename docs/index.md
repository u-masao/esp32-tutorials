# ESP32 チュートリアル

## はじめに

この文書は、ESP32 のチュートリアルです。

## ESP32 とは

### ESP32 とは

ESP32 は、上海に拠点を置く[Espressif Systems 社](https://www.espressif.com/) が開発するマイクロコントローラーのシリーズ名です。Wi-Fi と Bluetooth を内蔵しており、Windows、Linux、Mac で開発することができます。500円～700円程度と低価格ながら、[多くの種類のインタフェース](https://ja.wikipedia.org/wiki/ESP32) をサポートしています。開発キットを利用することで、PC や Mac からマイクロ USB ケーブルで接続し、C 言語、MicroPython、JavaScript、lua、mruby でプログラミングすることができます。日本国内では、技適マークが無い ESP32 で電波を発射すると電波法違反の罪に問われます。必ず、技適マークがある機器を購入してください。

<img src="https://images-na.ssl-images-amazon.com/images/I/51ZcOB41f%2BL._AC_.jpg" />


### ESP32 でできること

- ESP32 本体ができること
  - マルチコアを利用した並列処理
    - マルチスレッド通信
    - センシングと動作を並列化


  - 無線接続（WPA2 をサポート）
    - セキュアな無線通信を実現


  - デジタル信号入出力
    - LED の点滅
    - 周辺機器の制御

  - アナログ信号入出力
    - センサー値の読み取り

  - GPIO、UART、SPI、I2C、CAN Bus による周辺機器との相互通信
    - 様々な周辺機器との相互通信

  - PWM、I2S、DAC による信号出力
    - サーボモーター等の制御
    - 音声信号の出力
    - 電圧信号の出力

  - タッチセンサーによる接触入力
    - タッチスイッチの読み取り

  - SD カードアクセス
    - SD カードからの読み出し
    - SD カードへの保存

  - 各種割込み（タイマー、GPIO）

  - 超低電力スリープ


- ESP32 に接続した周辺機器でできること

  - 各種センサーの利用
    - スイッチ、ジョイスティック
    - ボリューム
    - 温度、湿度、気圧、CO2、照度センサー
    - 加速度、角加速度センサー
    - 振動センサー
    - 音センサー（マイク）
    - 超音波センサー
    - 距離センサー
    - 磁気センサー
    - 圧力センサー
    - 電流センサー
    - カメラ
    - リアルタイムクロック

  - 各種出力機器の利用
    - LED、LCD、OLED
    - スピーカー
    - DCモーター、サーボモーター、ステッピングモーター
    - ソレノイド
    - リレー、FET、MOS-FET
      - 電源ON/OFFで動作するあらゆる機器

  - 各種コンピューターと通信
    - Wi-Fi、Bluetooth で通信可能な機器
    - UART、SPI、I2C、CAN Bus で通信可能な機器

### ESP32 の種類と買い方

#### 技適マークに注意

[総務省から注意喚起](https://www.tele.soumu.go.jp/j/adm/monitoring/summary/qa/giteki_mark/)が出ています。

> 一般に使用する無線機の殆どに特定無線設備の技術基準適合証明等のマーク（技適マーク）が付いています。
技適マークが付いていない無線機は、「免許を受けられない／違法になる」恐れがありますので無線機を購入・使用する際は十分ご注意下さい。


<img src="https://www.tele.soumu.go.jp/j/adm/monitoring/summary/qa/giteki_mark/__icsFiles/artimage/2009/02/01/c_giteki_mar/giteki_new.jpg" alt="技適マーク" width="20%" height="20%" />


### ESP32 の種類

この[サイト](https://lang-ship.com/blog/work/esp32-esp8266/#toc8)で確認してください。

ESP32-DevKitC型(38pin) 22.86mm がオススメです。


### ESP32 と必要機器の購入

一通り買います。全部買うと8,000円くらいです。

#### Amazon で買うもの

- ESP32 Dev Kit 本体（1個1,100円です。2個以上買うのをオススメします）
  - [HiLetgo ESP32 ESP-32S NodeMCU開発ボード2.4GHz WiFi + Bluetoothデュアルモード](https://www.amazon.co.jp/dp/B0718T232Z?tag=langship-22&linkCode=ogi&th=1&psc=1)

<img src="https://esphome.io/_images/nodemcu_esp32-full.jpg" alt="NodeMCU-32S ピンアサイン" width="100%" height="100%" />



#### 秋月電子通商で買うもの

- とりあえず買うもの（1,200円ぐらい）
  - [普通の Micro USB ケーブル](https://akizukidenshi.com/catalog/g/gC-09314/) 1個
  - [ブレッドボード](https://akizukidenshi.com/catalog/g/gP-00315/) 1個
  - [ジャンパーワイヤー](https://akizukidenshi.com/catalog/g/gC-05371/) 1セット
  - [ジョイスティック](https://akizukidenshi.com/catalog/g/gK-15233/) 1個
  - [白色LED 5mm](https://akizukidenshi.com/catalog/g/gI-02024/) 1セット
  - [カーボン抵抗 １／６Ｗ３３０Ω（１００本入）](https://akizukidenshi.com/catalog/g/gR-16331/) 1セット

- お好みで買うもの（4,500円ぐらい）
  - [サーボモーター](https://akizukidenshi.com/catalog/g/gM-08914/) 1個 500円
  - [有機ELディスプレイ](https://akizukidenshi.com/catalog/g/gP-12031/) 1個 600円
  - [温湿度気圧センサー](https://akizukidenshi.com/catalog/g/gK-09421/) 1個 1,000円
  - [CO2センサーモジュール](https://akizukidenshi.com/catalog/g/gM-16142/) 1個 2,500円

### ESP32 の開発環境

主要開発環境の、Arduino-IDE を紹介します。

#### Arduino-IDE

[Arduino IDE](https://www.arduino.cc/en/software)

Arduino というマイコン向けの IDE です。ESP32 用のモジュールをインストールすることで、ESP32 の開発環境になります。単純なプログラムを作る場合は、Arduino-IDE で十分なことが多いです。

#### その他

ESP-IDF、MicroPython 等があります。
[ESP-IDF](https://github.com/espressif/esp-idf) は、Linux で動作する ESP32 のネイティブの開発環境です。フル機能を使いたい場合は、ESP-IDF を使うのが早道です。多数のサンプルコードがありとても有用ですが、微妙に実装が不十分だったり、普通にバグがあったりもします。
Windows の WSL2 は、シリアルポートに対応していないため書き込みができません。初代 WSL を使うか、ネイティブの Linux PC を使うのが安心です。ネイティブな Windows 環境では、動かないと思います。


## 開発環境の構築


### 開発環境のインストール

Arduino IDE をインストールし、ESP32 用にセットアップします。
[こちら](https://www.indoorcorgielec.com/resources/arduinoide%E8%A8%AD%E5%AE%9A/esp-wroom-32%E6%90%AD%E8%BC%89%E8%A3%BD%E5%93%81/)のサイトを参考にしてください。

- 手順概要

  1. Arduino IDE をダウンロードする
  2. Arduino IDE をインストールする
  3. 追加のボードマネージャに ESP32 を設定


### 開発環境の設定

1. USB ケーブルで ESP32 Dev Kit を PC に接続します（USB HUB を経由せず、直接 PC に接続してください）
2. デバイスマネージャを開き、「ポート（COMとLPT）」で「Silicon Labs CP210x USB to UART Bridge(COM*)」のポート番号「COM*」を確認します
3. Arduino IDE を起動します
4. メニューの「ツール」→「ボード：・・・・」→「ESP32 Arduino」→「NodeMCU-32S」を選びます
5. メニューの「ツール」→「シリアルポート」でポート番号「COM*」を選びます


## 動作確認

オンボード LED を点滅させます。

### 必要機器

- ESP32 Dev Kit 1個
- マイクロ USB ケーブル 1本

オンボード LED は、ESP32 の GPIO 2 に接続されています。
以下の操作で、GPIO 2 に接続されたオンボード LED を 2 秒周期で点滅させます。

### オンボード LED の点滅

- Arduion IDE を起動します
- メニューの「ファイル」→「スケッチ例」→「01.Bacis」→「Blink」を選択します
- 以下の通り編集します
```c:
#define LED_BUILTIN 2     /* この行を追加 */

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
```
- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します
- 上手く行くとこんな表示が出ます

```
最大1310720バイトのフラッシュメモリのうち、スケッチが207705バイト（15%）を使っています。
最大327680バイトのRAMのうち、グローバル変数が15228バイト（4%）を使っていて、ローカル変数で312452バイト使うことができます。
esptool.py v2.6
Serial port COM4
Connecting.....
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
MAC: 84:cc:a8:7a:6e:74
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 921600
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 8192 bytes to 47...
Wrote 8192 bytes (47 compressed) at 0x0000e000 in 0.0 seconds (effective 4096.1 kbit/s)...
Hash of data verified.
Compressed 15856 bytes to 10276...
Wrote 15856 bytes (10276 compressed) at 0x00001000 in 0.1 seconds (effective 998.8 kbit/s)...
Hash of data verified.
Compressed 207824 bytes to 105395...
Wrote 207824 bytes (105395 compressed) at 0x00010000 in 1.5 seconds (effective 1109.9 kbit/s)...
Hash of data verified.
Compressed 3072 bytes to 128...
Wrote 3072 bytes (128 compressed) at 0x00008000 in 0.0 seconds (effective 1365.3 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

- ESP32 Dev Kit のオンボードLEDが青く点滅するのを確認します


### シリアル出力（デバッグ）

シリアル出力機能を使うと、デバッグが行えます。


- Arduion IDE を起動します
- メニューの「ファイル」→「新規ファイル」を選択します
- 以下の通り編集します

```
#define LED_BUILTIN 2

void setup() {
  Serial.begin(115200);
  Serial.println("setup pin");
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.println("LED on");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);                    
  Serial.println("LED off");
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```
- メニューの「ファイル」→「保存」を選択し、適当な名前で保存します
- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します
- 上手く行くとこんな表示が出ます

```
最大1310720バイトのフラッシュメモリのうち、スケッチが213249バイト（16%）を使っています。
最大327680バイトのRAMのうち、グローバル変数が15372バイト（4%）を使っていて、ローカル変数で312308バイト使うことができます。
esptool.py v2.6
Serial port COM4
Connecting....
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
MAC: 84:cc:a8:7a:6e:74
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 921600
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 8192 bytes to 47...
Wrote 8192 bytes (47 compressed) at 0x0000e000 in 0.0 seconds (effective 6553.6 kbit/s)...
Hash of data verified.
Compressed 15856 bytes to 10276...
Wrote 15856 bytes (10276 compressed) at 0x00001000 in 0.1 seconds (effective 1112.7 kbit/s)...
Hash of data verified.
Compressed 213360 bytes to 108767...
Wrote 213360 bytes (108767 compressed) at 0x00010000 in 1.6 seconds (effective 1087.2 kbit/s)...
Hash of data verified.
Compressed 3072 bytes to 128...
Wrote 3072 bytes (128 compressed) at 0x00008000 in 0.0 seconds (effective 2048.0 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

- ESP32 Dev Kit のオンボードLEDが青く点滅するのを確認します
- メニューの「ツール」→「シリアルモニタ」を選択します
- シリアルモニタの右下で「115200 bps」を選択します
- ESP32 のリセットボタンを押します
- 以下の表示を確認します

```
LED off
LED on
LED off
LED on
LED off
LED on
LED off
LED on
LED off
LED on
```


## 出力編

### LED

LED と抵抗を直列に接続し、ESP32 の GPIO ピンに接続します。抵抗は、LED や GPIO ピンに流れる電流を制御するために利用します。

### 有機ELディスプレイ

### サーボモーター

## 入力編

### 気温、湿度、気圧センサー

### 内蔵センサー

#### 温度センサー

#### 磁気センサー

#### タッチセンサー

## HTTP 通信

### WiFi 接続設定

### Web Server 構築

簡単なAPIサーバとRRD-Toolsで表示。
[MQTT,Grafana](https://dzone.com/articles/playing-with-docker-mqtt-grafana-influxdb-python-a)

### HTTP GET

### HTTPS PUSH

## コミュニケーション

### UART

### I2C

### TCP/IP

#### HTTP

#### HTTPS

## 情報源

### ESP-IDF

### Arduino-IDE サンプルファイル

### ESP32 DevKit

## 購入方法

### 秋月電子

### e-bay

### aliexpress

### スイッチサイエンス

### Amazon

