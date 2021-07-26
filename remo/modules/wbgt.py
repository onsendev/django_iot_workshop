
class Wbgt():

    def __init__(self, wbgt_value, css_bg_class, description):
        self.wbgt_value = wbgt_value
        self.css_bg_class = css_bg_class
        self.description = description
    
    @staticmethod
    def of(templature, humidity):
        # このクラスにある__calculate_wbgtメソッドを呼び出し、熱中症指数(WBGT)を計算しましょう。
        
        # 計算した熱中症指数をもとに、このクラスのインスタンスを生成してreturnしましょう。
        
        return None
    
    @staticmethod
    def __calculate_wbgt(templature, humidity):
        # 熱中症指数を計算してreturnしましょう。
        return 0

    
    def __str__(self):
        return f"{self.wbgt_value}, description={self.description}, css_bg={self.css_bg_class}"
        
