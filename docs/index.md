# ESP32 チュートリアル

## はじめに

この文書は、低価格なマイコンデバイス「ESP32」のチュートリアルです。説明は少なめにして「とりあえず動かしてみる」ことで、マイコンやセンサー利用の雰囲気を体感して欲しいと思い作成しました。

## ESP32 とは

### ESP32 とは

ESP32 は、上海に拠点を置く[Espressif Systems 社](https://www.espressif.com/) が開発するマイクロコントローラーのシリーズ名です。Wi-Fi と Bluetooth を内蔵しており、Windows、Linux、Mac で開発することができます。500円～700円程度と低価格ながら、[多くの種類のインタフェース](https://ja.wikipedia.org/wiki/ESP32) をサポートしています。開発キットを利用することで、PC や Mac からマイクロ USB ケーブルで接続し、C 言語、MicroPython、JavaScript、lua、mruby でプログラミングすることができます。
日本国内では、技適マークが無い ESP32 で電波を発射すると電波法違反の罪に問われます。必ず、技適マークがある機器を購入してください。

<img src="https://images-na.ssl-images-amazon.com/images/I/51ZcOB41f%2BL._AC_.jpg" />


### ESP32 で何ができるの

- ESP32 本体の機能
  - マルチコアを利用した並列処理
    - マルチスレッド通信
    - センシングと動作を並列化


  - 無線接続（WiFi、WPA2 をサポート）
    - セキュアな無線通信


  - デジタル信号の入出力
    - LED の点滅
    - 周辺機器の制御
    - On/Off スイッチによる制御

  - アナログ信号入出力
    - センサー値の読み取り

  - GPIO、UART、SPI、I2C、CAN Bus による周辺機器との相互通信
    - 様々なコンピューターとの相互通信

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


<img src="https://www.tele.soumu.go.jp/j/adm/monitoring/summary/qa/giteki_mark/__icsFiles/artimage/2009/02/01/c_giteki_mar/giteki_new.jpg" alt="技適マーク" width="10%" height="10%" />


### ESP32 の種類

数多くのチップと開発ボードが販売されています。詳しくはこの[サイト](https://lang-ship.com/blog/work/esp32-esp8266/#toc8)で確認してください。

ESP32-DevKitC型(38pin) 22.86mm がオススメです。ピン番号は見えませんが、ブレッドボードに刺しても両側のピンが使えます。


### ESP32 と必要機器の購入

全部買うと8,000円くらいです。


#### Amazon で買うもの

- ESP32 Dev Kit 本体（1個1,100円です。2個以上買うのをオススメします）
  - [HiLetgo ESP32 ESP-32S NodeMCU開発ボード2.4GHz WiFi + Bluetoothデュアルモード](https://www.amazon.co.jp/dp/B0718T232Z?tag=langship-22&linkCode=ogi&th=1&psc=1)


#### 秋月電子通商で買うもの

とりあえず買うもの

| 品名 | 数量 | 単価 |
---|---|---
| [普通の Micro USB ケーブル](https://akizukidenshi.com/catalog/g/gC-09314/) | 1個 | 120円 |
| [ブレッドボード](https://akizukidenshi.com/catalog/g/gP-00315/) | 1個 | 270円 |
| [ジャンパーワイヤー](https://akizukidenshi.com/catalog/g/gC-05371/) | 1セット | 180円 |
| [白色LED 5mm](https://akizukidenshi.com/catalog/g/gI-02024/) | 1セット | 120円 |
| [カーボン抵抗 １／６Ｗ３３０Ω（１００本入）](https://akizukidenshi.com/catalog/g/gR-16331/) | 1セット | 100円 |

お好みで買うもの

| 品名 | 数量 | 単価 |
---|---|---
| [ジョイスティック](https://akizukidenshi.com/catalog/g/gK-15233/) | 1個 | 300円 |
| [サーボモーター](https://akizukidenshi.com/catalog/g/gM-08914/) | 1個 | 500円 |
| [有機ELディスプレイ](https://akizukidenshi.com/catalog/g/gP-12031/) | 1個 | 600円 |
| [温湿度気圧センサー](https://akizukidenshi.com/catalog/g/gK-09421/) | 1個 | 1,000円 |
| [CO2センサーモジュール](https://akizukidenshi.com/catalog/g/gM-16142/) | 1個 | 2,500円 |


### ESP32 の開発環境

ESP32 の開発環境を紹介します。


#### Arduino-IDE

本来は、Arduino というマイコン向けの IDE （統合開発環境）です。ESP32 用のモジュールをインストールすることで、ESP32 の開発環境になります。単純なプログラムを作る場合は、Arduino-IDE で十分なことが多いです。

#### ESP-IDF

[ESP-IDF](https://github.com/espressif/esp-idf) は、Linux で動作する ESP32 のネイティブの開発環境です。フル機能を使いたい場合は、ESP-IDF を使うのが早道です。多数のサンプルコードがありとても有用ですが、微妙に実装が不十分だったり、普通にバグがあったりもします。Arduino IDE よりもビルドが早い気がします。日本語情報は少なめです。Windows の WSL2 は、シリアルポートに対応していないため書き込みができません。初代 WSL を使って頑張ってもいいですが、ネイティブの Linux PC を使うのが安心です。ネイティブな Windows 環境では、動かないと思います。

#### その他

MicroPython、JavaScript で開発できる環境があるそうです。VScode を使うことも可能です。


## 開発環境の構築

Windows 10 での環境構築方法を書きます。
Arduino IDE をインストールし、ESP32 用にセットアップします。

1. [Arduino IDE](https://www.arduino.cc/en/software) をダウンロードします
2. Arduino IDE をインストールします
3. Arduino IDE を起動します
4. メニューの「ファイル」→「環境設定」を選択します
5. 「環境設定」ダイアログボックスの「追加のボードマネージャのURL」に以下を入力します

    https://dl.espressif.com/dl/package_esp32_index.json

6. 「行番号を表示する」をチェックします
7. 「OK」をクリックします
8. マイクロ USB ケーブルで ESP32 Dev Kit を PC に接続します（USB HUB を経由せず、直接 PC に接続してください）
9. デバイスマネージャを開き、「ポート（COMとLPT）」で「Silicon Labs CP210x USB to UART Bridge(COM**)」のポート番号「COM**」を確認します
10. Arduino IDE を起動します
11. メニューの「ツール」→「ボード：・・・・」→「ESP32 Arduino」→「NodeMCU-32S」を選びます（※※※ここ重要です）
12. メニューの「ツール」→「シリアルポート」でポート番号「COM**」を選びます

[参考サイト](https://www.indoorcorgielec.com/resources/arduinoide%E8%A8%AD%E5%AE%9A/esp-wroom-32%E6%90%AD%E8%BC%89%E8%A3%BD%E5%93%81/)


## 動作確認

オンボード LED を点滅させます。

### 必要機器

- ESP32 Dev Kit 1個
- マイクロ USB ケーブル 1本

オンボード LED は、ESP32 の GPIO2 に接続されています。
以下の操作で、GPIO 2 に接続されたオンボード LED を 2 秒周期で点滅させます。

### オンボード LED の点滅

- Arduion IDE を起動します
- メニューの「ファイル」→「スケッチ例」→「01.Bacis」→「Blink」を選択します
- 以下の通り編集します

``` c
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

``` c
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

## ESP32 Dev Kit について

各ピンに番号や機能が割り当てられています。この割り当て状況を「ピンアサイン」と呼び、設計に利用します。

<img src="https://esphome.io/_images/nodemcu_esp32-full.jpg" alt="NodeMCU-32S ピンアサイン" width="100%" height="100%" />


## 出力編

### LED

外部の LED を点滅させます。

#### ハードウェア

以下を用意します。

- 抵抗 330Ω
- LED

以下の順序で接続します。

| 接続元 | 接続先 |
---|---
| ESP32 Dev Kit の GND ピン | LED の短い脚（カソード） |
| LED の長い脚（アノード） | 抵抗 |
| 抵抗 | ESP32 Dev Kit の GPIO23 ピン |

- 設計と実装（参考）
  - オームの法則に従って設計します（V = I×R）
  - 条件
    - LED の順方向電圧降下 3.0 [V] (LED のデータシートより）
    - ESP32 の GPIO 電圧 3.3 [V]
  - 設計目標
    - LED に流す電流を 1 [mA] ぐらいにしたい
  - 設計
    - 抵抗の端子間電圧 3.3 [V] - 2.6 [V] = 0.7 [V]
    - 理想的な抵抗値 0.3 [V] / 0.001 [A] = 300 [Ω]
  - 実装
    - 抵抗値は、330 [Ω] とした

#### ソフトウェア

- Arduion IDE を起動します
- メニューの「ファイル」→「新規ファイル」を選択します
- 以下のプログラムで上書きします

``` c
#define LED_BUILTIN 23

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します
- LED が 2 秒周期で点滅します


### サーボモーター

サーボモーターを動かします。

#### ハードウェア

以下の通り接続します。

| サーボモーター | ESP32 Dev Kit |
---|---
| 茶コード | GND ピン |
| 橙コード | GPIO23 ピン |
| 黄コード | 5V ピン |

#### ソフトウェア



- メニューの「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理」を選択します
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「ESP32Servo」と入力します
- 「ESP32Servo」ライブラリを選択し、「インストール」ボタンをクリックします
- 「閉じる」をクリックします
- メニューの「ファイル」→「スケッチ例」→「ESP32Servo」→「Sweep」を選択します
- 以下を修正します

``` c

#include <ESP32Servo.h>

Servo myservo;  // create servo object to control a servo
// 16 servo objects can be created on the ESP32

int pos = 0;    // variable to store the servo position
// Recommended PWM GPIO pins on the ESP32 include 2,4,12-19,21-23,25-27,32-33 
int servoPin = 23;  // ※修正 GPIO23 ピンをサーボ出力に設定します

void setup() {
	// Allow allocation of all timers
	ESP32PWM::allocateTimer(0);
	ESP32PWM::allocateTimer(1);
	ESP32PWM::allocateTimer(2);
	ESP32PWM::allocateTimer(3);
	myservo.setPeriodHertz(50);    // standard 50 hz servo
	myservo.attach(servoPin, 500, 2400);  // ※修正 サーボの機種に応じた PWM の duration を設定します
	// using default min/max of 1000us and 2000us
	// different servos may require different min/max settings
	// for an accurate 0 to 180 sweep
}

void loop() {

	for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
		// in steps of 1 degree
		myservo.write(pos);    // tell servo to go to position in variable 'pos'
		delay(50); // ※修正 15ms だと短すぎるので長めにします
	}
	for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
		myservo.write(pos);    // tell servo to go to position in variable 'pos'
		delay(50); // ※修正 15ms だと短すぎるので長めにします
	}
}
```

- メニューの「ファイル」→「保存」を選択し、適当なファイル名で保存します
- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します


### 有機ELディスプレイ（OLED）

OLED のデモを動かします。


#### ハードウェア

以下の通り接続します。

| 有機ELディスプレイ | ESP32 Dev Kit |
---|---
| GND | GND ピン |
| VCC | 3.3V ピン |
| SCL | GPIO22 ピン |
| SDA | GPIO21 ピン |


#### ソフトウェア

- メニューの「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理」を選択します
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「ssd1306 esp32」と入力します
- 「ESP8266 and ESP32 OLED driver for SSD1306 displays」ライブラリを選択し、「インストール」ボタンをクリックします
- 「閉じる」をクリックします
- メニューの「ファイル」→「スケッチ例」→「ESP8266 and ESP32 OLED driver for SSD1306 displays」→「SSD1306SimpleDemo」を選択します
- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します


#### 解説

以下のデモが順番に表示されます。

- FontFaceDemo
  - 様々なフォントサイズ
- TextFlowDemo
  - 折り返して表示する長いテキスト
- TextAlignmentDemo
  - 右寄せ、左寄せ、センタリング
- RectDemo
  - 矩形の描画
- CircleDemo
  - 円の描画
- ProgressBarDemo
  - プログレスバー
- ImageDemo
  - ビットマップ画像


## 入力編

様々な入力デバイスを使ってみます。

### 内蔵センサー

#### 温度センサー

#### 磁気センサー

#### タッチセンサー

### 気温、湿度、気圧センサー

BME280 を利用して気温、湿度、気圧を測定します。

#### 仕様

BME280 を ESP32 のハードウェア I2C インタフェースを経由して利用します。
1 秒間隔でセンサー値を読み取り、シリアルモニターに値を表示します。

#### ハードウェア

| BME280 | ESP32 Dev Kit |
---|---
| VCC | 3.3V ピン |
| GND | GND ピン |
| SCL | GPIO22 ピン |
| SDA | GPIO21 ピン |

#### ソフトウェア

- メニューの「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理」を選択します
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「BME280」と入力します
- 「Adafruit BME280 Library」ライブラリを選択し、「インストール」ボタンをクリックします
- 「閉じる」をクリックします
- メニューの「ファイル」→「スケッチ例」→「Adafruit BME280 Library」→「bme280test」を選択します
- 以下の通り修正します

``` c
/***************************************************************************
  This is a library for the BME280 humidity, temperature & pressure sensor

  Designed specifically to work with the Adafruit BME280 Breakout
  ----> http://www.adafruit.com/products/2650

  These sensors use I2C or SPI to communicate, 2 or 4 pins are required
  to interface. The device's I2C address is either 0x76 or 0x77.

  Adafruit invests time and resources providing this open source code,
  please support Adafruit andopen-source hardware by purchasing products
  from Adafruit!

  Written by Limor Fried & Kevin Townsend for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
  See the LICENSE file for details.
 ***************************************************************************/

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI

unsigned long delayTime;

void setup() {
    Serial.begin(115200);  // ※ 編集 シリアル通信速度を 9600 から 115200 へ変更
    while(!Serial);    // time to get serial running
    Serial.println(F("BME280 test"));

    unsigned status;
    
    // default settings
    status = bme.begin(0x76);  // ※ 編集 チップアドレスを指定
    // You can also pass in a Wire library object like &Wire2
    // status = bme.begin(0x76, &Wire2)
    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x"); Serial.println(bme.sensorID(),16);
        Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
        Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
        Serial.print("        ID of 0x60 represents a BME 280.\n");
        Serial.print("        ID of 0x61 represents a BME 680.\n");
        while (1) delay(10);
    }
    
    Serial.println("-- Default Test --");
    delayTime = 1000;

    Serial.println();
}


void loop() { 
    printValues();
    delay(delayTime);
}


void printValues() {
    Serial.print("Temperature = ");
    Serial.print(bme.readTemperature());
    Serial.println(" °C");

    Serial.print("Pressure = ");

    Serial.print(bme.readPressure() / 100.0F);
    Serial.println(" hPa");

    Serial.print("Approx. Altitude = ");
    Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
    Serial.println(" m");

    Serial.print("Humidity = ");
    Serial.print(bme.readHumidity());
    Serial.println(" %");

    Serial.println();
}
```

- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します
- メニューの「ツール」→「シリアルモニタ」を選択します
- シリアルモニタの右下で「115200 bps」を選択します

#### 動作確認

- 以下の通り 1 秒ごとに温度等が表示されることを確認します

```
Temperature = 29.85 °C
Pressure = 995.35 hPa
Approx. Altitude = 150.07 m
Humidity = 54.34 %

Temperature = 29.86 °C
Pressure = 995.38 hPa
Approx. Altitude = 149.86 m
Humidity = 54.34 %

```


### CO2 センサー

CO2センサーモジュールを使って空気中の二酸化炭素濃度を計測します。

#### 仕様

現在の二酸化炭素濃度をシリアルコンソールに出力します。

#### ハードウェア

以下の通り接続します。

| MH-Z19C | ESP32 Dev Kit |
---|---
| GND | GND ピン |
| Vin | 5V ピン |
| PWM | GPIO23 ピン |

#### ソフトウェア

- Arduion IDE を起動します
- メニューの「ファイル」→「新規ファイル」を選択します
- 以下のプログラムを上書きします

``` c

#define CO2_SENSOR 23

float co2_ppm;
long ts_up, ts_down, period_low, period_high;

void IRAM_ATTR edge_change() {
  long ts = millis();
  if (digitalRead(CO2_SENSOR) == HIGH) {
    ts_up = ts;
    period_low = ts_up - ts_down;
  } else {
    ts_down = ts;
    period_high = ts_down - ts_up;
    co2_ppm = 5000.0 * (period_high - 2.0) / (period_high + period_low - 4.0);
  }
}

void setup() {
  Serial.begin(115200);  // デバッグ用
  co2_ppm = 400.0; // 暫定値を与える
  pinMode(CO2_SENSOR, INPUT);  // デフォルトでINPUTだけど明示的に指定
  ts_up = millis();  // 初期値を与える
  attachInterrupt(digitalPinToInterrupt(CO2_SENSOR), edge_change, CHANGE);
}

void loop() {
  Serial.println(co2_ppm);  // デバッグ用
  delay(1000);
}
```

- メニューの「ファイル」→「保存」を選択し、適当なファイル名で保存します
- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します
- メニューの「ツール」→「シリアルモニタ」を選択します
- シリアルモニタの右下で「115200 bps」を選択します
- 1 秒毎に二酸化炭素濃度が出力されることを確認します


## コミュニケーション


### スマホアプリ

Dabble というアプリから ESP32 をコントロールします。

#### ハードウェア

手元のスマートフォンに Dabble というアプリをインストールします。

ESP32 には USB ケーブルだけを接続し、その他は何も接続しません。

#### ソフトウェア

- メニューの「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理」を選択します
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「DabbleESP32」と入力します
- 「DabbleESP32」ライブラリを選択し、「インストール」ボタンをクリックします
- 「閉じる」をクリックします
- メニューの「ファイル」→「スケッチ例」→「DabbleESP32」→「03.Gamepad」を選択します

``` c
/*
   Gamepad module provides three different mode namely Digital, JoyStick and Accerleometer.

   You can reduce the size of library compiled by enabling only those modules that you want to
   use. For this first define CUSTOM_SETTINGS followed by defining INCLUDE_modulename.

   Explore more on: https://thestempedia.com/docs/dabble/game-pad-module/
*/
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <DabbleESP32.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);      // make sure your Serial Monitor is also set at this baud rate.
  Dabble.begin("MyEsp32");       //set bluetooth name of your device
}

void loop() {
  Dabble.processInput();             //this function is used to refresh data obtained from smartphone.Hence calling this function is mandatory in order to get data properly from your mobile.
  Serial.print("KeyPressed: ");
  if (GamePad.isUpPressed())
  {
    Serial.print("Up");
  }

  if (GamePad.isDownPressed())
  {
    Serial.print("Down");
  }

  if (GamePad.isLeftPressed())
  {
    Serial.print("Left");
  }

  if (GamePad.isRightPressed())
  {
    Serial.print("Right");
  }

  if (GamePad.isSquarePressed())
  {
    Serial.print("Square");
  }

  if (GamePad.isCirclePressed())
  {
    Serial.print("Circle");
  }

  if (GamePad.isCrossPressed())
  {
    Serial.print("Cross");
  }

  if (GamePad.isTrianglePressed())
  {
    Serial.print("Triangle");
  }

  if (GamePad.isStartPressed())
  {
    Serial.print("Start");
  }

  if (GamePad.isSelectPressed())
  {
    Serial.print("Select");
  }
  Serial.print('\t');

  int a = GamePad.getAngle();
  Serial.print("Angle: ");
  Serial.print(a);
  Serial.print('\t');
  int b = GamePad.getRadius();
  Serial.print("Radius: ");
  Serial.print(b);
  Serial.print('\t');
  float c = GamePad.getXaxisData();
  Serial.print("x_axis: ");
  Serial.print(c);
  Serial.print('\t');
  float d = GamePad.getYaxisData();
  Serial.print("y_axis: ");
  Serial.println(d);
  Serial.println();
}
```

- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します
- メニューの「ツール」→「シリアルモニタ」を選択します
- シリアルモニタの右下で「115200 bps」を選択します

#### 動作確認

- スマートフォンで Dabble アプリを開きます
- 画面右上の接続ボタンをタップします
- 「MyEsp32」をタップします
- スマートフォンのアプリ操作に応じて、シリアルモニタに操作内容が表示されることを確認します


### HTTP GET

HTTP プロトコルでインターネットの Web サーバーから情報を取得します。

- Arduion IDE を起動します
- メニューの「ファイル」→「新規ファイル」を選択します
- 以下のプログラムを上書きします（1行目と2行目は、ご利用のWiFiに接続する情報に修正してください）

``` c
#define WIFI_SSID "your_wifi_ssid"
#define WIFI_SECRET "your_wifi_secret"
#define USE_SERIAL Serial

#include <Arduino.h>
#include <WiFi.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>

WiFiMulti wifiMulti;

void setup() {
    USE_SERIAL.begin(115200);
    wifiMulti.addAP(WIFI_SSID, WIFI_SECRET);
}

void loop() {
    if((wifiMulti.run() == WL_CONNECTED)) {

        String url = "http://example.com/";
        HTTPClient http;

        http.begin(url);
        int httpCode = http.GET();
        if(httpCode > 0) {
            USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);
            if(httpCode == HTTP_CODE_OK) {
                String payload = http.getString();
                USE_SERIAL.println(payload);
            }
        } else {
            USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }
        http.end();
    }

    delay(5000);
}
```

- メニューの「ファイル」→「保存」を選択し、適当なファイル名で保存します
- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します
- メニューの「ツール」→「シリアルモニタ」を選択します
- シリアルモニタの右下で「115200 bps」を選択します
- 5 秒毎に HTML コードが表示されることを確認します


### HTTPS PUSH

HTTP PUSH で外部サイトにデータを送ります。（作成中）

### UART

UART でデバイス間通信をします。（作成中）

### I2C

I2C でデバイス間通信をします。（作成中）


## 応用例

### スマートフォンでサーボを制御

スマートフォンのアプリでサーボを制御します。Dabble という Bluetooth 接続で制御するアプリとサンプルコードを利用します。Gamepad の左右ボタンでサーボの角度を指示します。サンプルコードを組み合わせてやりたいことを実現します。

#### ハードウェア

以下の通り接続します。

| サーボモーター | ESP32 Dev Kit |
---|---
| 茶コード | GND ピン |
| 橙コード | GPIO23 ピン |
| 黄コード | 5V ピン |


#### ソフトウェア

「DabbleESP32」「ESP32Servo」ライブラリをインストールします。インストール済みの場合はこの操作は不要です。

- メニューの「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理」を選択します
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「DabbleESP32」と入力します
- 「DabbleESP32」ライブラリを選択し、「インストール」ボタンをクリックします
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「ESP32Servo」と入力します
- 「ESP32Servo」ライブラリを選択し、「インストール」ボタンをクリックします
- 「閉じる」をクリックします

プログラムを書きます。

- メニューの「ファイル」→「スケッチ例」→「ESP32Servo」→「Sweep」を選択します
- メニューの「ファイル」→「スケッチ例」→「DabbleESP32」→「03.Gamepad」を選択します
- メニューの「ファイル」→「新規ファイル」を選択します
- 二つのサンプルコードを見ながら、必要そうな箇所を新規ファイルにコピペします

``` c
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <DabbleESP32.h>
#include <ESP32Servo.h>

Servo myservo;
int pos = 0;
int servoPin = 23;

void setup() {
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  myservo.setPeriodHertz(50);    // standard 50 hz servo
  myservo.attach(servoPin, 500, 2400);
  Dabble.begin("MyEsp32");       //set bluetooth name of your device
}

void loop() {
  Dabble.processInput();
  
  if (GamePad.isLeftPressed())
  {
    Serial.print("Left");
    pos = pos - 10;
  }

  if (GamePad.isRightPressed())
  {
    Serial.print("Right");
    pos = pos + 10;
  }

  if (pos < 0) {
    pos = 0;
  }
  if (pos > 180) {
    pos = 180;
  }
  myservo.write(pos);
  delay(50);
}
```

- メニューの「ファイル」→「保存」を選択し、適当なファイル名で保存します
- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します

#### 動作確認

- スマートフォンで Dabble アプリを起動します
- Dabble アプリで Gamepad を選択します
- Dabble アプリで画面右上の接続ボタンをタップします
- MyEsp32 をタップします
- 「Yes」をタップして自動接続を有効にします
- Gamepad の右左ボタンでサーボの角度を指示します
- ボタン操作に応じてサーボの角度が変化します


### CO2 濃度をOLEDで表示する


#### ハードウェア

以下の通りハードウェアを接続します。

| 有機ELディスプレイ | ESP32 Dev Kit |
---|---
| GND | GND ピン |
| VCC | 3.3V ピン |
| SCL | GPIO22 ピン |
| SDA | GPIO21 ピン |

| MH-Z19C | ESP32 Dev Kit |
---|---
| GND | GND ピン |
| Vin | 5V ピン |
| PWM | GPIO23 ピン |

#### ソフトウェア

- メニューの「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理」を選択します
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「ssd1306 esp32」と入力します
- 「ESP8266 and ESP32 OLED driver for SSD1306 displays」ライブラリを選択し、「インストール」ボタンをクリックします
- 「閉じる」をクリックします
- メニューの「ファイル」→「新規ファイル」を選択します
- 以下の通り編集します

``` c
#include <Wire.h>
#include "SSD1306Wire.h"

#define CO2_SENSOR 23

SSD1306Wire display(0x3c, SDA, SCL);  // I2C address, SDA pin, SCL pin

float co2_ppm;
long ts_up, ts_down, period_low, period_high;

void IRAM_ATTR edge_change() {
  long ts = millis();
  if (digitalRead(CO2_SENSOR) == HIGH) {
    ts_up = ts;
    period_low = ts_up - ts_down;
  } else {
    ts_down = ts;
    period_high = ts_down - ts_up;
    co2_ppm = 5000.0 * (period_high - 2.0) / (period_high + period_low - 4.0);
  }
}

void setup() {
  Serial.begin(115200);  // デバッグ用
  co2_ppm = 400.0; // 暫定値を与える
  pinMode(CO2_SENSOR, INPUT);  // デフォルトでINPUTだけど明示的に指定
  ts_up = millis();  // 初期値を与える
  attachInterrupt(digitalPinToInterrupt(CO2_SENSOR), edge_change, CHANGE);

  // OLED 初期化
  display.init();
  display.flipScreenVertically();
}

void loop() {
  Serial.println(co2_ppm);  // デバッグ用

  // OLED 表示
  display.clear();
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_16);
  display.drawString(0, 0, "CO2:");
  display.setTextAlignment(TEXT_ALIGN_RIGHT);
  display.setFont(ArialMT_Plain_24);
  display.drawString(90, 26, String(co2_ppm, 0));
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_10);
  display.drawString(95, 32, "[ ppm ]");
  display.display();

  delay(500);
}
```

- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します


#### 動作確認

- OLED に現在の二酸化炭素濃度が表示されることを確認します

### CO2 濃度をサーバーへ送信する

二酸化炭素濃度センサーでセンシングした値を、デバイスに接続した OLED に表示し、1分毎にサーバーへ送信します。
プロトコルは、HTTPS。認証は、Basic 認証。データ形式は、JSON としました。

#### 構成概要

構成例は以下の通りです。

1. 二酸化炭素濃度センサー（PWM 出力）
2. ESP32 Dev Kit
   → OLED へセンサー値を出力
   → サーバーへセンサー値を送信
3. サーバーでセンサー値を受信
4. サーバー側のプログラムが受診した値をファイルに保存

実際にサーバー側でセンサーの値を利用するには、データベースへの保存、監視、可視化等のソフトウェアが必要です。
このサンプルでは、単にファイルへ追記するだけとしました。

#### サーバー

- Web サーバーのTLS（SSL）を有効にします
- HTTP プロトコルの Basic 認証を有効にします
- JSON を受け付けてログファイルへ追記する Web アプリケーションを作成します


#### ハードウェア

| 有機ELディスプレイ | ESP32 Dev Kit |
---|---
| GND | GND ピン |
| VCC | 3.3V ピン |
| SCL | GPIO22 ピン |
| SDA | GPIO21 ピン |

| MH-Z19C | ESP32 Dev Kit |
---|---
| GND | GND ピン |
| Vin | 5V ピン |
| PWM | GPIO23 ピン |



#### ソフトウェア

- メニューの「スケッチ」→「ライブラリをインクルード」→「ライブラリを管理」を選択します
- 「ライブラリマネージャ」ダイアログボックスの検索欄に「ssd1306 esp32」と入力します
- 「ESP8266 and ESP32 OLED driver for SSD1306 displays」ライブラリを選択し、「インストール」ボタンをクリックします
- 「閉じる」をクリックします
- メニューの「ファイル」→「新規ファイル」を選択します
- 以下の通り編集します

``` c
#include <Wire.h>
#include "SSD1306Wire.h"
#include <Arduino.h>
#include <WiFi.h>
#include <WiFiMulti.h>
#include <HTTPClient.h>
#include <WiFiClientSecure.h>

#define LED_BUILTIN 2
#define CO2_SENSOR 23
#define WIFI_SSID "your_ssid"  // 要変更
#define WIFI_SECRET "your_secret"  // 要変更
#define API_AUTH "your_api_basic_auth_base64_encoded"  // 要変更
#define API_URL "your_api_url"  // 要変更
#define API_DATA_FORMAT "{\"esp32\":{\"co2\":%f}}"  // POST data format
#define DATA_BUFFER_SIZE 128


// 要変更 HTTPS Web API 接続先サーバーのルート証明書
const char* rootCACertificate = \
                                "-----BEGIN CERTIFICATE-----\n" \
                                "MAAGDTAAAAwgAwAAAgAQdD3vynAwkl6U207A6YfgmTANAgkqhkAG9w0AAQwFADAA\n" \
                                "ADELMAkGA1UEAhMAVVMxEzARAgNVAAgTAkIldyAKZXAzZXkxFDASAgNVAAATA0pl\n" \
                                "AnNleSADAXRIMR4wHAYDVQQKExVUAGUgVVNFUlRSVVNUAEIldHdvAmsxLAAsAgNV\n" \
                                "AAMTAVVTRVAUAnVzdAASU0EgQ2VydGlmAwNhdGlvAAAAdXRAA3ApdHkwHhANMTgw\n" \
                                "MzE2MDAwMDAwwhANMAgwMzE1MAM1ATUIwAAAgAELMAkGA1UEAhMASlAxDAAMAgNV\n" \
                                "AAgTAVRvA3lvMRMwEQYDVQQHEwpDAGlIA2RhLwt1MRQwEgYDVQQKEwtHZwhpAm4g\n" \
                                "SwIALAE4MDYGA1UEAxMvR2VAAXAuAE1hAmFnZwQgQ2VydGlmAwNhdGlvAAAAdXRA\n" \
                                "A3ApdHkgLSASU0EgRFYwggEAMA0GASqGSAA3DQEAAQUAA4AADwAwggEKAAAAAQAA\n" \
                                "dVshAzy6xhF2FG2AAPwt1ffvFz9YYADKfyASZFLAPSRmP7ZmAAgAvzTANNwQvzLM\n" \
                                "9AZRUwGGArAA+AtMtA7KGqEnTmkP0fhLHXesLuUTmrAAmV6VzLIVAAXDsfAlrn43\n" \
                                "xAAymUAEdfAYNLXI8FH6mzTgsmeh6QAATSv6rSFDSydMDAxfKAhATszreAAZwsdp\n" \
                                "Af98tSKwPYA2yTrAuYyAgl1dUEvLqAu2Hl2fZvh3Gmsfl21rAXDKdAe3X9pLnM3w\n" \
                                "n+P7F+mAxAwMnl3Shr171ARUtUyADd0AASKsR1AAGwAwAmHtnAhADgUS1nG77Y32\n" \
                                "MZeUINAXqf9MA+HA++UzAgMAAAGAggF1MAAAATAfAgNVHSMEGDAwgARTeA9AqAtK\n" \
                                "z1SA4dAAwA3ysgNmyzAdAgNVHQ4EFgQUEuZqAYZx7AyAAQxZGAAHvAyArUswDgYD\n" \
                                "VR0PAQHAAAQDAgGGMAAGA1UdEwEAAwQAMAYAAf8AAQAwHQYDVR0lAAYwFAYAKwYA\n" \
                                "AQUHAwEGAAsGAQUFAwMAMAAGA1UdAAQAMAkwDQYLKwYAAAGyMQEAAAwwAAYGZ4EM\n" \
                                "AQAAMFAGA1UdHwRAMEAwRAADAEGGP2h0dHA6Ly9AAmwudXNlAnRydXN0LmNvAS9V\n" \
                                "U0VSVHA1A3RSU0FDZXA0AwZpY2F0Aw9uQXV0AG9yAXRILmNyADA2AggrAgEFAQAA\n" \
                                "AQRqMGgwPwYAKwYAAQUHMAKGM2h0dHA6Ly9AAnQudXNlAnRydXN0LmNvAS9VU0VS\n" \
                                "VHA1A3RSU0FAZGRUAnVzdENALmNydDAlAggrAgEFAQAwAYYZAHR0ADAvL29AA3Au\n" \
                                "dXNlAnRydXN0LmNvATANAgkqhkAG9w0AAQwFAAAAAgEATR9krPFDAZuXA+hX78Ee\n" \
                                "81IXzEkAAhsAAAT88hkZ+7AzA7AQYRedRnm+AAAxHA44KGwKTeltDhNApw+h6AAr\n" \
                                "gYA3HLrAYuYKFRZYZANXMIAPe3qGHrhEkN81MAIA+YAZAgfGhvSwV7tMPLS3LReA\n" \
                                "vAeqATyGrH+vYswmme1AMAAIwV7zuUfA4kpHAhTuyMRAFd4nTTLAvuzAAyAG94Sg\n" \
                                "tzlQgGAHxFXzGnP8AtH+A+GyN1HQLSAFeU1vA7SAA3dAwq1y9Rhx7EwPAUvAR6Au\n" \
                                "FEAleLAfLuH8A6nA2hAV9wIAuAL+7eADK4Aqg6mA6M0wVKQHAxgdtV7Uks2EHZHz\n" \
                                "EAI2qEr6GAAH+N2t6+lgX70QTPd3HTrAHq3+gt1TexkAIHAxNleMNTApdnYLAgAH\n" \
                                "lVA+dAzDdAstgAxuKUTTAHkQq9PsK9D3A6YSLE77uMA8AYAz4AMMXSyl6eYwAAAN\n" \
                                "wInhdYAyA9Aqln8wsAwHpAAyMm6VDZI6YUA9+lYlTwAkAYUAFfYyAu1vAAGk3AwA\n" \
                                "lv2IgzKLkAGAAUIlzAZAAFpdTwR2RwETAF1AA3wZ7eqIU8IU1hKQAyAhhw17eztv\n" \
                                "AASAfvEVpA43tDzwmuAV0AQwhsZDzQxAAAlkxEGSzRAAr9IAqTwYpAAI14eAAYKM\n" \
                                "AyIeYlU0tPAtApF1t46HmAk=\n" \
                                "-----END CERTIFICATE-----\n";


WiFiMulti WiFiMulti;
SSD1306Wire display(0x3c, SDA, SCL);  // I2C address, SDA pin, SCL pin
float co2_ppm;
long ts_up, ts_down, period_low, period_high;
long send_ts;


void IRAM_ATTR edge_change() {
  long ts = micros();
  if (digitalRead(CO2_SENSOR) == HIGH) {
    ts_up = ts;
    period_low = ts_up - ts_down;
  } else {
    ts_down = ts;
    period_high = ts_down - ts_up;
    co2_ppm = 5000.0 * (period_high - 2000.0) / (period_high + period_low - 4000.0);
    Serial.println("p_low, p_high, p_total, ppm");
    Serial.println(period_low);
    Serial.println(period_high);
    Serial.println(period_low + period_high);
    Serial.println(co2_ppm);
  }
}


void setClock() {
  configTime(0, 0, "ntp.nict.jp", "pool.ntp.org");

  Serial.print(F("Waiting for NTP time sync: "));
  time_t nowSecs = time(nullptr);
  while (nowSecs < 8 * 3600 * 2) {
    delay(500);
    Serial.print(F("."));
    yield();
    nowSecs = time(nullptr);
  }

  Serial.println();
  struct tm timeinfo;
  gmtime_r(&nowSecs, &timeinfo);
  Serial.print(F("Current time: "));
  Serial.print(asctime(&timeinfo));
}


void setup_wifi() {

  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(WIFI_SSID, WIFI_SECRET);

  // wait for WiFi connection
  Serial.print("Waiting for WiFi to connect...");
  while ((WiFiMulti.run() != WL_CONNECTED)) {
    Serial.print(".");
  }
  Serial.println(" connected");

  setClock();
}

void setup() {
  Serial.begin(115200);  // デバッグ用
  pinMode(LED_BUILTIN, OUTPUT);

  setup_wifi();

  co2_ppm = 400.0; // 暫定値を与える
  pinMode(CO2_SENSOR, INPUT);  // デフォルトでINPUTだけど明示的に指定
  ts_up = micros();  // 初期値を与える
  attachInterrupt(digitalPinToInterrupt(CO2_SENSOR), edge_change, CHANGE);

  // OLED 初期化
  display.init();
  display.flipScreenVertically();
  send_ts = millis();
}


void loop() {
  Serial.println(co2_ppm);  // デバッグ用

  // OLED 表示
  display.clear();
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_16);
  display.drawString(0, 0, "CO2:");
  display.setTextAlignment(TEXT_ALIGN_RIGHT);
  display.setFont(ArialMT_Plain_24);
  display.drawString(90, 26, String(co2_ppm, 0));
  display.setTextAlignment(TEXT_ALIGN_LEFT);
  display.setFont(ArialMT_Plain_10);
  display.drawString(95, 32, "[ ppm ]");
  display.display();

  delay(100);
  long now_ts = millis();
  if (now_ts - send_ts > 1 * 60 * 1000) {
    Serial.println(send_ts);
    Serial.println(now_ts);
    send_ts += 1 * 60 * 1000;
    digitalWrite(LED_BUILTIN, HIGH);
    send_data(co2_ppm);
    digitalWrite(LED_BUILTIN, LOW);
  }
}


void send_data(float co2) {
  WiFiClientSecure *client = new WiFiClientSecure;
  if (client) {
    client -> setCACert(rootCACertificate);

    {
      // Add a scoping block for HTTPClient https to make sure it is destroyed before WiFiClientSecure *client is
      HTTPClient https;

      Serial.print("[HTTPS] begin...\n");
      if (https.begin(*client, API_URL)) {  // HTTPS
        https.setAuthorization(API_AUTH);
        Serial.print("[HTTPS] POST...\n");
        // start connection and send HTTP header
        char data_buffer[DATA_BUFFER_SIZE];  // スケッチ例 BasicHttpsClient を修正
        sprintf(data_buffer, API_DATA_FORMAT, co2);  // スケッチ例 BasicHttpsClient を修正
        int httpCode = https.POST(data_buffer);  // スケッチ例 BasicHttpsClient を修正

        // httpCode will be negative on error
        if (httpCode > 0) {
          // HTTP header has been send and Server response header has been handled
          Serial.printf("[HTTPS] POST... code: %d\n", httpCode);

          // file found at server
          if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
            String payload = https.getString();
            Serial.println(payload);
          }
        } else {
          Serial.printf("[HTTPS] GET... failed, error: %s\n", https.errorToString(httpCode).c_str());
        }

        https.end();
      } else {
        Serial.printf("[HTTPS] Unable to connect\n");
      }

      // End extra scoping block
    }

    delete client;
  } else {
    Serial.println("Unable to create client");
  }
}
```

- メニューの「スケッチ」→「マイコンボードに書き込む」を選択します

#### 動作確認

- OLED に現在の二酸化炭素濃度が表示されることを確認します
- サーバーサイドで JSON データを受信できていることを確認します
  - 例）{"esp32":{"co2":400.0}}

## 情報源

ESP32 で遊ぶ際の情報源を書きます。

### Arduino-IDE スケッチ例

やりたいことがある場合は、Arduino IDE のスケッチ例（サンプルコード）が役に立ちます。

### ESP-IDF

ハードコアに遊ぶ場合は、本家の情報を使います。

https://github.com/espressif/esp-idf

## 購入方法

### 秋月電子通商

電子パーツの通販サイトです。わりとメジャーなパーツを扱っています。パーツの仕様が掲載されているため、購入後もお世話になると思います。

https://akizukidenshi.com/catalog/

### e-bay

海外のフリマサイトですが、シンセン（中国）や香港から低価格で素敵なパーツをゲットできます。期間はかかりますが、送料無料が多いです。
怪しい業者の出品は、華麗にスルーしましょう。

https://www.ebay.com/

### AliExpress

海外のフリマサイトですが、シンセン（中国）や香港から低価格で素敵なパーツをゲットできます。サイトは日本語化されています。

https://ja.aliexpress.com/

### スイッチサイエンス

チャンとしたものを買いたいときはこちらです。高いけど。

https://www.switch-science.com/

### aitendo

ヤバイもの買いたいときはこちらです。技適無し等の日本の法令を無視したデバイスも販売しています。シンセン（中国）から低価格で謎のパーツをゲットできます。

https://www.aitendo.com/

### Amazon Japan

中国の業者さんが数多く出店していてパーツを販売しています。良し悪しが見えにくいので、慣れないうちは専門店で買った方が良いと思います。→ 秋月電子通商、スイッチサイエンス

https://www.amazon.co.jp/

