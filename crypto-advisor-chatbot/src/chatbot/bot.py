class CryptoBuddy:
    def __init__(self, advisor):
        self.advisor = advisor

    def respond_to_query(self, query):
        if "profitability" in query:
            return self.advisor.get_profitability_advice()
        elif "sustainability" in query:
            return self.advisor.get_sustainability_advice()
        else:
            return "I'm sorry, I can only provide advice on profitability and sustainability."