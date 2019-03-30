# _*_ coding: utf-8 _*_
WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']

#「曜日」と「勉強時間」を、同じfor文内で回します。
#休日（木曜）と平日をif文で分岐さて、メッセージを分けました。
#N限目と勉強内容を同じ行に表示させるために、zip関数を利用しました。
#各曜日のN限目に表示される勉強内容が日が変わるとPythonから表示されてしまいます。

def output_schedule(study_time_list, holiday):
    '''今週の勉強予定を出力します'''
    index = 1
    for today_study_time, day_of_the_week  in zip(study_time_list, WEEK_LIST):
        if day_of_the_week == holiday:
            print('{}曜日は、お休みです。'.format(holiday))
        else:
            print('{0}曜日は、{1}時間勉強する予定です。'.format(day_of_the_week,today_study_time))
            for period in range(today_study_time):
                print('{0}限目 {1}'.format(period+1,SUBJECT_LIST[index]))
                index += 1
                if index == 5:
                    index = 0
                       
def main():
    '''勉強情報をoutput_scheduleに渡します'''
    # 1日に何時間勉強するか（1週間　月曜日〜日曜日）
    study_time_list = [3, 1, 3, 0, 4, 2, 2]
    holiday = WEEK_LIST[3]
    output_schedule(study_time_list,holiday)    

#モジュールとしてimportされた場合、Pythonは「__name__」変数にモジュール名（03-02-python-set.py）を代入します。
#そのため、当該ファイル（モジュール）をimportしても実行されません。
#当該ファイルを直接実行した場合（Pythonの引数として直接実行）には、
#「__name__」変数に「__main__」という文字列を代入しますので、main()関数が呼び出されます。
if __name__ == '__main__':
    main()
