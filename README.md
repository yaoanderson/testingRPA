# testingRPA
testingRPA is software testing project which is wrote by Anderson.Yao, one SDET in China. This project is one software testing process automation project which can reduce your duplicate working in creating and updating manual and automation test cases and make it effective and efficient, in order that they can focus on test design and data preparation much more but not writing and update duplicate test cases daily.
This project is the first release version, and will be enhanced in the future. Thanks for any feedback after your using :)

One simple "UI / Login" function case which I have showed you in "user" directory, if you want to create one new case, just 3 steps you need to do as below:
1. Prepare one case config file in "user -> config" directory like "ui_login.ini" format.
2. Add new case class (eg: LoginUICase) and map in "user -> case -> __init__.py" file.
3. Add new manual and automation case template files in "user -> case -> template" directory.
After finishing above 3 steps, you can run command and generate manual and automation test cases any time, the run command as below:
python3 ./main.py login[,xxx] [ui]
By the way, I have used pict tool in this project, and default pict execution file (core -> common directory) is built for Mac OS, so if you run this project in Windows or Linux, you should download pict and built it again. (https://github.com/Microsoft/pict)

If your test data will be changed, you do not have to spend much time to update all test cases which is related to these data, and you just need to update data config file then run command again to generate all test cases file again, That's it.

Thanks for any feedback after your using :)
