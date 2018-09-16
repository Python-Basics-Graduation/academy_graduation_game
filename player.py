
class Player:
    """
    Args:
        name (string) - name of the player
    Returns:
        score (int) - points gained by winning with opponent
        units (array of units objects) - list of avalible units during a game
        account_balance (int) - cash that will topup before every turn
    """
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.units = []
        self.account_balance = 0

    def top_up_account(amount):
        self.account_balance = sel.account_balance + amount
        return self.account_balance

    def gain_point(points_amount):
        self.score = self.score + points_amount
        return self.score
