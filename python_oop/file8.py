class  ma:
    def run(self):
        print("跑")
class lv:
    def tuo(self):
        print("驼东西")
class luo(ma,lv):
    pass
luozi = luo()
luozi.run()
luozi.tuo()