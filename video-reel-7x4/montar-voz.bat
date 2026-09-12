@echo off
REM montar-voz.bat - pega la locucion definitiva sobre el reel mudo (Windows)
REM Deja los WAV en audio\voz-explicacion.wav y audio\voz-cta.wav y haz doble clic.
cd /d "%~dp0"
ffmpeg -y -i reel-7x4.mp4 -i audio\voz-explicacion.wav -i audio\voz-cta.wav ^
 -filter_complex "[1:a]adelay=150|150[a1];[2:a]adelay=15250|15250[a2];[a1][a2]amix=inputs=2:normalize=0,aresample=48000[a]" ^
 -map 0:v -map "[a]" -t 20 -c:v copy -c:a aac -b:a 192k reel-7x4-final.mp4
echo listo -^> reel-7x4-final.mp4
pause
