# Fx Qwerty

Various keyboard layouts for your F(x)tec Pro1 physical keyboard:

- (Sym->漢字) F(x)tec Pro1 Qwerty - US
- (Sym->漢字) F(x)tec Pro1 Qwerty - US - Fn+Tab
- (Sym->漢字) F(x)tec Pro1 Qwerty - US - Shift as Fn
- (Sym->漢字) F(x)tec Pro1 Qwerty - US - Shift as Fn - Fn+Tab

See the based [Fx Qwerty website](https://slions.net/resources/fx-qwerty.7/) for layout maps *and I changed `Sym` to `半角/全角漢字(ZENKAKU_HANKAKU)`.*

**(Affect: `Power(Alt + Sym)`) is not working)**

The layouts are provided via the Android standard layouts mechanism and are selectable in Android settings - no root required.

## Installing

see latest [releases](https://github.com/epser/hwkbd_kanji/releases).

## Building

Python 3 is required to build.

The project uses Gradle and can be built with Android Studio or via commandline, for example:

```
export JAVA_HOME="$HOME/android-studio/jre"
export ANDROID_HOME="$HOME/Android/Sdk"
./gradlew assembleDebug
```

## Layout files

Most layouts are generated from other layouts automatically by `generate_layouts.py`
during the build process and are therefore not found in this repository.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Credits

This project was forked from [Fx Qwerty](https://github.com/Slion/hwkbd), and referred to [8796.jp管理日誌(Gemini PDAのキーボードレイアウトを変更するやつ)](https://blog.8796.jp/8796kanri/2018/06/gemini-pda%E3%81%A7%E3%81%AF%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%82%AB%E3%83%83%E3%83%88%E3%81%8C%E4%BE%BF%E5%88%A9.html).
