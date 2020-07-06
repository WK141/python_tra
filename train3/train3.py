#課題1 MP3Player クラスの作成
class Mp3player:
    def play_music(self):
        print("音楽を再生します")

    def next_song(self):
        print("次の曲を再生します")

    def previous_song(self):
        print("前の曲を再生します")

    def stop_music(self):
        print("音楽を止めます")


#課題2 MP3Player をインスタンス化し、それぞれのメソッドを呼び出す
mp3 = Mp3player()
mp3.play_music()
mp3.next_song()
mp3.previous_song()
mp3.stop_music()


#課題3 CellPhone クラスの作成
class Cellphone:
    def __init__(self, tel_number, mail_address):
        self.tel_number = tel_number
        self.mail_address = mail_address 

    def call(self):
        print(self.tel_number + "から発信します")

    def send_mail(self):
        print(self.mail_address + "から送信します")


#課題4 CellPhone クラスをインスタンス化し、それぞれのメソッドを呼び出す
cellphone = Cellphone("080-1111-1111","w.ishii@a-force.co.jp")
cellphone.call()
cellphone.send_mail()


#課題5 SmartPhone クラスの作成
class Smartphone(Mp3player,Cellphone):
    def printAll(self):
        pass


#課題6 SmartPhone クラスをインスタンス化し、全てのメソッドを呼び出す
smartPhone = Smartphone("080-1111-1111","w.ishii@a-force.co.jp")
smartPhone.play_music()
smartPhone.next_song()
smartPhone.previous_song()
smartPhone.stop_music()
smartPhone.call()
smartPhone.send_mail()