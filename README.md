# Fx Kanji Mod

Various keyboard layouts for your F(x)tec Pro1 physical keyboard with `半角/全角漢字(ZENKAKU_HANKAKU)`:

![f(x)-kanji-mod-based-fx-qwerty](https://user-images.githubusercontent.com/8068831/88495105-db366880-cff3-11ea-859d-e9ea4fd1ab01.png)

- Fx Qwerty Compatible
- Fx Qwerty Compatible - Fn+Tab
- Fx Qwerty Compatible - Shift as Fn
- Fx Qwerty Compatible - Shift as Fn - Fn+Tab

See the based [Fx Qwerty website](https://slions.net/resources/fx-qwerty.7/) for layout maps.

and more variants, Meta-key(Fx Logo) combinations:

![f(x)-kanji-mod-with-metakey](https://user-images.githubusercontent.com/8068831/88495259-5b5cce00-cff4-11ea-9e63-707d9d9be144.png)

- Fx Qwerty with Meta-Key
- Fx Qwerty with Meta-Key - Fn+Tab
- Fx Qwerty with Meta-Key - Shift as Fn
- Fx Qwerty with Meta-Key - Shift as Fn - Fn+Tab

The layouts are provided via the Android standard layouts mechanism and are selectable in Android settings - no root required.

## Installing

[Google Play Store](https://play.google.com/store/apps/details?id=net.eps_r.hwkbd_kanji.FxTecPro1KanjiMod) or apk file on [releases](https://github.com/epser/hwkbd_kanji/releases).

## Documentation

Japanese documentation is [Fx Kanji Mod ドキュメント - eps_r](https://eps-r.hatenablog.com/entry/2020/07/29/fx-kanji-mod-document).

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

This project was forked from [Fx Qwerty](https://github.com/Slion/hwkbd), and referred to [8796.jp管理日誌(Gemini PDAのキーボードレイアウトを変更するやつ)](https://blog.8796.jp/8796kanri/2018/06/gemini-pda%E7%94%A8user-installable-keymaps%E3%81%AE%E3%81%BE%E3%81%A8%E3%82%81.html).
